#!/usr/bin/env python3

import shutil, psutil
import socket, sys, emails

path = "/Users/ernie_py"

Error = ""

# TODO Report an error if CPU usage is over 80%
if psutil.cpu_percent(interval=None) > 80:
    Error = "Error - CPU usage is over 80%"

# TODO Report an error if available disk space is lower than 20%
#shutil.disk_usage()
total, used, free, percent = psutil.disk_usage(path)
if percent < 20.0:
    Error = "Error - Available disk space is less than 20%"

# TODO Report an error if available memory is less than 500MB
(total, available, percent, used, free, active, inactive, wired) = psutil.virtual_memory()
available_MB = available/(10**6)
if available_MB < 500:
    Error = "Error - Available memory is less than 500MB"

# TODO Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
localhost = socket.gethostbyname('localhost')
if localhost != "127.0.0.1":
    Error = "Error - localhost cannot be resolved to 127.0.0.1"

def main(argv):

  # Send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "username@example.com"
  subject = Error
  body = "Please check your system and resolve the issue as soon as possible."
  attachment = None
  message = emails.generate(sender, receiver, subject, body, attachment)
  emails.send(message)

if __name__ == "__main__":
    main(sys.argv)
