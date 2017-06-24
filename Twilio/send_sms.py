from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC268d9c2f447e6f74dba3535640b4b2ad"
# Your Auth Token from twilio.com/console
auth_token  = "42405b3ef6a2929d3dd37e8b999f74aa"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918059459498", 
    from_="+19102924159",
    body="Hello from Python!")

print(message.sid)
