import cv2
import os

# rows and columns for collage
columns = 3
rows = 2

# spacing inbetween each image and on the border 
horizontal_margin = 40
vertical_margin = 20

# image path 
images = os.listdir('images')

# all images to be same size
img1 = cv2.imread('images/img1.JPG')

# .shape uses order of height then width 
width = img1.shape[1] 
height = img1.shape[0]
