import os
import random
from PIL import Image

# Learning image color manipulation with python.
# This is a very basic knowledge.

def pixel_value(pixels):
    return sum(pixels) // len(pixels)

def picture_off(colors: tuple):
    # Establish colors list and assign them to the RGB values
    # Function just assigns a random number and subtracts it.
    c_list = []
    for key, val in enumerate(colors):
        c_list.append(random.randrange(255) - val)
    
    r,g,b = c_list[0], c_list[1], c_list[2]
    return (r,g,b)


def sepia(colors: tuple):
    csepia = []
    for key, val in enumerate(colors):
        csepia.append(val)
    # tr, tg, and tb take the ratios based on the sepia color
    # although I think it just turns it into the respective "brown" color-type
    tr = (0.393 * csepia[0]) + (0.769 * csepia[1]) + (0.189 * csepia[2])
    tg = (0.349 * csepia[0]) + (0.686 * csepia[1]) + (0.168 * csepia[2])
    tb = (0.272 * csepia[0]) + (0.534 * csepia[1]) + (0.131 * csepia[2])

    if tr > 255:
        sr = 255
    else:
        sr = round(tr)
    if tg > 255:
        sg = 255
    else:
        sg = round(tg)
    if tb > 255:
        sb = 255
    else:
        sb = round(tb)

    return (sr,sg,sb)


def black_and_white(colors: tuple):
    # grayscale is based on the average of the RGB values.
    grayscale = []
    for key, val in enumerate(colors):
        grayscale.append(val // 3)
      
    r = sum(grayscale)
    g = sum(grayscale)
    b = sum(grayscale)

    return (r,g,b)


def inverse(colors: tuple):
    # Inverse is based on what the opposite color value is.
    # So subtracting the value from the color max (255),
    # we can find the inverse value.
    c_inverse = []
    for key, val in enumerate(colors):
        c_inverse.append(255-val)
    
    r,g,b = c_inverse[0], c_inverse[1], c_inverse[2]

    return (r,g,b)


if __name__ == "__main__":
    os.chdir('C:\\Users\\Brayd\\Downloads')
    image_pic = Image.open('cat.jpg')
    image_load = image_pic.load()
    print(image_pic.size)
    pic_x = image_pic.size[0]
    pic_y = image_pic.size[1]

    pixel_list = []

    for x in range(pic_x):
        for y in range(pic_y):
            pixel_list.append(pixel_value(image_load[x, y]))
            image_load[x, y] = picture_off(image_load[x,y])

    image_pic.save('off_cat.png')