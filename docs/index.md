---
layout: default
title:  Home
---

![](images/image1.png)

## Summary
Sketchy AI is an AI that takes a provided picture and builds it in Minecraft. The AI takes in an image and processes that image into a collection of pixels, which makes it easier to apply to Minecraft. This is made possible using the external resource Scikit-Image. We also made a dictionary of Minecraft blocks that are available to use in building a vertical image. The AI would then use this dictionary to compare to each pixel and determine the closest blocks to use when recreating the image. The result is a replica of the image built vertically in the Minecraft world environment. Because Minecraft has a vertical limit, large pictures wouldn't be able to be replicated without being cutoff. Therefore, we added a way to resize the image, also made possible by Scikit-Image. We made a GUI to make our project more user friendly by letting users input the image name and desired resize. Additionally, we want to translate an image's perceived depth into Minecraft to create a 3D-looking or pop-up image by situating blocks to recreate that depth, instead of having a flat image.

## Code
If you would like to take a look at our project, you can find it here:
[https://github.com/Alex561/Sketchy-AI](https://github.com/Alex561/Sketchy-AI "Sketchy AI")

## Screenshots
Here are some of the results from our testing. We use a variety of images to test the limits of our project.

### Flat Image Screenshots

Recreation of the symbol for the popular video game Overwatch:

![](images/image2.png)

Here we used an impressive painting of space we randomly found:

<img src="image3.png" width="850" height="450">

An example of the AI using a photo:

![](images/image4.png)

### 3D-ish Image Screenshots


Comparisons of the same photo, but with various parameters:
![](images/tina1.png) 
![](images/tina2.png)

Similarly, a jetty:
![](images/d5.png) 
![](images/d3.png)

Here is another photo:
![](images/idk.png)


## Resources
##### Scikit-Image:
This project used Scikit-Image in order to process its images, but has since moved on to using OpenCV. Scikit-Image is a collection of algorithms used for image processing in Python. Check it out here:

[http://scikit-image.org/](http://scikit-image.org/ "Link to Scikit-Image's Site")

##### OpenCV Image Processing:


[http://docs.opencv.org/master/d2/dbd/tutorial_distance_transform.html](http://docs.opencv.org/master/d2/dbd/tutorial_distance_transform.html)

[https://github.com/opencv/opencv/blob/master/samples/python/distrans.py](https://github.com/opencv/opencv/blob/master/samples/python/distrans.py)

### Computer Vision
Here are some of the computer vision resources that were used in the project.

##### SimpleCV Cookbook: 
[http://simplecv.sourceforge.net/doc/cookbook.html](http://simplecv.sourceforge.net/doc/cookbook.html)