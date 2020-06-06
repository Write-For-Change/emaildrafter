# -*- coding: utf-8 -*-

# import win32com.client as win32
import urllib.request, json
import requests
import pymongo
from bs4 import BeautifulSoup
from emailtemplates import get_existing_templates


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


def getMPDetails(postcode):
    url_base = "http://api.postcodes.io/postcodes/"
    with urllib.request.urlopen(url_base + postcode) as url:
        data = json.loads(url.read().decode())
        if data["status"] == 200:
            # Create query from the data retrieved from postcodes.io
            query = {"constituency": data["result"]["parliamentary_constituency"]}
        else:
            raise KeyError("No postcode found!")

    # Tell Python where to look for the database.
    client = pymongo.MongoClient(
        "mongodb://heroku_b22mk7d6:mpdj7v335osvtda7c3g3ffo2ao@ds121565.mlab.com:21565/heroku_b22mk7d6"
    )
    # Define where the data is stored.
    mpCollection = client["heroku_b22mk7d6"]["mp_email_list"]

    # Execute the query on the mpCollection
    mpDetails = mpCollection.find_one(query)
    # Return a dictionary of the email, name and constituency
    return mpDetails


def draftEmails(myname, postcode):
    ret = getMPDetails(postcode)
    ward = ret["constituency"]
    MPname = ret["name"]
    MPemail = ret["email"]

    print(
        "Details found. You live in {} constituency and your MP is {}, with email: {}".format(
            ward, MPname, MPemail
        )
    )

    # Empty list of filled templates
    filled_email_templates = []
    # Get all the empty templates from templates.py
    empty_email_templates = get_existing_templates()
    # Set the user dictionary to include the name of the person sending
    user = {"name": myname}

    for e in empty_email_templates:  # For each empty template
        if e.target is None:
            # If no defined target, use MP info to fill target fields
            e.set_target(name=MPname, email=MPemail, ward=ward)

        # ToDo : Implement setting a cc

        # Pass the dictionary containing user information to the template filler
        success = e.fill(user)  # Returns true if successfully filled

        if success:
            # Append successful templates to the list we return
            filled_email_templates.append(e)
        else:
            print("Failed to fill template, subject: {}".format(e.subject))
            pass

    return filled_email_templates
