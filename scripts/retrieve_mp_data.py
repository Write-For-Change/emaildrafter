import urllib.request, json
import requests
from bs4 import BeautifulSoup
import csv
from urllib.error import HTTPError


###################### These aren't used anymore but may be used for a future thing if MPs aren't in the database ###############################


def getGovDetails(postcode):

    url_base = "http://api.postcodes.io/postcodes/"
    with urllib.request.urlopen(url_base + postcode) as url:
        data = json.loads(url.read().decode())
        if data["status"] == 200:
            topdata = data["result"]
        else:
            print(f"Invalid postcode {postcode}")
            raise KeyError("No postcode found!")

    MPurl = (
        "http://lda.data.parliament.uk/commonsmembers.json?_view=members&_pageSize=2097&_page=0&constituency.label="
        + "%20".join(topdata["parliamentary_constituency"].split(" "))
    )

    with urllib.request.urlopen(MPurl) as url:
        MPdata = json.loads(url.read().decode())

        for possibleMP in MPdata["result"]["items"]:
            MPid = (possibleMP["_about"]).split("/")[-1]
            print("Checking MP: {}".format(possibleMP["fullName"]))

            try:
                MPurl = "https://members.parliament.uk/member/{}/contact".format(MPid)
                MPemails = emailExtractor(MPurl)  # MP email (in a list)
                assert len(MPemails) > 0
                # Quick hack to only return one email
                MPemail = MPemails[0]

                myward = topdata["admin_ward"]  # User's ward
                MPname = possibleMP["fullName"]["_value"]
                print("Found correct MP: {}. Email: {} ".format(MPname, MPemail))
                break
            except:
                pass

    return {"ward": myward, "MPemail": MPemail, "MPname": MPname}


def emailExtractor(urlString):
    emailList = []
    getH = requests.get(urlString)
    h = getH.content
    soup = BeautifulSoup(h, "html.parser")
    mailtos = soup.select("a[href^=mailto]")
    for i in mailtos:
        href = i["href"]
        try:
            str1, str2 = href.split(":")
        except ValueError:
            break

        emailList.append(str2)
    return emailList


######################### End of (temporarily) useless functions


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
