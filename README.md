# 16:9 image resizer 

Simple Python scripts that converts all non 16:9 images into 16:9. This is done by either by adding a blurred background to a vertical image or downsizing a wide one. 

The algorithm checks every image in the directory, if it has not yet been transformed and if it is already in 16:9. If not, transform it and save it. It will not transform again images already transformed.

## Idea
My father works as a photo editor and sometimes shoots vertical images. My idea was to make a tool for him that resizes those images locally with no need of online services or having to resize each image one by one. This will allow him to dump all images and let Python do the job.  
Further job is to make an executable to make it universal for him without the need for installing Python and its libraries.

## Make it work
For that, just put the script in the same folder where your images are. It will check every image and transform those not in 16:9 to 16:9.  
