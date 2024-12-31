import cv2
import os
import numpy as np

# rows and columns for collage
columns = 3
rows = 2

# spacing inbetween each image and on the border 
horizontal_margin = 40
vertical_margin = 20

# image path 
images = os.listdir('images')

# all images to be same size
shape = cv2.imread('images/img1.JPG').shape

# background using numpy

# shape[0] * rows accounts for for the vertical size of only the images
# 2 rows -> 3 horizontal margins
# 3 rows -> 4 horizontal margins 

# shape[1] * columns accounts for the horizontal display of only the images
# 3 rows -> 4 vertical margins
# 4 rows -> 5 margins 
background = np.zeros((shape[0]  * rows + horizontal_margin * (rows + 1), 
                       shape[1] * columns + vertical_margin * (columns + 1), 
                       shape[2]), 
                       np.uint8)

background.fill(255)

cv2.imwrite('grid.JPG', background)