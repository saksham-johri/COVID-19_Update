# DEVELOPED BY SAKSHAM

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import datetime

header = {"User-Agent": "Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers=header)
html = urlopen(req)
# print(html.status)

obj = BeautifulSoup(html, features="html.parser")

# COVID-19 IN INDIA
total_cases = obj.find("div", {"class": "maincounter-number"}).span.text
total_deaths = list(obj.find("div", {"id": "maincounter-wrap"}).next_siblings)[1].span.text
recovered = list(obj.find("div", {"id": "maincounter-wrap"}).next_siblings)[3].span.text

# TODAY'S UPDATE
new_cases = obj.find("li", {"class": "news_li"}).strong.text.split()[0]
new_deaths = list(obj.find("li", {"class": "news_li"}).strong.next_siblings)[1].text.split()[0]

# TODAY'S DATE

today = (str(datetime.now())).split()[0]
today_date = today.split('-')
today_date = f"{today_date[2]}.{today_date[1]}.{today_date[0]}"
# print(today_date)

# OUTPUT
print(f"****  COVID-19 IN INDIA TILL {today_date}  ****")
print(f"Total Cases: {total_cases} \nTotal Deaths: {total_deaths} \nRecovered: {recovered}")

print(f"\n****  TODAY'S UPDATE  ****")
print(f"Date: {today_date}")
print(f"New Cases: {new_cases} \nNew Deaths: {new_deaths}", end='\n')
