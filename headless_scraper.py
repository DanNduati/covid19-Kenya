import requests
import pandas as pd
import sqlalchemy as db
from bs4 import BeautifulSoup
from datetime import datetime
import config as my_config
from models import Base

url = 'https://www.worldometers.info/coronavirus/'
database_uri = my_config.database_uri

page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
#print(soup.prettify())
#extract the table
table = soup.find('table',attrs={'id':'main_table_countries_today'})
#print(table)
data_rows = table.find_all("tr", attrs={"style": ""})
#print(data_rows)
#convert the rows into list form
data = []
header = []
kenyan_data = []
for i,item in enumerate(data_rows):
	#print(f'Country count {i} data: {item.text}')
	c_data = item.text.strip().split("\n")
	if(c_data[1]== 'Kenya'):
		#print(f'Found Kenya table row: {i}')
		kenyan_data = c_data
	#store the rest of the countries data as well
	data.append(c_data)
header = data[0]
print(header)
print(kenyan_data)
#convert the data to a pandas dataframe 
frame = pd.DataFrame(data)
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
frame.to_csv(f'data/data_{date}.csv',header=False, index=False,encoding='utf-8')
#connect to the database
engine = db.create_engine(database_uri)
connection = engine.connect()
Base.metadata.bind = engine
#create table
try:
	Base.metadata.create_all()
	print('Table created successfully')
except Exception as e:
	raise e