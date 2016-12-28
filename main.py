from app import App
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--android', required=True, type=str, help='Android app id')
parser.add_argument('-i', '--ios', required=True, type=str, help='ios app id' )
args = parser.parse_args()



def scrape(base_url, xpaths):
    print("scraper")