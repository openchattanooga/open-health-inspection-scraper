from bs4 import BeautifulSoup
import scraperwiki
import json
import urllib

def clean(data):
    if data is not None:
        return data.replace(u'\xa0', '')
    return data

def getContent(url):
    html = scraperwiki.scrape(url)
    return BeautifulSoup(html)

def getText(element):
    return clean(element.find(text=True))

def getAllText(element):
    text = element.find_all(text=True)
    return [ clean(t) for t in text ]

def getLatLng(address, city):
    # Need to implement status code-based error handling
    api_url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address="
    #api_key = ""

    url = api_url + urllib.quote_plus(address + " in " + city + ", VA")
    result = json.load(urllib.urlopen(url))

    lat_lng = {'lat': result['results'][0]['geometry']['location']['lat'], 'lng': result['results'][0]['geometry']['location']['lng']}

    return lat_lng