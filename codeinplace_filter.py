"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
RED_FILTER = 1.5
BLUE_FILTER = 1.5
GREEN_FILTER = .7

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()
    for pixel in image:
    # Apply the filter
        pixel.red *= RED_FILTER
        pixel.green *= GREEN_FILTER
        pixel.blue *= BLUE_FILTER
    # Show the image after the transform
    image.show()
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()