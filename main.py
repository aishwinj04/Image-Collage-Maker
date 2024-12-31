import cv2
import os
import numpy as np


def grid_preferences():
    # rows and columns for collage
    rows = int(input('Enter rows: '))
    columns = int(input('Enter columns: '))

    # spacing inbetween each image and on the border 
    horizontal_margin = int(input('Enter horizontal margin: '))
    vertical_margin = int(input('Enter vertical margin: '))

    return rows, columns, horizontal_margin, vertical_margin

def image_validate():
        
    # image path 
    images = os.listdir('images')

    # for macOS
    valid_images = []
    for filename in images:
        if filename != '.DS_Store' :
            valid_images.append(filename)

    # all images to be same size
    shape = cv2.imread('images/img1.JPG').shape
    image_obj = []
    for filename in valid_images:
        image = cv2.imread(f'images/{filename}')
        # resize function wants in form (width, height)
        resized_image = cv2.resize(image, (shape[1], shape[0]))
        image_obj.append(resized_image)

    return image_obj

def generate_collage(rows, columns, horizontal_margin, vertical_margin):
    img_list = image_validate()
    shape = img_list[0].shape # all images have same shape

    # shape[0] * rows accounts for for the vertical size of images
    # 2 row -> 3 horizontal margins between each row 
    # 3 rows -> 4 horizontal margins 

    # shape[1] * columns accounts for the horizontal display of images
    # 3 columns -> 4 vertical margins
    # 4 columns -> 5 vertical margins 
    background = np.zeros((shape[0]  * rows + horizontal_margin * (rows + 1), 
                        shape[1] * columns + vertical_margin * (columns + 1), 
                        shape[2]), 
                        np.uint8)

    background.fill(255) # change to white

    # add images ontop of the background
    positions = [(x, y) for x in range(columns) for y in range(rows)]
    #print(positions)

    # each image gets a position in the list
    for (pos_x, pos_y), image in zip(positions, img_list):
        x = pos_x * (shape[1] + vertical_margin) + vertical_margin
        y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin
        background[y:y+shape[0], x:x+shape[1]] = image


    return background



def main():
    
    rows, columns, horizontal_margin, vertical_margin = grid_preferences()
    collage = generate_collage(rows, columns,horizontal_margin, vertical_margin)

    cv2.imwrite('grid.JPG', collage)
    print("Success!")


if __name__ == '__main__':
    main()