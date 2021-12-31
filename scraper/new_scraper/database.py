from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

database_uri = config.database_url
#create sqlalchemy engine
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
Base = declarative_base()