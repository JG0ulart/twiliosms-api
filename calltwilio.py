from twilio.rest import Client

account_sid = "PUT YOU SID HERE"
auth_token = "PUT YOU TOKEN HERE"
client = Client(account_sid, auth_token)

call = client.calls.create(
  to="+YOU NUMBER TO RECEIVE HERE", 
  from_="+NUMBER TO SEND HERE",
  url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)