# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #2: Run simple mission using raw XML
from Tkinter import *
import numpy as np
import MalmoPython
import os
import sys
import time

import colors as woolColors
from skimage import io
from skimage.transform import rescale, resize
import Image
# from sklearn import decomposition

# def pca(X, yDim):
#     # Principal Component Analysis
#     # input: X, matrix with training data as flattened arrays in rows
#     # return: projection matrix (with important dimensions first),
#     # variance and mean
#
#     #shape the rgb bands
#     X = flattenColorImage(X)
#
#     svd = decomposition.TruncatedSVD(n_components=yDim, algorithm="arpack")
#
#     svd.fit(X)
#
#     newX = svd.transform(X).astype(int)
#
#     print(newX.shape)
#     print(newX[0,0])
#
#     # return unflattenColorImage(newX) - broken atm, was working on this
#     return newX

# def flattenColorImage(colorImage):
#     flattended = np.zeros(shape=(colorImage.shape[0], colorImage.shape[1]))
#     for y in range(colorImage.shape[0]):
#         newRow = np.zeros(colorImage.shape[1])
#         for x in range(colorImage.shape[1]):
#             newRow[x] = getIfromRGB(colorImage[y][x])
#         flattended[y] = newRow
# 
#     return flattended
# 
# def unflattenColorImage(flattenedImage):
#     unflattended = np.zeros(shape=(flattenedImage.shape[0], flattenedImage.shape[1], 3))
#     for y in range(flattenedImage.shape[0]):
#         newRow = np.zeros(flattenedImage.shape[1])
#         for x in range(flattenedImage.shape[1]):
#             rgbFromI = getRGBfromI(flattenColorImage[y][x])
#             newRow[y][x] = rgbFromI
#         unflattended[y] = newRow
# 
#     return unflattended
# 
# def getRGBfromI(RGBint):
#     blue = RGBint & 255
#     green = (RGBint >> 8) & 255
#     red = (RGBint >> 16) & 255
#     return red, green, blue
# 
# def getIfromRGB(rgb):
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     RGBint = (red << 16) + (green << 8) + blue
#     return RGBint

difList = []

#get resolution button
def getResolution():
    userInputP.get()
    resolution =0
    resolutionLabel=Label(root,text="Resolution: "+str(resolution))
    resolutionLabel.pack()
    resolutionLabel.place(x=150,y=60)
#drawPciture button
def drawPicture():
   userInputH.get()
   userInputW.get()
   userInputP.get()
def QuantitiveEval(difList):
    sum=0
    for i in range(len(difList)):
        sum+=difList[i]
    return sum/len(difList)

def closestColor(pixel, woolDict):
    resultColor = "WHITE"
    minDif = float("inf")
    for wool, colorValue in woolDict.items():
        dif = np.sqrt((pixel[0]-colorValue[0])**2 + (pixel[1]-colorValue[1])**2 + (pixel[2]-colorValue[2])**2)
        if (dif < minDif):
            resultColor = wool
            minDif = dif

    difList.append(minDif)
    return resultColor

def picturefy(pixelArray, woolDict):
    returnString = ""
    isAlpha = False
    if (pixelArray.shape[2] == 4):
        isAlpha = True

    pixelArray = np.rot90(pixelArray, k=2)

    # pixelArray = pca(pixelArray, 100) - broken atm

    xCount = 0
    yCount = 0
    for x in range(pixelArray.shape[1]):
        xCount += 1
        for y in range(pixelArray.shape[0]):
            yCount += 1

            pixelColor = pixelArray[y][x] * 255
            if (isAlpha):
                pixelColor = round(pixelColor[0]), round(pixelColor[1]), round(pixelColor[2]), round(pixelColor[3])
            else:
                pixelColor = round(pixelColor[0]), round(pixelColor[1]), round(pixelColor[2])

            # print(pixelColor)
            if (isAlpha and pixelArray[y][x][3] > 0) or (not isAlpha):
                closestWool = closestColor(pixelColor, woolDict)
                if closestWool in woolColors.wool:
                    returnString += '<DrawBlock x="{0}" y="{1}" z="10" type="wool" colour="{2}"/>\n'.format(x, y+7, closestWool)
                else:
                    returnString += '<DrawBlock x="{0}" y="{1}" z="10" type="{2}"/>\n'.format(x, y+7, closestWool)

    print("({0}, {1}) pixels", xCount, yCount/xCount)
    print(QuantitiveEval(difList))
    return returnString
#initilize gui
root = Tk()
frame = Frame(root, width=300, height=300)
frame.pack()
userInputH = StringVar()#Height Stuff
heightLabel=Label(root,text="Height")
heightLabel.pack()
heightLabel.place(x=20,y=150)
height = Entry(root, text="Black", fg="black",textvariable=userInputH)
height.place(x=60,y=150)

userInputW = StringVar()#width
widthLabel=Label(root,text="Width")
widthLabel.place(x=20,y=100)
width = Entry(root, text="Black", fg="black",textvariable=userInputW)
width.place(x=60,y=100)

userInputP = StringVar()#picture box
pictureLabel=Label(root,text="Picture File")
pictureLabel.place(x=20,y=20)
picture = Entry(root, text="Black", fg="black",textvariable=userInputP)
picture.place(x=90,y=20)

getResolution= Button(root, text ="Get Resolution", command = getResolution)#resolution button
getResolution.pack()
getResolution.place(x=30,y=60)

drawPicture = Button(root, text ="Draw picture", command = drawPicture)#draw button
drawPicture.pack()
drawPicture.place(x=75,y=200)

#picture stuff
imageFile = "Tina.jpg"
image = io.imread(imageFile)
image = resize(image, (200, 200))

import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

              <About>
                <Summary>Hello world!</Summary>
              </About>

              <ServerSection>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,0,5*3,2;3;,biome_1" forceReset="true"/>
                  <DrawingDecorator>
                    ''' + picturefy(image, woolColors.colors) + '''
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="1000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>

              <AgentSection mode="Survival">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x="0.5" y="8.0" z="0.5" yaw="0"/>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse(sys.argv)
except RuntimeError as e:
    print
    'ERROR:', e
    print
    agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print
    agent_host.getUsage()
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission(my_mission, my_mission_record)
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print
            "Error starting mission:", e
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print
"Waiting for the mission to start ",
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print
        "Error:", error.text

print
print
"Mission running ",

# Loop until mission ends:
while world_state.is_mission_running:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print
        "Error:", error.text

print
print
"Mission ended"
# Mission has ended.
