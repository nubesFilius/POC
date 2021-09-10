#! /usr/bin/env python3

import os
import requests
import json

path_to_description = "/Users/ernie_py/Documents/googleit/PIL Capstone/Project4/supplier-data/descriptions/"

fruit_dict = {"name": "",
        "weight": "",
        "description": "",
        "image_name": ""
        }

files = os.listdir(path_to_description)
for file in files:
    with open(path_to_description + file) as fl:
        file_content = fl.readlines()
    #print(file_content)
        fruit_dict["name"] = file_content[0].strip("\n")
        fruit_dict["weight"] = int(file_content[1].strip("\n").split()[0])
        fruit_dict["description"] = file_content[2].strip("\n")
        filename = os.path.splitext(file)[0]
        fruit_dict["image_name"] = filename + ".jpeg"
    #print(fruit_dict)
        post_request = requests.post("http://httpbin.org/post", json=fruit_dict)
#print(post_request.request.body)
#print(post_request.status_code)
