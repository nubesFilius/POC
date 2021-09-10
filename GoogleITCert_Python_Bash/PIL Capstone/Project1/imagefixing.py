#!/usr/bin/env python3

from PIL import Image
import os, subprocess

# Iterate through each file in the folder
path = "/Users/ernie_py/Documents/googleit/images/"

def image_processing():
    list_of_images = []
    for file in os.listdir(path):
    #return list_of_images
    #print( list_of_images)

# For each file:
    # Rotate the image 90° clockwise
    # Resize the image from 192x192 to 128x128
    # Save the image to a new folder in .jpeg format
    # im = Image.open(folder)
    # im.rotate(90).show()
        with Image.open(path + file) as im:
            im.convert("RGB").rotate(270).resize((128, 128)).save(file + ".jpeg")
            new_image_name = file + ".jpeg"
            subprocess.call(["mv", new_image_name, "opt/icons/"])

image_processing()
