import pathlib
from datetime import datetime
import logging
import logging.config
import requests
from models import Data
from utils.scraper import get_data
from database import Session
import pandas as pd

logging.config.fileConfig(fname="log.conf",disable_existing_loggers=False)
# get the logger specified in the config file
logger = logging.getLogger("scrapper")
# Disable requests encoding logging
logging.getLogger("chardet.charsetprober").disabled = True
logging.getLogger('urllib3.connectionpool').disabled=True

def clean_column(field):
	#normalize the data
	field=0 if field=='' else int(float(field.replace(',', '')))
	return field

def store_db(k_data:list):
	session = Session()
	data = Data(country_name = k_data[1],total_cases = clean_column(k_data[2]),new_cases = clean_column(k_data[3]),total_deaths = clean_column(k_data[4]),new_deaths = clean_column(k_data[5]),total_recovered = clean_column(k_data[6]),new_recovered = clean_column(k_data[7]),active_cases = clean_column(k_data[8]),serious_cases = clean_column(k_data[9]),total_cases_per_m = clean_column(k_data[10]),deaths_per_m = clean_column(k_data[11]),total_tests = clean_column(k_data[12]),tests_per_m = clean_column(k_data[13]),population = clean_column(k_data[14]),new_cases_per_m = clean_column(k_data[18]))
	try:
		session.add(data)
		session.commit()
		logging.info("Data added to db!")
	except Exception as e:
		logging.exception("Exception occured!")
	finally:
		session.close()

def main():
	try:
		logger.info("Scraping data...")
		all_data,kenyan_data = get_data()
		logger.info("Data scrapped successfully!")
		frame = pd.DataFrame(all_data)
		date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
		csv_path = pathlib.Path(__file__).parent.joinpath(f"data/data_{date}.csv")
		frame.to_csv(csv_path,header=False, index=False,encoding='utf-8')
		store_db(kenyan_data)
	except requests.exceptions.RequestException:
		logging.exception("Scraping requests exception occured!")
	except Exception as e:
		logging.exception("Other exception occured!")

if __name__ == "__main__":
	main()