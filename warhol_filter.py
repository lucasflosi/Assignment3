"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2 #must be greater than 1 .. I could have user input here
N_COLS = 2 #must be greater than 1.. I could have user input here
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
LOW_RANDOM_RANGE = 0
HIGH_RANDOM_RANGE = 199 #199 is selected because since we divide by 1 it results in 0 to 2X the value

#Various Patches below here. Could create a user input, but prefer to leave it hardcoded for now

#PATCH_NAME = 'images/luval4.jpg'
PATCH_NAME = 'images/simba-sq.jpg'
#PATCH_NAME = 'images/stanford.png'
#PATCH_NAME = 'images/Blue.jpg'

def main():
    patch = SimpleImage(PATCH_NAME)
    #imports an image, names it "patch"
    final_image = SimpleImage.blank((patch.width*N_COLS),(patch.height*N_ROWS))
    #generates blank canvas
    final_image = grid_of_patches(patch,final_image)
    #runs script that makes a grid of patches
    final_image.show()

#creates rows and columns of an image patch
def grid_of_patches(patch,final_image):
    for cols in range(N_COLS):
        for rows in range(N_ROWS):
            patch = random_recolored_patch()
            final_image = single_patch(final_image, patch, cols, rows)
    return final_image

#Used in <grid of patches> function above. Creates a single patch
def single_patch(final_image, patch, cols, rows):
    for y in range(patch.height):
        for x in range(patch.width):
            image_width = patch.width
            image_height = patch.height
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel(x + (cols * image_width), y + (rows * image_height), pixel)
    return final_image

#generates a randomly filtered image patch
def random_recolored_patch():
    patch = SimpleImage(PATCH_NAME)
    red_scale = (random.randint(LOW_RANDOM_RANGE, HIGH_RANDOM_RANGE) + random.randint(LOW_RANDOM_RANGE, HIGH_RANDOM_RANGE)) / 200
    blue_scale = (random.randint(LOW_RANDOM_RANGE, HIGH_RANDOM_RANGE) + random.randint(LOW_RANDOM_RANGE, HIGH_RANDOM_RANGE)) / 200
    green_scale = (random.randint(LOW_RANDOM_RANGE, HIGH_RANDOM_RANGE) + random.randint(LOW_RANDOM_RANGE, HIGH_RANDOM_RANGE)) / 200
    print("Pixel Modifiers: " + "R: " + str(red_scale)+ "B: "+ str(blue_scale)+ "G: " + str(green_scale))
    for pixel in patch:
        pixel.red *= red_scale
        pixel.blue *= blue_scale
        pixel.green *= green_scale
    return patch

if __name__ == '__main__':
    main()