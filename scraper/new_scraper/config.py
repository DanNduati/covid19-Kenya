import os
from dotenv import load_dotenv

load_dotenv()
database_uri = os.environ.get('DatabaseUri')