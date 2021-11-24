import cv2
import numpy as np

tShirt = cv2.imread('foto.jpg')
scale_percent = 30
width= int(tShirt.shape[1] * scale_percent/100)
height= int(tShirt.shape[0] * scale_percent/100)
dim= (width,height)
tShirt2 = cv2.resize(tShirt, dim , interpolation = cv2.INTER_AREA)


hsv = cv2.cvtColor(tShirt2, cv2.COLOR_BGR2HSV)

# hsv hue sat value
lower_red = np.array([135,100,25])
upper_red = np.array([255,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(tShirt2, tShirt2, mask = mask)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(mask, kernel, iterations = 1)
dilation = cv2.dilate(mask, kernel, iterations = 1)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


cv2.imshow('tShirt2', tShirt2)
cv2.imshow('res', res)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.imshow('closing', closing)
cv2.imshow('opening', opening)

'''
kernel = np.ones((15,15), np.float32)/255
smoothed = cv2.filter2D(res, -1, kernel)

blur = cv2.GaussianBlur(res, (15,15), 0)
median = cv2.medianBlur(res,15)
bilateral = cv2. bilateralFilter(res, 15, 75, 75)


cv2.imshow('tShirt2', tShirt2)
#cv2.imshow('mask', mask)
cv2.imshow('res', res)
#cv2.imshow('smoothed', smoothed)
cv2.imshow('blur', blur)
cv2.imshow('median',median)
cv2.imshow('bilateral', bilateral)
'''
