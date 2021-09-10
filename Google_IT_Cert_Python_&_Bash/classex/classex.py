#!/usr/bin/env python

import re, sys, os, csv, communicate

user_pattern = "user:(\w+) .*[FAILED]"

users = []
users_emails = []
# with open(sys.argv[1] ) as file:
#     logfile = file.readlines()
#     for line in logfile:
#         result = re.search(user_pattern, line)
#         if result != None:
#             #print(result.group(1))

with open("users.csv") as file:
    user_file = csv.DictReader(file)
    for line in user_file:
        print(line)
