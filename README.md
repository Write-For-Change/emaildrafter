# emaildrafter

An app to let people draft personalised emails for a good cause.

Didn't want to spam the chat more so DM me for access!!

# Getting set up

We're using **pre-commit hooks** to maintain consistent code formatting

You need **Python 3.6** or later.

1.  Create and activate a virtual environment (virtualenv):

        python -m venv venv
        . ./venv/bin/activate
        pip install wheel

2.  Install requisite packages into the virtualenv:

        pip install -r requirements.txt -r requirements-dev.txt
        pre-commit install

## The different `requirements` files

- requirements.txt: pinned dependencies (version number is specified)
- requirements-minimal.txt: unpinned dependencies (more loose, no strict version constraints)

  You should be able to recreate requirements.txt by running `pip install -r
  requirements-minimal.txt` and then `pip freeze` in a fresh virtualenv.

- requirements-dev.txt: pinned **additional** dependencies for a development environment (that aren't needed in production)
- requirements-dev-minimal.txt: unpinned equivalent

  Again, you can recreate requirements-dev.txt using the same commands as above
  on requirements-dev-minimal.txt.


## Email Template Structure

Some work needs to be done to make the template structure easy to use and scalable to many emails (a more complete ToDo list is on the GitHub Projects page). For now, the available fields which templates are able to use are provided below, simple [python formatting](https://pyformat.info/#getitem_and_getattr) is used to populate the email body from dictionary values.

User information (provided in the form on the landing page):

User Info | String for Template
---| ---
Name | `{u[name]}`
Postcode | `{u[postcode]}`


Information about the recipient of the email, either set by the template, or information about an MP retrieved automatically (the ward is set to `None` if the recipient is not an MP):


Target Info | String for Template
--- | ---
Name | `{t[name]}`
Email | `{t[email]}`
Ward (soon to be replaced with Constituency)| `{t[ward]}`
