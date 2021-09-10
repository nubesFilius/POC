#! /usr/bin/env python3

import os
import requests
import json

path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

files = os.listdir(path)
for file in files:
    key_index = 0
    dict = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            dict[keys[key_index]] = value
            key_index += 1
    post_request = requests.post("http://35.192.174.218/feedback/", json=dict)
print(post_request.request.body)
print(post_request.status_code)
