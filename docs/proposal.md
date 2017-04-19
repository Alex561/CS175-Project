---
layout:	default
title:	Proposal
---

## Summary of the Project
Our project is an AI that takes a provided picture and builds it as a vertical portrait in Minecraft. Our input will be a picture saved as a text file and loaded into our AI. The output it produces is a set of vertical blocks designed to look like the picture inputted into the AI. We are planning on finding an external application for converting the picture to a text file in order for our AI to load the image text file then translate it into Minecraft blocks and finally build a replica in the game.  As a second step once we get the builder working and if we have extra time, we plan to find a way to sidestep the external application and build directly from a png file.

## AI/ML Algorithms
Our AI is going to use primary component analysis with k nearest neighbor methods in order to reduce a large image into a smaller minecraft portrait while preserving accuracy.

## Evaluation Plan
For our quantitative evaluation, we plan to determine accuracy by plotting a error rate graph that compares the Minecraft blocks' RGB value to the image's RGB values, which would tell us how close our colors in game are to the colors in the picture. If it becomes obvious that our AI not working then we will reevaluate how our AI translates the input as well as reevaluate the PCA algorithm and make sure our image is maintaining the most important parts of the picture. 

Our qualitative evaluation for our AI will be primarily based on how accurate the replication of the photo is. We will look at both the image in Minecraft and the source; comparing both and focusing on how close a replica the Minecraft image is. Our moonshot case is to be able to create 3D images inside of Minecraft instead of flat 2D portraits. 

## Appointment with the Instructor
We scheduled a meeting for Tuesday (4/25) at 1 PM.
