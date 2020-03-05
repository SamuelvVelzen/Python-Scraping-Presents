import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import config
import re

url = config.target["mainUrl"] + config.target["listUrl"]
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.findAll(['div.subtopics', 'ul', 'li', 'a']))

# parentDiv = soup.findAll("div", class_="subtopics")
# print(parentDiv)

print(soup.findAll(re.compile("div")))
# print(soup.findAll(href="/topics/embassies-consulates-and-other-representations/overview-countries-and-regions/liberia"))
