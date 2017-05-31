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
import sys
import time

import colors
from skimage import io
from sklearn import *
import cv2

difList = []

def main(imageString, imageHeight, imageWidth):
    difList = []

    image = cv2.imread(imageString)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.rot90(image, k=2)

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # depth_map = cv2.distanceTransform(gray_image, cv2.cv.CV_DIST_L2, cv2.cv.CV_DIST_MASK_PRECISE)
    # depth_map = cv2.distanceTransform(gray_image, cv2.cv.CV_DIST_L1, 3)
    depth_map = cv2.distanceTransform(gray_image, cv2.cv.CV_DIST_C, 5)

    depth_map = preprocessing.scale(depth_map)

    image = cv2.resize(image, (imageWidth, imageHeight))
    depth_map = cv2.resize(depth_map, (imageWidth, imageHeight))

    print(depth_map.min())
    print(depth_map.max())
    print(depth_map.mean())
    print(depth_map)

    import matplotlib.pyplot as plt
    plt.imshow(np.rot90(image, k=-2))
    plt.imshow(np.rot90(depth_map, k=-2))
    plt.show()

    missionXML = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                  <About>
                    <Summary>Hello world!</Summary>
                  </About>

                  <ServerSection>
                    <ServerHandlers>
                      <FlatWorldGenerator generatorString="3;7,0,5*3,2;3;,biome_1" forceReset="true"/>
                      <DrawingDecorator>
                        ''' + picturefy(image, depth_map, colors.colorDict) + '''
                      </DrawingDecorator>
                      <ServerQuitFromTimeUp timeLimitMs="1000"/>
                      <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                  </ServerSection>

                  <AgentSection mode="Creative">
                    <Name>SketchyAI</Name>
                    <AgentStart>
                        ''' + '<Placement x="{0}" y="{1}" z="{2}" yaw="0"/>'.format(imageWidth/2, imageHeight/2, -imageHeight * .75) + '''
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
        print 'ERROR:', e
        print
        agent_host.getUsage()
        exit(1)
    if agent_host.receivedArgument("help"):
        print
        agent_host.getUsage()
        exit(0)

    my_mission = MalmoPython.MissionSpec(missionXML, True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission.setModeToSpectator()

    # Attempt to start a mission:
    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission(my_mission, my_mission_record)
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print "Error starting mission:", e
                exit(1)
            else:
                time.sleep(2)

    # Loop until mission starts:
    print "Waiting for the mission to start ",
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:", error.text

    print
    print "Mission running ",

    # Loop until mission ends:
    while world_state.is_mission_running:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:", error.text

    print
    print "Mission ended"
    # Mission has ended.

def QuantitiveEval(difList):
    sum=0
    for i in range(len(difList)):
        sum+=difList[i]
    return sum/len(difList)

def closestColor(pixel, colorDict):
    resultColor = "WHITE"
    minDif = float("inf")
    for wool, colorValue in colorDict.items():
        dif = np.sqrt((pixel[0]-colorValue[0])**2 + (pixel[1]-colorValue[1])**2 + (pixel[2]-colorValue[2])**2)
        if (dif < minDif):
            resultColor = wool
            minDif = dif

    difList.append(minDif)
    return resultColor

def picturefy(pixelArray, depth_map, colorDict):
    returnString = ""
    isAlpha = False
    if (pixelArray.shape[2] == 4):
        isAlpha = True

    depthRange = depth_map.max() - depth_map.min()

    xCount = 0
    yCount = 0
    layerCount = 10
    zScale = 3

    for x in range(pixelArray.shape[1]):
        xCount += 1

        for y in range(pixelArray.shape[0]):
            yCount += 1

            pixelColor = pixelArray[y][x]
            depth = depth_map[y][x]

            if (isAlpha):
                pixelColor = round(pixelColor[0]), round(pixelColor[1]), round(pixelColor[2]), round(pixelColor[3])
            else:
                pixelColor = round(pixelColor[0]), round(pixelColor[1]), round(pixelColor[2])

            if (isAlpha and pixelArray[y][x][3] > 0) or (not isAlpha):
                bestColor = closestColor(pixelColor, colorDict)
                zValue = int(round((depth - depth_map.min()) / (depthRange) * layerCount)) * zScale
                if bestColor in colors.woolList:
                    returnString += '<DrawBlock x="{0}" y="{1}" z="{2}" type="wool" colour="{3}"/>\n'.format(x, y+7, zValue, bestColor)
                else:
                    returnString += '<DrawBlock x="{0}" y="{1}" z="{2}" type="{3}"/>\n'.format(x, y+7, zValue, bestColor)

    #Draw gray background
    for x in range(-50, pixelArray.shape[1] + 50):
        for y in range(pixelArray.shape[0] + 10):
            returnString += '<DrawBlock x="{0}" y="{1}" z="{2}" type="wool" colour="GRAY"/>\n'.format(x, y + 7, 10 * zScale)

    print("({0}, {1}) pixels".format(xCount, yCount/xCount))
    print(QuantitiveEval(difList))
    return returnString

#get resolution button
def getResolution():
    imageString = userInputP.get()
    image = io.imread(imageString)
    resolutionLabel=Label(root,text="Resolution: "+ str("{0}x{1}".format(image.shape[1], image.shape[0])))
    resolutionLabel.pack()
    resolutionLabel.place(x=150,y=60)

#drawPciture button
def drawPicture():
    imageString = userInputP.get()
    imageHeight = int(userInputH.get())
    imageWidth = int(userInputW.get())

    main(imageString, imageHeight, imageWidth)

#initilize gui
root = Tk()
frame = Frame(root, width=300, height=300)
frame.pack()

userInputP = StringVar()#picture box
pictureLabel=Label(root,text="Picture File")
pictureLabel.place(x=20,y=20)
picture = Entry(root, text="Black", fg="black",textvariable=userInputP)
picture.place(x=90,y=20)

getResolution= Button(root, text ="Get Resolution", command = getResolution)#resolution button
getResolution.pack()
getResolution.place(x=30,y=60)

userInputW = StringVar()#width
widthLabel=Label(root,text="Width")
widthLabel.place(x=20,y=100)
width = Entry(root, text="Black", fg="black",textvariable=userInputW)
width.place(x=60,y=100)

userInputH = StringVar()#Height Stuff
heightLabel=Label(root,text="Height")
heightLabel.pack()
heightLabel.place(x=20,y=150)
height = Entry(root, text="Black", fg="black",textvariable=userInputH)
height.place(x=60,y=150)

drawPicture = Button(root, text ="Draw picture", command = drawPicture)#draw button
drawPicture.pack()
drawPicture.place(x=75,y=200)

root.mainloop()#drawn