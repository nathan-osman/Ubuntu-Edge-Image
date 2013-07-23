#!/usr/bin/env python

from json import dumps
from lxml import html
from os import path
from re import match
from time import sleep
from urllib2 import urlopen

from PIL import Image, ImageDraw, ImageFont

def retrieve_percentage():
    '''
    Retrieves the latest value as a percentage.
    Throws all manner of exceptions due to network problems,
    HTML parsing errors, invalid list indices, etc.
    '''
    page = urlopen('http://www.indiegogo.com/projects/ubuntu-edge').read()
    element = html.fromstring(page).find_class('progress')[0]
    progress = float(match(r'[\d.]+', element.text).group(0))
    return '%.f%%' % (progress * 100)

def generate_image(directory):
    '''
    Generates a PNG image displaying the provided percentage.
    The image combines the background design and bright green text.
    '''
    img = Image.open('bg.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Ubuntu-B.ttf', 30)
    percentage = retrieve_percentage()
    size = draw.textsize(percentage, font=font)
    draw.text((50 - size[0] / 2, 40 - size[1] / 2), percentage,
              fill=(0, 192, 0,), font=font)
    img.save(path.join(directory, 'percentage.png'), 'PNG')

# Note that exceptions are NOT handled here
if __name__ == '__main__':
    generate_image('.')