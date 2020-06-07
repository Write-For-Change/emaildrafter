import urllib.request, json
import requests
from bs4 import BeautifulSoup
import re


def createQueryURL(postcode):
    # Remove all whitespace
    postcode = postcode.replace(" ", "").lower()

    # Seperate outcode and incode by a hyphen.
    postcodeHyphen = postcode[:-3] + "-" + postcode[-3:]
    # Get the first occurring letters up to the first number.
    area = re.search("[a-z]{1,2}", postcode)[0]
    # Get everything but the last two letters.
    sector = postcodeHyphen[:-2]

    # Create the URL to be queried.
    queryURL = "https://www.192.com/places/{}/{}/{}".format(
        area, sector, postcodeHyphen
    )
    return queryURL


def addressExtractor(url):
    addressList = []
    getH = requests.get(url)
    h = getH.content
    soup = BeautifulSoup(h, "html.parser")
    addresses = soup.select("td.js-ont-full-address.ont-hidden-on-smaller-than-tablet")
    for i in addresses:
        addressList.append(i.contents[0])
    return addressList


def getAddresses(postcode):
    return sorted(addressExtractor(createQueryURL(postcode)))
