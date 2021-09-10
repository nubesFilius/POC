#!/usr/bin/env python3

import re, sys, os, csv

# Exercise 2:

# You do not have access to the database but you have access to the log file for today's activity. You must do the following:

# - Get a list of all the newly registered users and gather the following:
# 	- first and last name
# 	- email
# 	- phone number

# Some users have submitted and additional information document that saved in the following path for each user "public/uploads/[username]". In each user folder you will find a document named "additional_info.txt". That document contains other phone numbers, secondary emails and people they think should join the Team.

# - Go to each users additional info document and add their secondary emails and phones to the list you are making above:

# - Additionally, gather the information from people they are referring and make a separate list to use later.

# - For each newly registered user. You will find a welcome sms template and a welcome email template that you can use to send them welcome messages.

# - If the SMS fails to send, send them an email with the same message from the sms.

# - Finally for each Referral from the registered user's "additional_info.txt", create a template sms template named "referral_template.txt" and craft a message to send in order to invite them to the program.

pattern = "firstname\", \"([A-Za-z]*)\".*lastname\", \"([A-Za-z]*)\".*\"(\w+@\w+\.\w+)\".*\"(\d{3}-\d{3}-\d{4})\""

users = []

user_info = {"firstname": [], "last_name": [], "email": [], "phone_number": [], "secondary_email": []}

referred_people = []


with open("activity_log.txt") as file:
    loglines = file.readlines()
    for line in loglines:
        result = re.search(r'\[.*firstname\", \"([A-Za-z]*)\".*lastname\", \"([A-Za-z]*)\".*\"(\w+@\w+\.\w+)\".*\"(\d{3}-\d{3}-\d{4})\"', line)
        if result != None:
            #print(result.group(1), result.group(2), result.group(3), result.group(4) )
            user_info["firstname"].append(result.group(1))
            user_info["last_name"].append(result.group(2))
            user_info["email"].append(result.group(3))
            user_info["phone_number"].append(result.group(4))
        







