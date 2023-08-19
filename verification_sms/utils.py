import os
from twilio.rest import Client

account_sid = 'ACcb15b4ee03ffc30cc9265c38acbd44d1'
auth_token = '494f913cf9f9f4f4fa52a906f70a001f'
client = Client(account_sid, auth_token)

def send_message(user_code, phone_number):
    message = client.messages \
                    .create(
                        from_='+16185684486',
                        body=f"Hi! Your user verification code is {user_code}",
                        to=f'{phone_number}'
                    )

    print(message.sid)