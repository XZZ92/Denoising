# Image denoising

Welcome to my repository with a program for denoising images. 

### What is image noise and denoising?

Image noise is random (not present in the object imaged) variation of brightness or color information in images, and is usually an aspect of electronic noise.
Image denoising is a process of removing noise from an image, while at the same time preserving details and structures.


### Process description:

- read the infile and outfile name
- open infile picture as numpy array and make a copy of it
- for each pixel of the infile:
	- calculate its k-'neighborhood' and save it in a list m 
	- calculate median of elements in list m
	- in new image (outfile), in the position of pixel p (in infile), copy the median of its k-'neighborhood'
- save the new image with an appropriate name
