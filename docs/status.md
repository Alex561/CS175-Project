---
layout:	default
title:	Status
---

## Project Summary

This project is an AI that takes a provided picture and builds it in Minecraft. The AI should take in an image and process that image into a collection of pixels, which would make it easier to apply to Minecraft. This is made possible using the external resource Scikit-Image. We also made a list of Minecraft blocks that are available to use in building a vertical image. The AI would then use this list to compare to the image and determine the closest blocks to use when recreating the image. The result would be a replica of the image built vertically Minecraft world environment.

## Approach
For converting the image into a usable collection, we use Scikit-Image to convert the image into a collection of each pixel’s RGB values. The list of the Minecraft blocks provided is a dictionary full of block IDs, such as “diamond_block”, as keys. The value of each item in the dictionary would be the average RGB values of that block’s texture. We’ve only included a short list of Minecraft blocks so far, excluding many Minecraft blocks that would be unsuitable for creating an accurate image in Minecraft, like stairs or glass. The AI then creates a new image made of blocks by comparing each pixel to the values in the dictionary to find the block with the closest RGB value to the pixel’s RGB value.

Insert another paragraph here.


## Evaluation
For our quantitative evaluation, we plan to determine accuracy by calculating error between the Minecraft blocks’ RGB values to the image’s RGB values. This would tell us how close the colors of the replica are to the colors in the picture. These calculations will help us reevaluate how our AI recreates the image and make sure it maintains its most important aspects.

Our qualitative evaluation will be primarily based on how accurate the replication the image looks. This will include doing basic visual comparisons between the replica in Minecraft and the original. We will also compare the results from different algorithms to each other. We will collect feedback from volunteers on these comparisons, and use their feedback to think of ways to improve the AI’s accuracy.


## Remaining Goals and Challenges
At the moment, there is not much in terms of AI algorithms being used in our project. Unfortunately, we won't be able to add more in this regard by the status report deadline but we have started looking into computer vision ideas that we can apply to the project. One of the more interesting ideas we have are translating an image's perceived depth into Minecraft to create a 3D-looking, or pop-up, image by situating Minecraft blocks that recreates that depth, instead of having a flat image.