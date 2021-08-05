import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('woman.jpg',cv2.IMREAD_COLOR)

scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('image',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
