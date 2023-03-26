import cv2
import numpy as np

# load the image
img = cv2.imread('95035378.jpg')

# convert the image to HSI color space
hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL)

# convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# convert the image to HSL color space
hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# display the images
cv2.imshow('Original image', img)
cv2.imshow('HSI Image', hsi)
cv2.imshow('HSV Image', hsv)
cv2.imshow('HSL Image', hsl)

cv2.waitKey(0)
cv2.destroyAllWindows()
