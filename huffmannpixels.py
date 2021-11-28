img_file = "Images/output2.png"
# from matplotlib import image
# from matplotlib import pyplot
# # load image as pixel array
# image = image.imread(img_file)
# # summarize shape of the pixel array
# print(image.dtype)
# print(image.shape)
# # display the array of pixels as an image
# pyplot.imshow(image)
# pyplot.show()
#
# from PIL import Image
# from numpy import asarray
# # load the image
# image = Image.open(img_file)
# # convert image to numpy array
# data = asarray(image)
# print(type(data))
# # summarize shape
# print(data.shape)
#
# # create Pillow image
# image2 = Image.fromarray(data)
# print(type(image2))
#
# # summarize image details
# print(image2.mode)
# print(image2.size)
# print(data)

import numpy as np
import cv2
im = cv2.imread(img_file)
a = np.asarray(im)
print(a)