from twilio.rest import Client

class TwilioSms():
    def __init__(self,account_sid:str,auth_token:str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid,auth_token)
    def send(self,sender:str,recepient:str,msg:str):
        message = self.client.messages.create(
            body = msg,
            from_ = sender,
            to=recepient
        )
        print(message.sid)