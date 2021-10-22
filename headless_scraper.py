import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup
from datetime import datetime
import config as my_config
from models import Base,Data

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

def store_db(k_data):
	#connect to the database
	engine = create_engine(database_uri)
	connection = engine.connect()
	Base.metadata.bind = engine
	
	data = Data(
		country_name = k_data[1],
		total_cases = clean_column(k_data[2]),
		new_cases = clean_column(k_data[3]), 
		total_deaths = clean_column(k_data[4]),
		new_deaths = clean_column(k_data[5]),
		total_recovered = clean_column(k_data[6]),
		new_recovered = clean_column(k_data[7]),
		active_cases = clean_column(k_data[8]),
		serious_cases = clean_column(k_data[9]),
		total_cases_per_m = clean_column(k_data[10]),
		deaths_per_m = clean_column(k_data[11]),
		total_tests = clean_column(k_data[12]),
		tests_per_m = clean_column(k_data[13]),
		population = clean_column(k_data[14]),
		new_cases_per_m = clean_column(k_data[18])
	) 	
	Session = sessionmaker(bind=engine)
	s = Session()
	try:
		s.add(data)
		s.commit()
		date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
		print(f'Success ->{date}')
	except Exception as e:
		raise e

def clean_column(no):
	if no=='':
		return 0
	else:
		no = no.replace(',', '')
		return int(no)

#store all countries' data to csv file and save the kenyan data to the database
def store_data():
	all_data,kenyan_data = get_data()
	#print(all_data[0])
	frame = pd.DataFrame(all_data)
	date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	frame.to_csv(f'data/data_{date}.csv',header=False, index=False,encoding='utf-8')
	store_db(kenyan_data)
	
def main():
	store_data()


if __name__ == "__main__":
	main()