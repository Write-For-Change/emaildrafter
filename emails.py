from urllib.error import HTTPError
import urllib.request, json
from emailtemplates import get_existing_templates
from mpdetails import get_mp_details
import logging

log = logging.getLogger("app")


def validatePostcodeApi(postcode):
    url_base = "http://api.postcodes.io/postcodes/"
    postcode = postcode.replace(" ", "").upper()
    try:
        with urllib.request.urlopen(url_base + postcode) as url:
            data = json.loads(url.read().decode())
            return data["status"] == 200
    except HTTPError:
        return False


def draft_all_emails(myname, postcode, address):
    ret = get_mp_details(postcode)
    constituency = ret["constituency"]
    MPname = ret["name"]
    MPemail = ret["email"]

    log.debug(
        "Details found. You live in {} constituency and your MP is {}, with email: {}".format(
            constituency, MPname, MPemail
        )
    )

    # Empty list of filled templates
    filled_email_templates = []
    # Get all the empty templates from templates.py
    empty_email_templates = get_existing_templates()
    # Set the user dictionary to include the name of the person sending
    user = {"name": myname, "address": address}

    for e in empty_email_templates:  # For each empty template
        if e.target is None:
            # If no defined target, use MP info to fill target fields
            e.set_target(name=MPname, email=MPemail, constituency=constituency)

        # ToDo : Implement setting a cc

        # Pass the dictionary containing user information to the template filler
        try:
            success = e.fill(user)  # Returns true if successfully filled

            if success:
                # Append successful templates to the list we return
                filled_email_templates.append(e)
        except AttributeError:
            log.debug("Target set incorrectly, failed to fill template")
            pass
        except KeyError as err:
            # Template not filled due to error in either template or user dict
            log.debug(err)
            pass

    return filled_email_templates


def draft_specific_templates(templates, name, postcode, address):
    user = {"name": name, "address": address}
    filled_email_templates = []
    mp = None
    for e in templates:
        if e.target is None and mp is None:
            # Only get MP info if target not set on one of the emails
            mp_details = get_mp_details(postcode)

        if e.target is None:
            # If target is none, set target to MP
            e.set_target(
                name=mp_details["name"],
                email=mp_details["email"],
                constituency=mp_details["constituency"],
            )
        # Pass the dictionary containing user information to the template filler
        try:
            success = e.fill(user)  # Returns true if successfully filled

            if success:
                # Append successful templates to the list we return
                filled_email_templates.append(e)
        except AttributeError:
            log.debug("Target set incorrectly, failed to fill template")
            pass
        except KeyError as err:
            # Template not filled due to error in either template or user dict
            log.debug(err)
            pass
    return filled_email_templates
