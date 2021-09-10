import time
import datetime
import random

def send_text(message, phone):
  ra = random.randint(1291, 5000)
  current_time = datetime.datetime.now()
  print( "Processing Outbound SMS." )
  print( "tel:", phone )
  print( "sms:", message )
  print( "sent at:", current_time )
  time.sleep(2)
  if "111" in phone or "555" in phone:
    return f"{current_time} pid[{ra}]: message:SMS failed to send to {phone}. status:failed"
  else:
    return f"{current_time} pid[{ra}]: message:SMS sucessfully sent to {phone}. status:success"

def send_email(sender, email, message):
  ra = random.randint(1291, 5000)
  current_time = datetime.datetime.now()
  print( "Processing Outbound Message." )
  print( "message:", message )
  print( "sent at:", current_time )
  time.sleep(2)
  return f"{current_time} pid[{ra}]: message:Email sucessfully sent to {email}. status:success"

