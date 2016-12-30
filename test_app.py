import app
import pytest

# Testing Instagram cross platform app


def test_ios():
    iosUrl = 'https://itunes.apple.com/lookup?id=389801252'
    iosApp = app.AttributeScraper(iosUrl).scrape()
    assert iosApp.id == 389801252


def test_android():
    androidUrl = 'https://play.google.com/store/apps/details?id=com.instagram.android'
    androidApp = app.AttributeScraper(androidUrl).scrape()
    assert androidApp.id == "com.instagram.android"


def test_invalidUrl():
    with pytest.raises(SystemExit):
        url = ''
        app.AttributeScraper(url).scrape()
