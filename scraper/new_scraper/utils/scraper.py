#!/usr/bin/python3.7
import requests
from bs4 import BeautifulSoup

def get_data()->list:
	url = 'https://www.worldometers.info/coronavirus/'
	data = kenyan_data = []
	html = requests.get(url)
	soup = BeautifulSoup(html.text,'html.parser')
	table = soup.find('table',attrs={'id':'main_table_countries_today'})
	data_rows = table.find_all("tr", attrs={"style": ""})
	for item in data_rows:
		c_data = item.text.strip().split("\n")
		if(c_data[1]== 'Kenya'):
			kenyan_data = c_data
		data.append(c_data)
	return data,kenyan_data