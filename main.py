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
# for macOS
valid_images = []
for filename in images:
    if filename != '.DS_Store' :
        valid_images.append(filename)
print(valid_images)
image_obj = [cv2.imread(f'images/{filename}') for filename in valid_images]

# all images to be same size
shape = cv2.imread('images/img1.JPG').shape


# (3648, 5472, 3)
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

background.fill(255) # change to white


# add images ontop of the background

positions = [(x, y) for x in range(columns) for y in range(rows)]
print(positions)


# each image gets a position in the list
for (pos_x, pos_y), image in zip(positions, image_obj):
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin
    background[y:y+shape[0], x:x+shape[1]] = image


cv2.imwrite('grid.JPG', background)
