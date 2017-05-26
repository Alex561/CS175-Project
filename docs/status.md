---
layout:	default
title:	Status
---

## Video Summary
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZhqGhHBmCaw" frameborder="0" allowfullscreen></iframe>

## Project Summary

This project is an AI that takes a provided picture and builds it in Minecraft. The AI takes in an image and processes that image into a collection of pixels, which makes it easier to apply to Minecraft. This is made possible using the external resource Scikit-Image. We also made a dictionary of Minecraft blocks that are available to use in building a vertical image. The AI would then use this dictionary to compare to each pixel and determine the closest blocks to use when recreating the image. The result is a replica of the image built vertically in the Minecraft world environment. Because Minecraft has a vertical limit, large pictures wouldn't be able to be replicated without being cutoff. Therefore, we added a way to resize the image, also made possible by Scikit-Image. We made a GUI to make our project more user friendly by letting users input the image name and desired resize. Additionally, we want to translate an image's perceived depth into Minecraft to create a 3D-looking or pop-up image by situating blocks to recreate that depth, instead of having a flat image.

## Approach
For converting the image into a usable collection, we use Scikit-Image to convert the image into a collection of each pixel’s RGB values. The list of the Minecraft blocks provided is a dictionary full of block IDs, such as “diamond_block”, as keys. The value of each item in the dictionary would be the average RGB values of that block’s texture. We’ve only included a short list of Minecraft blocks so far, excluding many Minecraft blocks that would be unsuitable for creating an accurate image, like stairs or glass. The AI then creates a new image made of blocks by comparing each pixel to the values in the dictionary to find the block with the closest RGB value to the pixel by minimizing the distance error between the 3-tuple representing the RGB values.

Initially, we tried resizing the image using PCA. However, this approach changed the image significantly, as the RGB values mixed in such a way that the colors were completely different from the original. PCA also only resized in one dimension, which further distorted the image. Instead we turned to Scikit-Image once again, which proved to be much more effective at resizing the image the way we expected. For recreating depth, we plan on using an external computer vision library that uses classifiers to distinguish between the different layers of depth. This would then be translated into Minecraft by placing blocks farther away from the player depending the more depth there is.

## Evaluation
For our quantitative evaluation, we determine accuracy by calculating error between the Minecraft blocks’ RGB values to the image’s RGB values. This tells us how close the colors of the replica are to the colors in the picture. These calculations will help us reevaluate how our AI recreates the image and make sure it maintains its most important aspects.

Our qualitative evaluation is primarily based on how accurate the replication the image looks. This includes doing basic visual comparisons between the replica in Minecraft and the original. We also compare the results from trying different algorithms to each other to see which one seems to recreate the image and its depth the best. We will collect feedback from volunteers on these comparisons and use their feedback to think of ways to improve the AI’s accuracy.


## Remaining Goals and Challenges
We have had a few challenges getting to this point. Getting Numpy to work was an issue initially. Another challenge we've had was trying to get PCA working, but being unable to use it in the end. We also had some troubles with time management when working on the project.

Our goal for the next few weeks is making our images 3D-like with depth to them instead of simple portraits like our current implementation of our project.  We plan to do this using computer vision algorithms for detecting depth from a flat image and applying this algorithm to the image and translating this into Minecraft. One challenge we anticipate for this is application difficulty since none of our team has experience working with computer vision. We will also continue evaluating and improving the project.