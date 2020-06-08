import urllib.request, json
import requests
from bs4 import BeautifulSoup
import csv
import pymongo


def convert_party(party):
    switcher = {
        "Conservative": 1,
        "Labour": 2,
        "Scottish National Party": 3,
        "Liberal Democrats": 4,
        "Independent": 5,
        "Plaid Cymru": 6,
        "Social Democratic Party": 7,
        "Social Democratic & Labour Party": 7,
        "Alliance": 8,
        "Green Party": 9,
        "Democratic Unionist Party": 10,
        "Sinn Féin": 11,
        "Speaker": 12,
    }
    return switcher.get(party)


def retrieve_mp_data():

    MPdata = {}

    MPurl = "http://lda.data.parliament.uk/commonsmembers.json?_view=members&_pageSize=3000&_page=0"

    # Get the list of MP JSON Data
    with urllib.request.urlopen(MPurl) as url:
        MPlist = json.loads(url.read().decode())["result"]["items"]

    # Iterate over each MP
    for mp in MPlist:
        # Get each relevant field
        constituency = mp["constituency"]["label"]["_value"]
        party = mp["party"]["_value"]
        # Format the name nicely!
        fullname = (
            mp["givenName"]["_value"].strip() + " " + mp["familyName"]["_value"].strip()
        )
        real_fullname = mp["fullName"]["_value"].strip()
        # id = (mp["_about"]).split("/")[-1]

        # Create an entry for the MP in the dict
        MPdata[fullname] = [constituency, real_fullname, party]

    # Open the CSV file containing the email.
    with open("190391mpl.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            full_name = (
                row[0].replace('"', "").strip() + " " + row[2].replace('"', "").strip()
            )
            try:
                MPdata[full_name].append(row[3].replace(" ", "").replace('"', ""))
            except:
                pass

    MPdata_formatted = []
    errors = 0
    count = 1
    for key, value in MPdata.items():
        try:
            MPdata_formatted.append(
                {
                    "_id": count,
                    "name": value[1],
                    "email": value[3],
                    "constituency": value[0],
                    "party": convert_party(value[2]),
                }
            )
            count += 1
        except:
            errors += 1
            pass
    return MPdata_formatted


client = pymongo.MongoClient(
    "mongodb://heroku_b22mk7d6:mpdj7v335osvtda7c3g3ffo2ao@ds121565.mlab.com:21565/heroku_b22mk7d6?retryWrites=false"
)
# Define where the data is stored.
mpCollection = client["heroku_b22mk7d6"]["mp_email_list"]

# Execute the query on the mpCollection
mpDetails = mpCollection.insert_many(retrieve_mp_data())
