import requests
from bs4 import BeautifulSoup
import schedule, time, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from replit import db

#there is no error handling included

#using Gmail and my personal account email notificaiton is sent to me if price_check function found the price right
def email_sending(price):
        
    password = os.environ['app_password']
    username = os.environ['email']
    
    email = f"WUHUU! Price of GT SPORT is now at {price}€. Go to https://www.vpd.fi/gran-turismo-sport-hits-ps4.html to buy now!"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    message = MIMEMultipart()
    message["to"] = username
    message["from"] = "Monco C."
    message["subject"] = "New event"
    message.attach(MIMEText(email, "html"))

    s.send_message(message)
    print("Email has been sent")
    del message

        
#this functions checks if price on web page is under our pre-set max limit
def price_check(price):
    price = price.replace(",",".")
    max_price = 20.00
    if float(price) < max_price:
        email_sending(price)
    else:
        print("Ah shuut. Still can't afford it.")


#web_crawler checks for a specific product's price
def web_crawler():
    print("Crawling started")
    print()

    URL = "https://www.vpd.fi/gran-turismo-sport-hits-ps4.html"
    
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    price_box = soup.find("div", {"class":"price-box price-final_price"})
    product_price = price_box.find("span", {"class":"price"})
    price_check(product_price.text[:-2])
    


