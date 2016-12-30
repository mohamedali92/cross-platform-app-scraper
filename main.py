from app import App
from app import AttributeScraper
import argparse

import sys

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--android', required=True, type=str, help='Android app id')
parser.add_argument('-i', '--ios', required=True, type=str, help='ios app id' )
args =vars(parser.parse_args())

iosUrl = 'https://itunes.apple.com/lookup?id=' + args['ios']
iosXPaths = {'id':'trackId' ,'name': 'trackCensoredName', 'stars': 'averageUserRating', 'ratings': 'userRatingCount', 'lastUpdated': 'currentVersionReleaseDate'}
androidUrl = 'https://play.google.com/store/apps/details?id=' + args['android']

AttributeScraper(iosUrl, "ios").scrape()
AttributeScraper(androidUrl, "android").scrape()