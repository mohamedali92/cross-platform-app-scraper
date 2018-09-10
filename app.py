from bs4 import BeautifulSoup
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
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def scrape(self):
        try:
            r = requests.get(self.baseUrl)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print (e)
            sys.exit(1)

        if "apple" in self.baseUrl:
            return self.scrapeIos(r)
        else:
            return self.scrapeAndroid(r)

    def scrapeIos(self, response):
        data = response.json()['results'][0]
        id = data['trackId']
        name = data['trackCensoredName']
        stars = data['averageUserRating']
        ratings = data['userRatingCount']
        lastUpdated = data['currentVersionReleaseDate']

        return (App(id, name, stars, ratings, lastUpdated))

    def scrapeAndroid(self, response):
        data = BeautifulSoup(response.content, "html.parser")
        id = data.find(class_="app-compatibility").get('data-docid')
        name = data.find(class_="id-app-title").get_text()
        stars = data.find(class_="score").get_text()
        ratings = data.find(class_="reviews-num").get_text()
        lastUpdated = data.find(itemprop="datePublished").get_text()
        return (App(id, name, stars, ratings, lastUpdated))
