#!/usr/bin/env python2.7

import os
import sys
import requests
import json
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from Article import Article

site = "http://hosted.ap.org"
urlList = ["/dynamic/fronts/US?SITE=AP&SECTION=HOME", "/dynamic/fronts/WORLD?SITE=AP&SECTION=HOME", "/dynamic/fronts/BUSINESS?SITE=AP&SECTION=HOME", "/dynamic/fronts/TECHNOLOGY?SITE=AP&SECTION=HOME", "/dynamic/fronts/ENTERTAINMENT?SITE=AP&SECTION=HOME", "/dynamic/fronts/HEALTH?SITE=AP&SECTION=HOME", "/dynamic/fronts/SCIENCE?SITE=AP&SECTION=HOME", "/dynamic/fronts/POLITICS?SITE=AP&SECTION=HOME"]
articleJSONList = []

for i in range(len(urlList)):
	url = site + urlList[i];
	response = requests.get(url)
	html = response.content
	geolocator = Nominatim()

	soup = BeautifulSoup(html, 'lxml')
	articleNames = soup.findAll('a', attrs={'class':'ap-topheadlineitem-a'})
	articleDetails = soup.findAll('span', attrs={'class':'topheadlinebody'})

	for i in range(len(articleNames)):
		# the name of the article
		article = Article(articleNames[i].text);

		# storing article urls...
		if articleNames[i].has_attr('href'):
			article.url = site + articleNames[i]['href']

		# storing location name of the article
		if len(articleDetails[i].text.split('--')) >= 2:
			article.location = articleDetails[i].text.split('--')[0]
			article.location = article.location.split('     ')[0]
			if article.location == "UNITED NATIONS":
				article.geocode = (40.7494, -73.9681)
			else:
				location = geolocator.geocode(article.location)
				article.geocode = (location.latitude, location.longitude)

			# storing the little snippet about the article
			article.snippet = articleDetails[i].text.split('-- ')[1]

			# adding the article to the article list
			articleJSONList.append(article.getJSONData())

with open('data.json', 'w') as outFile: 
	json.dump(articleJSONList, outFile)


