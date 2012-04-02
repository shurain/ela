#!/usr/bin/env python

from PIL import Image


ORIG = './books-edited.jpg'
TEMP = 'temp.jpg'
SCALE = 15


def ELA():
    original = Image.open(ORIG)
    original.save(TEMP, quality=70)
    temporary = Image.open(TEMP)

    WIDTH, HEIGHT = original.size
    i1 = original.load()
    i2 = temporary.load()

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            r, g, b = [abs(color[0] - color[1]) * SCALE for color in zip(i1[x, y], i2[x, y])]
            i2[x, y] = (r, g, b)

    temporary.show()

if __name__ == '__main__':
    ELA()
