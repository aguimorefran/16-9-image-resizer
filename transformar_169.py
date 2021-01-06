import os
from PIL import Image
from PIL import ImageFilter
from math import floor, trunc


#function to get only the first two decimals of a flat
def truncate(number, decimals=0):
    factor = 10.0 ** decimals
    return trunc(number * factor) / factor

image_out_format = ".png"
image_out_extension = "-TRANSFORMADA"+image_out_format

#get images in folder
f = []
for root, dirs, files in os.walk("."):
    for filename in files:
        #check if image is already transformed
        if (filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg")) and (os.path.splitext(filename)[0]+image_out_extension) not in files:
            f.append(filename)

all_169 = True
transformed_images = 0
#iterate over files
for img_filename in f:
    im = Image.open(img_filename)
    im_w, im_h = im.size
    saved_filename = os.path.splitext(img_filename)[0] + image_out_extension
    ratio = im_w / im_h
    #check if image is 16:9 to apply transformation
    if (truncate(ratio,2) != truncate(16/9, 2)):
        all_169 = False
        #create background by upscaling original image and blurring it
        im_w, im_h = im.size
        bg = im.resize((floor(im_w*(16/9*2)), floor(im_h*(16/9*2))))
        bg_w, bg_h = bg.size
        bg = bg.filter(ImageFilter.GaussianBlur(radius=bg.size[1]/150))

        #paste original image
        offset = ((bg_w - im_w)//2,(bg_h - im_h)//2)
        bg.paste(im, offset)

        #crop to 16:9
        left = (bg_w - floor(im_h*(16/9)))/2
        top = (bg_h - im_h)/2
        right = (bg_w + floor(im_h*(16/9)))/2
        bottom = (bg_h + im_h)/2
        dst = bg.crop((left, top, right, bottom))
        #save img
        print("\n-----------------------------------\n")
        print("GUARDANDO IMAGEN ---> " + saved_filename)
        dst = dst.save(saved_filename)
        transformed_images += 1
print("\n-----------------------------------\n")


if all_169:
    print("\n-----------------------------------\n")
    print("TODAS LAS IMAGENES EN 16:9")
    print(f"IMAGENES TRANSFORMADAS = {transformed_images}")        
    print("\n-----------------------------------\n")
