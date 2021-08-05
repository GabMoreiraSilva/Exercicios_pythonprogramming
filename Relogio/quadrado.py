import cv2
import matplotlib.pyplot as plt

img = cv2.imread('woman.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('woman.jpg',cv2.IMREAD_COLOR)

scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
resized2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.line(resized, (0,0), (180,230), (255,255,255), 15)
cv2.rectangle(resized, (150,190), (220,270), (0,255,0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(resized, 'Relogio', (155,290), font, 0.5, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',resized)
cv2.imshow('image2',resized2)
cv2.waitKey(0)
cv2.destroyAllWindows()
