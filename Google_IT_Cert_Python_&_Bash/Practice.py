#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib, ssl
import getpass

message = EmailMessage()
sender = "me@example.com"
recipient = "youw@example.com"


message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there!

I'm learning to send emails using Python!"""

message.set_content(body)


mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)

#mail_server.set_debuglevel(1)

#print(mail_pass)
#print(message)
