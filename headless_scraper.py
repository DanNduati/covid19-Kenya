import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.worldometers.info/coronavirus/'
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
