from PIL import Image
import numpy as np
import random
import math

# Sets size of screen
width = 400
height = 300
number = 0

pixels = []

# Initates colors for each varible
red = 0
green = 0
blue = 0

# Makes a txt file to label new pictures correctly
try:
    with open('img_num.txt') as docNum:
        number = int(docNum.read())
except:
    with open('img_num.txt', 'w') as docNum:
        docNum.write(str(number))

# Goes through every pixel in a 2D array
while 1:
    pixels = []
    counter = 0

    for x in range(height):
        counter = 0
        temp = []

        while counter < width:
            # Makes random colors for each pixel in screen size of array
            red = random.randint(0, 256)
            green = random.randint(0, 256)
            blue = random.randint(0, 256)

            #Sets random colored varibles into rgb array
            rgb = [red, green, blue]

            temp.append(rgb)
            counter += 1
        
        pixels.append(temp)

    # Sets the 2D array of of all random pixels
    array = np.array(pixels, dtype=np.uint8)

    # Makes image from 2D array
    new_img = Image.fromarray(array)

    # Saves images to whatevery folder you want
    new_img.save(f'image/new_image{number}.bmp')

    number += 1

    with open('img_num.txt', 'w') as docNum:
        docNum.write(str(number))
