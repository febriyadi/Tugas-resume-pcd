import cv2
import numpy as np

# Load the image
img = cv2.imread('singa.jpg')

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the brightness and contrast values
brightness = 50
contrast = 1.5

# Apply the brightness and contrast adjustment
adjusted_img = np.int16(hsv_img)
adjusted_img[:, :, 2] = np.clip(adjusted_img[:, :, 2] * contrast + brightness, 0, 255)
adjusted_img = np.uint8(np.clip(adjusted_img, 0, 255))

# Convert the image back to BGR color space
result_img = cv2.cvtColor(adjusted_img, cv2.COLOR_HSV2BGR)

# Display the original and adjusted images
cv2.imshow('Original Image', img)
cv2.imshow('Adjusted Image', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
