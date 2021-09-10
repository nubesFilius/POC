#!/usr/bin/env python3

import requests, os

#TODO send the images to [linux-instance-IP-Address]/upload using requests

url = "http://httpbin.org/post"
path = "/Users/ernie_py/Documents/googleit/PIL Capstone/Project4/supplier-data/images/"

for file in os.listdir(path):
    if file.endswith(".jpeg"):
        with open(path + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r.status_code)
    else:
        continue
