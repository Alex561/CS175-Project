# from skimage import data
# cat = data.chelsea()
# print(type(cat))
# print(cat[10,20])
# # camera = data.camera()
# # print(camera.size)

import os
import skimage
# filename = os.path.join('GORRILA.jpg')
from skimage import io
gorilla = io.imread('C:\\Users\\Edwin\\Pictures\\SELFIES\\Us Beach.jpg')

print(gorilla.shape)
print(gorilla[390, 920])
