#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import datetime
from json import dumps
from os import path
from re import match
from time import sleep
from urllib2 import urlopen

from lxml import html
from PIL import Image, ImageDraw, ImageFont

class ImageUpdater:
    '''
    Updates the image displaying percentage of completion.
    '''

    def retrieve_percentage(self):
        '''
        Retrieves the latest value as a percentage.
        Throws all manner of exceptions due to network problems,
        HTML parsing errors, invalid list indices, etc.
        '''
        page = urlopen('http://www.indiegogo.com/projects/ubuntu-edge').read()
        element = html.fromstring(page).find_class('progress')[0]
        progress = float(match(r'[\d.]+', element.text).group(0))
        return '%.f%%' % (progress * 100)

    def generate_image(self, directory):
        '''
        Generates a PNG image displaying the provided percentage.
        The image combines the background design and bright green text.
        '''
        img = Image.open('bg.png')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('Ubuntu-B.ttf', 30)
        percentage = self.retrieve_percentage()
        size = draw.textsize(percentage, font=font)
        draw.text((50 - size[0] / 2, 40 - size[1] / 2), percentage,
                fill=(0, 192, 0,), font=font)
        img.save(path.join(directory, 'percentage.png'), 'PNG')
    
    def run(self, args):
        '''
        Runs the application according to the interval argument.
        '''
        while True:
            try:
                self.generate_image(args.directory)
                print '[%s] image updated' % datetime.now()
            except Exception, e:
                print e
            if not args.interval:
                break
            sleep(60 * args.interval)

if __name__ == '__main__':
    parser = ArgumentParser(description='Updates percentage image')
    parser.add_argument('--directory',
                        type=str,
                        default='.',
                        help='directory to create the image in')
    parser.add_argument('--interval',
                        metavar='MINUTES',
                        type=int,
                        default=0,
                        help='number of minutes between updates (0 to run once)')
    ImageUpdater().run(parser.parse_args())