# -*- coding: utf-8 -*-

# import win32com.client as win32
import urllib.request, json
import requests
import logging
from bs4 import BeautifulSoup
from emailtemplates import get_existing_templates
from urllib.error import HTTPError
from wtforms.validators import ValidationError

log = logging.getLogger("app")


def validatePostcode(form, field):
    url_base = "http://api.postcodes.io/postcodes/"
    postcode = field.data.replace(" ", "")
    try:
        with urllib.request.urlopen(url_base + postcode) as url:
            data = json.loads(url.read().decode())
            return data["status"] == 200
    except HTTPError:
        raise ValidationError("Invalid postcode. Please try again.")
        return False


def getGovDetails(postcode):

    url_base = "http://api.postcodes.io/postcodes/"
    with urllib.request.urlopen(url_base + postcode) as url:
        data = json.loads(url.read().decode())
        if data["status"] == 200:
            topdata = data["result"]
        else:
            log.debug(f"Invalid postcode {postcode}")
            raise KeyError("No postcode found!")

    MPurl = (
        "http://lda.data.parliament.uk/commonsmembers.json?_view=members&_pageSize=2097&_page=0&constituency.label="
        + "%20".join(topdata["parliamentary_constituency"].split(" "))
    )

    with urllib.request.urlopen(MPurl) as url:
        MPdata = json.loads(url.read().decode())

        for possibleMP in MPdata["result"]["items"]:
            MPid = (possibleMP["_about"]).split("/")[-1]
            log.debug("Checking MP: {}".format(possibleMP["fullName"]))

            try:
                MPurl = "https://members.parliament.uk/member/{}/contact".format(MPid)
                MPemails = emailExtractor(MPurl)  # MP email (in a list)
                assert len(MPemails) > 0
                # Quick hack to only return one email
                MPemail = MPemails[0]

                myward = topdata["admin_ward"]  # User's ward
                MPname = possibleMP["fullName"]["_value"]
                log.debug("Found correct MP: {}. Email: {} ".format(MPname, MPemail))
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


def draftEmails(myname, postcode):
    ret = getGovDetails(postcode)
    ward = ret["ward"]
    MPname = ret["MPname"]
    MPemail = ret["MPemail"]

    log.debug(
        "Details found. You live in {} ward and your MP is {}, with email: {}".format(
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
            log.debug("Failed to fill template, subject: {}".format(e.subject))
            pass

    return filled_email_templates
