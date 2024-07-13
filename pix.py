import cv2

image = cv2.imread('mypic2.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
resized_image = cv2.resize(binary_image, (128, 128))

cv2.imwrite('output_image.png', resized_image)
