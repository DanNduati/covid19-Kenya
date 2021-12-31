import os
from os.path import join,dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path,override=True)

#database
database_url = os.environ.get('DATABASE_URL')
#twilio
account_sid = os.environ.get('TWILIO_ACCOUNT_SID',None)
auth_token = os.environ.get('TWILIO_AUTH_TOKEN',None)
sender = os.environ.get('TWILIO_PHONE_NUMBER',None)