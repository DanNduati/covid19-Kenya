import time
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

class virus():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        
    def scrape_data(self):
        try:
            self.driver.get('https://www.worldometers.info/coronavirus/')
            #//*[@id="main_table_countries_today"]/tbody[1]/tr[118]/td[1]
            table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
            country_element = table.find_element_by_xpath("//td[contains(., 'Kenya')]")
            row = country_element.find_element_by_xpath("./..")
            self.driver.quit()
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

            try:
                send_msg(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical)
            except :
                print('Message send failed')
        except:
            print('Web scraping failed')
            self.driver.close()
            self.driver.quit()

def send_msg(country,tcases,ncases,tdeaths,ndeaths,acases,trecovered,scritical):
    account_sid = 'your account sid'
    auth_token = 'your authentication token'
    client = Client(account_sid,auth_token)
    msg = 'Today in ' + country + '\
            \nThere is new data on coronavirus:\
            \nTotal cases: ' + tcases +'\
            \nNew cases: ' + ncases + '\
            \nTotal deaths: ' + tdeaths + '\
            \nNew deaths: ' + ndeaths + '\
            \nActive cases: ' + acases + '\
            \nTotal recovered: ' + trecovered + '\
            \nSerious, critical cases: ' + scritical  + '\
            \nCheck the link: https://www.worldometers.info/coronavirus/'
    message =client.messages.create(
        body = str(msg),
        from_='your twilio number',
        to='+number you want to send message to must be twilio veriified'
    )
    print(message.sid)

bot = virus()
bot.scrape_data()
