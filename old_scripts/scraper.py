import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class virus():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def scrape_data(self):
        try:
            self.driver.get('https://www.worldometers.info/coronavirus/')
            #//*[@id="main_table_countries_today"]/tbody[1]/tr[118]/td[1]
            #/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table
            #//*[@id="main_table_countries_today"]
            #//*[@id="main_table_countries_today"]/tbody[1]/tr[93]
            table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[93]')
            country_element = table.find_element_by_xpath("//td[contains(., 'Kenya')]")
            row = country_element.find_element_by_xpath("./..")
            self.driver.close()
            self.driver.quit()
            data = row.text.split(" ")
            print(row.text)
            print(data)
            total_cases = data[2]
            new_cases = data[3]
            total_deaths = data[3]
            new_deaths = data[4]
            active_cases = data[6]
            total_recovered = data[5]
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