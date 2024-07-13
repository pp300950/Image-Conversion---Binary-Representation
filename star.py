import cv2
import numpy as np

#อ่านภาพเข้ามา
image = cv2.imread('mypic4.webp')

height, width = image.shape[:2]
crop_height = min(height, width)
crop_width = crop_height  
start_height = (height - crop_height) // 2
start_width = (width - crop_width) // 2
cropped_image = image[start_height:start_height + crop_height, start_width:start_width + crop_width]

gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
resized_image = cv2.resize(binary_image, (64, 64))
binary_array = (resized_image > 127).astype(int)

for row in binary_array:
    line = ''.join('*' if pixel == 1 else ' ' for pixel in row)
    print(line)
