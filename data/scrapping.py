import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup

import config
import re


def getData():
    url = config.target["mainUrl"] + config.target["listUrl"]
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    countries = {}

    for tag in soup.select("div.subtopics ul li a"):
        data = {}
        overviewUrl = config.target["mainUrl"] + tag["href"]
        overviewBody = requests.get(overviewUrl)
        overviewSoup = BeautifulSoup(overviewBody.text, 'html.parser')

        for tag in overviewSoup.select("#content h1"):
            try:
                country = tag.text.split(': ')[1]

                if "Missions" in country:
                    countryArr = country.split(" ")
                    newcountry = []

                    for count, item in enumerate(countryArr):
                        if count != 0:
                            newcountry.append(item)

                    data['name'] = " ".join(newcountry)

                else:
                    data['name'] = tag.text.split(': ')[1]

            except:
                data['name'] = tag.text.split(': ')[0]

        for overviewTag in overviewSoup.select("ul.common li a"):
            time.sleep(1)

            if "/topics/" in overviewTag["href"]:
                countryUrl = config.target["mainUrl"] + overviewTag["href"]
                countryBody = requests.get(countryUrl)
                countrySoup = BeautifulSoup(countryBody.text, 'html.parser')

                emailArr = []
                for count, email in enumerate(countrySoup.select('a.email')):
                    emailArr.append(email.text)

                data['email'] = emailArr
        countries[data["name"].strip()] = data

    return json.dumps(countries)
