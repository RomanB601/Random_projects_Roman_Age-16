import requests
import json
import os
from twilio.rest import Client

i = 1
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
o2 = response.json()
pic = o2["url"]
pic = str(pic)
explan = o2["explanation"]
explan =str(explan)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACb062c2c0f7fe50e06ef6e626a6580e43"
auth_token = 'a35c32d836ddc165fe05184267f954ee'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body= explan,
         from_='+12183003170',
         media_url=[pic],
         to='+17349853128'
     )
print(message.sid)