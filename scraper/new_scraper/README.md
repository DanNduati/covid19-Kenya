<center>
<h1><b>V2 headless Covid19 kenyan Data Scraper</b></h1>
</center>

## Introduction
This is v2 of the Covid19 kenyan Data Scraper that scrapes kenyan covid data from [worldometers](https://www.worldometers.info/coronavirus/) with Python using BeautifulSoup and requests. A cron job runs the worker script every 4 hours, which pulls data from worldometers real-time dashboard stores the kenyan data to a persistent mysql database and saves all the other countries data into a csv file.

## Installing locally
### Create a python virtual environment activate it
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
Create a `.env` file similar to `.env.example` and add your twilio credentials and database url to it

## Install the dependencies
```bash
pip install -r requirements.txt
```

## Run the script
As mentioned above I run this script in the background.For this I use the [cron](https://en.wikipedia.org/wiki/Cron) service available in all Unix-based distributions.
## Some Cron background and scheduling of our worker
Each user in a Unix system has the option to set up scheduled commands that are executed by the system in a "crontab" (cron table) file. The crontab command is used to open a text editor on the user's crontab file:
```bashhttps://www.worldometers.info/coronavirus/
crontab -e
```
The crontab -e command will start a text editor on the user's crontab file, which will initially be empty, aside from some explanatory comments. A scheduled job is given in the crontab file as a line with six fields. The first five fields are used to set up the run scheduled for the job. The sixth and last field is the command to run. You can configure multiple jobs, each with its own schedule by writing multiple lines in the crontab file.
```bash
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23) 
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
│ │ │ │ │                                       7 is also Sunday on some systems)
│ │ │ │ │
│ │ │ │ │
* * * * *  command to execute
```

To run the job every 4 hours
```bash
0 */4 * * * <cmd>
```
In my case that looks like this
```bash
0 */4 * * * /home/daniel/Desktop/covid19_kenya/venv/bin/python /home/daniel/Desktop/covid19_kenya/scraper/new_scraper/worker.py
```