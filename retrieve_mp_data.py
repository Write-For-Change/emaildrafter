import urllib.request, json
import requests
from bs4 import BeautifulSoup
import csv


def retrieve_mp_data():

    MPdata = {}

    MPurl = "http://lda.data.parliament.uk/commonsmembers.json?_view=members&_pageSize=3000&_page=0"

    with urllib.request.urlopen(MPurl) as url:
        MPlist = json.loads(url.read().decode())["result"]["items"]

    for mp in MPlist:
        constituency = mp["constituency"]["label"]["_value"]
        fullname = (
            mp["givenName"]["_value"].strip() + " " + mp["familyName"]["_value"].strip()
        )
        real_fullname = mp["fullName"]["_value"].strip()
        id = (mp["_about"]).split("/")[-1]

        MPdata[fullname] = [constituency, real_fullname]

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
    for key, value in MPdata.items():
        try:
            MPdata_formatted.append(
                {"name": value[1], "email": value[2], "constituency": value[0]}
            )
        except:
            errors += 1
            pass
    return MPdata_formatted
