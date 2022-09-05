import twilio
from twilio.rest import Client 
# from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Message, MessagingResponse
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 


def send_msg(to_num, frm_num, txt):
    ccount_sid = '' 
    auth_token = '' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(to = to_num,
                                from_= frm_num,
                                body = txt) 


def chat():
    # messages = client.messages.list(limit=20)
    exit = False 
    while (not exit):
        exit = True 

"""
Pass text as "info" to send notifications
"""
def send_notif(info):
    ccount_sid = '' 
    auth_token = '' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(to='',
                                from_="",
                                body=info) 
    print(message.sid)