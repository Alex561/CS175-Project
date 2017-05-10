# from skimage import data
# cat = data.chelsea()
# print(type(cat))
# print(cat[10,20])
# # camera = data.camera()
# # print(camera.size)

# filename = os.path.join('GORRILA.jpg')
from skimage import io
gorilla = io.imread("GORILLA.jpg")
print(gorilla.shape)
print(gorilla[714, 1279])
