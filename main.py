# DEVELOPED BY SAKSHAM

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs

header = {"User-Agent": "Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers=header)
html = urlopen(req)
# print(html.status)

obj = bs(html)

# COVID-19 IN INDIA
total_cases = obj.find("div", {"class": "maincounter-number"}).span.text
total_deaths = list(obj.find("div", {"id": "maincounter-wrap"}).next_siblings)[1].span.text
recovered = list(obj.find("div", {"id": "maincounter-wrap"}).next_siblings)[3].span.text

# TODAY'S UPDATE
new_cases = obj.find("li", {"class": "news_li"}).strong.text.split()[0]
new_deaths = list(obj.find("li", {"class": "news_li"}).strong.next_siblings)[1].text.split()[0]


# OUTPUT
