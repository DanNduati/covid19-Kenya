#!/usr/bin/python3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from models import Base

table_name = 'data'

load_dotenv()
database_uri = os.environ.get('DatabaseUri')
engine = create_engine(database_uri)
if not database_exists(engine.url):
    create_database(engine.url)

assert(database_exists(engine.url))
connection = engine.connect()
Base.metadata.bind = engine
if not engine.dialect.has_table(connection,table_name):
	try:
		Base.metadata.create_all()
		print('Table created successfully')
	except Exception as e:
		raise e
else:
	print('Table exists already!')