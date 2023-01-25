# Project Title

Product price scraper

## Description

Web scraping a specific product page for price. If price has gone down, email notification is sent.

## Getting Started

Instructions on how to set up the project on a local machine for development and testing purposes.

### Prerequisites

A list of necessary tools and dependencies to run the project.

Python with necessary libraries:
requests
BeautifulSoup
schedule
time
os
smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

This code also uses Replit.com's secret feature for email password and username.


### Installing

No specific steps required.

## Usage

By updating following parts you can  modify this code for your specific purpose:

#Schedule in main.py is set to operate in 60 second interval.
#web_crawler functions is set for a speific web page and to check for a price there
#price_check funtion then compares price provided by web_crawler with pre-set value it has
#then if price is on suitable level, email_sending function is called, which sends an email using Gmail, with set password and username (which are hidden using Replit.com's Secrets feature)

## Contributing

Thank you for your interest in contributing to this project! However, at this time we are not accepting contributions. We appreciate your understanding and support. 

If you would like to get involved with the project, please consider sharing it with others, providing feedback, or contributing in other ways such as submitting bug reports or feature requests.

## License

This project is licensed under the terms of the MIT license. 


