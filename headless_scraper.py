import requests
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from datetime import datetime
import config as my_config
from models import Base

url = 'https://www.worldometers.info/coronavirus/'
database_uri = my_config.database_uri


def get_data():
	data = []
	header = []
	kenyan_data = []
	page = requests.get(url)
	soup = BeautifulSoup(page.text,'html.parser')
	table = soup.find('table',attrs={'id':'main_table_countries_today'})
	data_rows = table.find_all("tr", attrs={"style": ""})
	for i,item in enumerate(data_rows):
		c_data = item.text.strip().split("\n")
		if(c_data[1]== 'Kenya'):
			kenyan_data = c_data
		data.append(c_data)
	return data,kenyan_data
def conn_db():
	#connect to the database
	engine = create_engine(database_uri)
	connection = engine.connect()
	Base.metadata.bind = engine
	#create table
	'''
	try:
		Base.metadata.create_all()
		print('Table created successfully')
	except Exception as e:
		raise e
	'''


#store all countries' data to csv file and save the kenyan data to the database
def store_data():
	all_data,kenyan_data = get_data()
	frame = pd.DataFrame(all_data)
	date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	frame.to_csv(f'data/data_{date}.csv',header=False, index=False,encoding='utf-8')
	print(kenyan_data)
	conn_db()



'''


'''
def main():
	store_data()


if __name__ == "__main__":
	main()