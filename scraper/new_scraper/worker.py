import pathlib
from datetime import datetime
from models import Data
from utils.scraper import get_data
from database import Session
import pandas as pd

def clean_column(field):
	#normalize the data
	field=0 if field=='' else int(float(field.replace(',', '')))
	return field

def store_db(k_data:list):
	session = Session()
	data = Data(country_name = k_data[1],total_cases = clean_column(k_data[2]),new_cases = clean_column(k_data[3]),total_deaths = clean_column(k_data[4]),new_deaths = clean_column(k_data[5]),total_recovered = clean_column(k_data[6]),new_recovered = clean_column(k_data[7]),active_cases = clean_column(k_data[8]),serious_cases = clean_column(k_data[9]),total_cases_per_m = clean_column(k_data[10]),deaths_per_m = clean_column(k_data[11]),total_tests = clean_column(k_data[12]),tests_per_m = clean_column(k_data[13]),population = clean_column(k_data[14]),new_cases_per_m = clean_column(k_data[18]))
	session.add(data)
	session.commit()
	session.close()

def main():
	all_data,kenyan_data = get_data()
	frame = pd.DataFrame(all_data)
	date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	csv_path = pathlib.Path(__file__).parent.joinpath(f"data/data_{date}.csv")
	frame.to_csv(csv_path,header=False, index=False,encoding='utf-8')
	store_db(kenyan_data)

if __name__ == "__main__":
	main()