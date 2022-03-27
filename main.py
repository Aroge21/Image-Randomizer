from PIL import Image
import numpy as np
import random
import math

width = 400
height = 300
number = 0

pixels = []

red = 0
green = 0
blue = 0

try:
    with open('img_num.txt') as docNum:
        number = int(docNum.read())
except:
    with open('img_num.txt', 'w') as docNum:
        docNum.write(str(number))

while 1:
    pixels = []
    counter = 0

    for x in range(height):
        counter = 0
        temp = []

        while counter < width:
            red = random.randint(0, 256)
            green = random.randint(0, 256)
            blue = random.randint(0, 256)

            rgb = [red, green, blue]

            temp.append(rgb)
            counter += 1
        
        pixels.append(temp)
    
    ##print(pixels)

    array = np.array(pixels, dtype=np.uint8)

    new_img = Image.fromarray(array)
    ##new_img.show()
    new_img.save(f'image/new_image{number}.bmp')

    number += 1

    with open('img_num.txt', 'w') as docNum:
        docNum.write(str(number))


