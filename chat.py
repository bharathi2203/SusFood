import twilio
from twilio.rest import Client 
 
account_sid = 'AC782659c3529185072669b6c67b52b87e' 
auth_token = '95ba2728eca91ec41938256f6a9fe372' 
client = Client(account_sid, auth_token) 


def chat():
    exit = False 
    while (not exit):
        exit = True 

"""
Pass text as "info" to send notifications
"""
def send_notif(info):
    message = client.messages.create(to='+16108648893',
                                from_="+19795593613",
                                body=info) 
    print(message.sid)