import functions
from bs4 import BeautifulSoup
import schedule, time


#From main.py schedule calls for the web_crawler functions, which calls for other functions as needed


schedule.every(60).seconds.do(functions.web_crawler)

while True:
    schedule.run_pending()
    time.sleep(1)
