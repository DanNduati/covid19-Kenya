#!/usr/bin/python3.7
import time
import asyncio
import aiohttp
import logging
from bs4 import BeautifulSoup
from aiohttp import ClientSession

async def fetch_html(url:str,session:ClientSession)->str:
	resp = await session.request(method="GET", url=url)
	html = await resp.text()
	return html

async def get_data(url:str,session:ClientSession):
	data = kenyan_data = []
	html = await fetch_html(url=url,session=session)
	soup = BeautifulSoup(html,'html.parser')
	table = soup.find('table',attrs={'id':'main_table_countries_today'})
	data_rows = table.find_all("tr")
	for item in data_rows:
		c_data = item.text.strip().split("\n")
		if(c_data[1]== 'Kenya'):
			kenyan_data = c_data
		data.append(c_data)
	return data,kenyan_data

async def main():
	url = 'https://www.worldometers.info/coronavirus/'
	async with aiohttp.ClientSession() as session:
		_,data = await get_data(url=url,session=session)
	print(data)
	return data
		

start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))