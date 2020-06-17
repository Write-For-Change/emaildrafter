"""Connections to the MP Details database for data relating to an MP & postcode lookup"""
import urllib.request, json
from urllib.error import HTTPError
from database import myDb

# Instantiate the db
mongo = myDb()


def validate_postcode_api(postcode):
    """Check that a postcode is valid (when using the postcodes.io api)"""
    url_base = "http://api.postcodes.io/postcodes/"
    postcode = postcode.replace(" ", "").upper()
    try:
        with urllib.request.urlopen(url_base + postcode) as url:
            data = json.loads(url.read().decode())
            return data
    except HTTPError:
        return None


def get_mp_details(postcode):
    url_base = "http://api.postcodes.io/postcodes/"
    with urllib.request.urlopen(url_base + postcode) as url:
        data = json.loads(url.read().decode())
        if data["status"] == 200:
            # Create query from the data retrieved from postcodes.io
            query = {"constituency": data["result"]["parliamentary_constituency"]}
        else:
            raise KeyError("No postcode found!")

    return mongo.get_one("mp_email_list", query)
