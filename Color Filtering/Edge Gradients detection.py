import cv2
import numpy as np

tShirt = cv2.imread('foto.jpg')
scale_percent = 30
width= int(tShirt.shape[1] * scale_percent/100)
height= int(tShirt.shape[0] * scale_percent/100)
dim= (width,height)
tShirt2 = cv2.resize(tShirt, dim , interpolation = cv2.INTER_AREA)

laplacian = cv2.Laplacian(tShirt2, cv2.CV_64F)
soblex = cv2.Sobel(tShirt2, cv2.CV_64F, 1, 0, ksize=5)
soblex2 = cv2.Sobel(tShirt2, cv2.CV_64F, 0, 1, ksize=5)
edges = cv2.Canny(tShirt2, 100, 200)


cv2.imshow('laplacian', laplacian)
cv2.imshow('tShirt2', tShirt2)
cv2.imshow('soblex', soblex)
cv2.imshow('soblex2', soblex2)
cv2.imshow('edges', edges)
