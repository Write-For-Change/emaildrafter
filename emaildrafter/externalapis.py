import json
import requests
import re
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen


def create_query_url(postcode):
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


def address_extractor(url):
    addressList = []
    getH = requests.get(url)
    h = getH.content
    soup = BeautifulSoup(h, "html.parser")
    addresses = soup.select("td.js-ont-full-address.ont-hidden-on-smaller-than-tablet")
    for i in addresses:
        addressList.append(i.contents[0])
    return addressList


def get_addresses(postcode):
    return sorted(address_extractor(create_query_url(postcode)))


def lookup_postcode(postcode):
    """Check that a postcode is valid (when using the postcodes.io api)"""
    url_base = "http://api.postcodes.io/postcodes/"
    postcode = postcode.replace(" ", "").upper()
    try:
        with urlopen(url_base + postcode) as url:
            data = json.loads(url.read().decode())
            return data
    except HTTPError:
        return None
