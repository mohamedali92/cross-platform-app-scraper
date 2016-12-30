from app import AttributeScraper
from app import App
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--android', required=True, type=str, help='Android app id')
parser.add_argument('-i', '--ios', required=True, type=str, help='ios app id')
args = vars(parser.parse_args())

iosUrl = 'https://itunes.apple.com/lookup?id=' + args['ios']
androidUrl = 'https://play.google.com/store/apps/details?id=' + args['android']

iosApp = AttributeScraper(iosUrl).scrape()
androidApp = AttributeScraper(androidUrl).scrape()
