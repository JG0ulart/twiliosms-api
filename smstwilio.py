from twilio.rest import Client

account_sid = "PUT YOU SID HERE"
auth_token = "PUT YOU TOKEN HERE"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+YOU NUMBER TO RECEIVE HERE", 
    from_="+NUMBER TO SEND HERE",
    body="Oi gatinha!")

print(message.sid)