from twilio.rest import Client

def lambda_handler(event, context):
    account_sid = "account_sid" # US
    auth_token = "auth_token" # US
    client = Client(account_sid, auth_token)

	client.messages.create(
        to="phone_number",
        from_="twilio_phone_number", # I used US phone number 
        body="    this is message text contents    ")

# If you want to include picture in messages,

# 	client.messages.create(
#       to="phone_number",
#       from_="twilio_phone_number", # I used US phone number 
#       body="    this is message text contents    ",
# 	media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")

    
