#! /usr/bin/env python3

import os
import requests
import json

path = "Project2/data/feedback/"

dict = {"title": "",
        "name": "",
        "date": "",
        "feedback": ""
        }

files = os.listdir(path)
for file in files:
    with open(path + file) as fl:
        file_content = fl.readlines()
        # for line in file_content:
        #     print(line[0].strip("\n"))
        dict["title"] = file_content[0].strip("\n")
        dict["name"] = file_content[1].strip("\n")
        dict["date"] = file_content[2].strip("\n")
        dict["feedback"] = file_content[3].strip("\n")
        #print(dict)
    post_request = requests.post("http://httpbin.org/post", json=dict)
print(post_request.request.body)
print(post_request.status_code)
