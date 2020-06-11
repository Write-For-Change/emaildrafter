from emailtemplates import get_existing_templates
from mpdetails import get_mp_details

log = logging.getLogger("app")


def draftEmails(myname, postcode, address):
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
        success = e.fill(user)  # Returns true if successfully filled

        if success:
            # Append successful templates to the list we return
            filled_email_templates.append(e)
        else:
            log.debug("Failed to fill template, subject: {}".format(e.subject))
            pass

    return filled_email_templates
