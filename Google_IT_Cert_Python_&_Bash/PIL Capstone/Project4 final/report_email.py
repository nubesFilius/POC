#!/usr/bin/env python3

import reports
import emails
import os, sys
from datetime import datetime

path_to_description = "supplier-data/descriptions/"

fruit_list = []
files = os.listdir(path_to_description)

for file in files:
    fruit_dict = {}
    with open(path_to_description + file) as fl:
        file_content = fl.readlines()
        #print(file_content)
        fruit_dict["name"] = file_content[0].strip("\n")
        fruit_dict["weight"] = file_content[1].strip("\n")
        fruit_list.append(fruit_dict)

#print(fruit_list)

additional_info = ""
pdf_title = "Processed Update on " + datetime.today().strftime('%B %d, %Y') + "\n"
pdf_attachment = "/tmp/processed.pdf"
for fruit in fruit_list:
    fruit_info = "name:{}<br/>weight:{}<br/><br/>".format(fruit["name"], fruit["weight"])
    additional_info += fruit_info

#print(additional_info)

def main(argv):

  # Geenrate the pdf
  title = pdf_title
  attachment = pdf_attachment
  reports.generate_report(attachment, title, additional_info)

  # Send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student-04-9afd3649569b@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = pdf_attachment
  message = emails.generate(sender, receiver, subject, body, attachment)
  emails.send(message)

if __name__ == "__main__":
    main(sys.argv)
