#!/usr/bin/env python3

import os, sys, re, csv, operator

error_dict = {}
per_user = {}

with open(sys.argv[1]) as file:
    file_content = file.readlines()
    for line in file_content:

        error_counter = re.search( r"ticky: ERROR (\w+.*).*\((.*)\)", line)
        user_info = re.search( r"ticky: (INFO) .*\((.*)\)", line)
        user_error = re.search(r"ticky: (ERROR) .*\((.*)\)", line)

        if error_counter:
            error_dict[error_counter.group(1)] = error_dict.get(error_counter.group(1), 0) +1
            per_user.setdefault(user_error.group(2),[0,0])[1] +=1 

        if user_info:
            per_user.setdefault(user_info.group(2), [0,0])[0] += 1
 
    sorted_errors = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_users = sorted(per_user.items())
    sorted_errors.insert(0, ("Error","Count"))
    sorted_users.insert(0, ("Username", ["INFO","ERROR"]))

#print(sorted_users)
#print(sorted_errors)

with open("error_message.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    for error in sorted_errors:
        writer.writerow(error)
 
with open("user_statistics.csv", 'w') as csvfile:  
    writer = csv.writer(csvfile)
    for stat in sorted_users:
        row = [stat[0],stat[1][0],stat[1][1]]
        writer.writerow(row)