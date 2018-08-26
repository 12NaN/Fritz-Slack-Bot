from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_message(command):
    message = client.messages.create(
                            body=command,
                            from_='',
                            to=''
                            )

