# covid19-webscraper-and-sms-alert
## Background
### webscraper
This is a basic webscrapper built on python3 and which collects real-time data from both official and unofficial sources so that the public can have a fair-minded understanding of this outbreak with transparent data sources.To pull data from these sources i use the selenium module,primarily it is for automating web applications for testing purposes but i use it to scrape data from: https://www.worldometers.info/coronavirus/

### webscraper with message alert
To add ontu the webscripting We will use the Twilio API to send the scraped data. Twilio is not a free service but they provide a trial account with some credit.In order to get started, we need to make an account in Twilio.
https://www.twilio.com/try-twilio .Grab your Account SID and auth token from your Twilio account console.If you are on a Twilio Trial account, your outgoing SMS messages are limited to phone numbers that you have verified with Twilio. Phone numbers can be verified via your Twilio Console's Verified Caller IDs.
### Required libraries
1.Selenium
2.twilio
## installation
```bash
pip install selenium
```
```bash
pip install twilio
```
# running the script
Web scraper script
```bash
python scraper.py
```
Web scraper script with sms alert
```bash
python scraper_msg.py
```
# expected output
![Expected output](https://github.com/DanNduati/covid19-webscraper-and-sms-alert/blob/master/terminaloutput.png)

