# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACc0e6fa2e310dfe07f875cf74eef7e7f2"
auth_token = "012865fb213d43bce244d853dba97371"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Your Tesla has been assigned a VIN number.\nClick on the link for more details: youtube.com/watch?v=t6FUR_nhGX8&t=6s",
                     from_='+18064294286',
                     to='+14082052742'
                 )

print(message.sid)
