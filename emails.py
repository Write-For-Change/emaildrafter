# -*- coding: utf-8 -*-

# import win32com.client as win32
import urllib.request, json
import requests
from bs4 import BeautifulSoup
from templates import get_existing_templates


def getGovDetails(postcode):

    url_base = "http://api.postcodes.io/postcodes/"
    with urllib.request.urlopen(url_base + postcode) as url:
        data = json.loads(url.read().decode())
        if data["status"] == 200:
            topdata = data["result"]
        else:
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
                myward = topdata["admin_ward"]  # User's ward
                MPname = possibleMP["fullName"]["_value"]
                print(
                    "Found correct MP: {}. {} emails found".format(
                        MPname, len(MPemails)
                    )
                )
                break
            except:
                pass

    return {"ward": myward, "MPemail": MPemails, "MPname": MPname}


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


def draftEmails(myname, postcode):
    ret = getGovDetails(postcode)
    ward = ret["ward"]
    MPname = ret["MPname"]
    MPemails = ret["MPemail"]

    print(
        "Details found. You live in {} ward and your MP is {}, with email(s): {}".format(
            ward, MPname, MPemails
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
            # If there isn't a defined target, we probably need to find the MP of the person - could move the postcode finder here?
            print("Need to get information about MP to fill out target of email")
            # Once implemented, you could update the target of the email template using this function:
            # e.set_target(name="",email="",ward="")
            pass
        else:
            print("Filling template with user info")
            # May want to set a cc if the target is set?
            # Pass the dictionary containing user information to the template filler
            success = e.fill(user)
            # It will return true if completed successfully
            if success:
                print("Successfully filled template")
                # Append successful templates to the list we return
                filled_email_templates.append(e)
            else:
                print("Failed to fill template, passing")
                pass

    return filled_email_templates
