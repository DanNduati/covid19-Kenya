
import time
from twilio.rest import Client
from selenium import webdriver
import re

class virus():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def scrape_data(self):
        try:
            self.driver.get('https://www.worldometers.info/coronavirus/')
            #//*[@id="main_table_countries_today"]/tbody[1]/tr[118]/td[1]
            
            table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
            country_element = table.find_element_by_xpath("//td[contains(., 'Kenya')]")
            row = country_element.find_element_by_xpath("./..")
            data = row.text.split(" ")
            total_cases = data[1]
            new_cases = data[2]
            total_deaths = data[3]
            new_deaths = data[4]
            active_cases = data[5]
            total_recovered = data[6]
            serious_critical = data[7]

            print("Country: " + country_element.text)
            print("Total cases: " + total_cases)
            print("New cases: " + new_cases)
            print("Total deaths: " + total_deaths)
            print("New deaths: " + new_deaths)
            print("Active cases: " + active_cases)
            print("Total recovered: " + total_recovered)
            print("Serious, critical cases: " + serious_critical)
        except:
            print('Web scraping failed')
            self.driver.close()
            self.driver.quit()
bot = virus()
bot.scrape_data()
