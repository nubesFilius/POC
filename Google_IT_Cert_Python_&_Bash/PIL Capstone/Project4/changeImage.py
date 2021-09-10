#!/usr/bin/env python3

from PIL import Image
import os, subprocess

# TODO modify images and save then in a specific folder

path = "/Users/ernie_py/Documents/googleit/PIL Capstone/Project4/supplier-data/images/"

# Iterate through each image
def image_processing():
    list_of_images = []
    for file in os.listdir(path):

        # Open each image, convert RBGA to RGB, resize to 600x400, change format to JPEG
        if file.endswith(".tiff"):
            new_path = '{}.jpeg'.format(path)
            with Image.open(path + file) as im:
                im.convert("RGB").resize((600, 400))
                im.save(new_path, "JPEG")
        else:
            continue

image_processing()
