from bs4 import BeautifulSoup
import json
import requests
import sys


class App:

    def __init__(self, id, name, stars, ratings, lastUpdated):
        self.id = id
        self.name = name
        self.stars = stars
        self.ratings = ratings
        self.lastUpdated = lastUpdated

    def __str__(self):
        return str(self.id) +"\n"+str(self.name)+"\n"+str(self.stars)+"\n"+str(self.ratings)+"\n"+str(self.lastUpdated)

class AttributeScraper:
    def __init__(self, baseUrl, platform):
        self.baseUrl = baseUrl
        self.platform = platform

    def scrape(self):
        try:
            r = requests.get(self.baseUrl)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print (err)
            sys.exit(1)

        if self.platform == 'ios':
            self.scrapeIos(r)
        else:
            self.scrapeAndroid(r)

    def scrapeIos(self, response):
        data = response.json()['results'][0]
        id = data['trackId']
        name = data['trackCensoredName']
        stars = data['averageUserRating']
        ratings = data['userRatingCount']
        lastUpdated = data['currentVersionReleaseDate']

        print(App(id, name, stars, ratings, lastUpdated))

    def scrapeAndroid(self, response):
        c = response.content
        data = BeautifulSoup(c, "html.parser")
        id = 513121
        name = data.find(class_="id-app-title").get_text()
        stars = data.find(class_="score").get_text()
        ratings = data.find(class_="reviews-num").get_text()
        lastUpdated = data.find(itemprop="datePublished").get_text()
        print(App(id, name, stars, ratings, lastUpdated))