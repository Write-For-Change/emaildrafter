import urllib.request, json
from database import myDb

# Instantiate the db
mongo = myDb()


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
