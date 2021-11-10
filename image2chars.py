# Given an image, return a grayscale version of it using characters.

from PIL import Image
import numpy as np
import math
import cv2

def main():
    # Constants:
    # Input image constants:
    IMAGE_NAME = "arnold_avedon.jpg"
    PATH2IMG = "imgs/"
    FULL_PATH2IMG = PATH2IMG + IMAGE_NAME
    WIDTH_DOWNSIZED = 200

    # Output image constants:
    WIDTH_OUTPUT_IMG = 1500
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    FONTSCALE = 0.4   
    COLOR = (0, 0, 0) # BGR
    THICKNESS = 1
    DELTA = 8

    # Char dict: 
    CHARS = {
    0:'@*',
    1:'#',
    2:'%',
    3:'&',
    4:'$',
    5:'/',
    6:';',
    7:',',
    8:'.',
    9:' '}

    # Get the image to convert to characters:
    img = Image.open(FULL_PATH2IMG).convert('L')
    img_width = img.size[0]
    img_height = img.size[1]
    img_aspect_ratio = img_height/img_width

    # Parameters of the resulting image:
    width = WIDTH_OUTPUT_IMG
    height = int(width/img_aspect_ratio)

    # Downsize the image:
    img = img.resize((WIDTH_DOWNSIZED, int(WIDTH_DOWNSIZED*img_aspect_ratio)))
    img_width = img.size[0]
    img_height = img.size[1]

    # Create a .txt file to contain the image as characters
    file_chars = open("arnold.txt","w")

    # Create a blank image which will contain the characters:
    img2 = 255*np.ones((width, height,1), dtype=np.uint8)

    character = ''
    org = (0,0)
    for i in range(img_width):
        for j in range(img_height):
            coordinates = (i,j)
            value = img.getpixel(coordinates)
            org = (i*DELTA,j*DELTA)
            dict_key = math.floor((len(CHARS)-1)*value/255)
            character = CHARS[dict_key]
            file_chars.write(character)
            img2 = cv2.putText(img2, character, org, FONT, FONTSCALE, COLOR, THICKNESS, cv2.LINE_AA)
        
        file_chars.write('\n')

    # Save the image
    name, extension = FULL_PATH2IMG.split(".")
    cv2.imwrite(name + "_ascii." + extension, img2) 

if __name__ == "__main__":
    main()