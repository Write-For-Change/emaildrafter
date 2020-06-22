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

Templates are now able to be submitted through the `/submit-template` endpoint.
Fields which will be automatically substituted are defined in `emailtemplates.py` as:

Placeholder | Filled with
---| ---
%YOURNAME| Name of the user of the site
%YOURADDRESS| Address of the user
%TONAME| Name of the recipient of the email
%CONSTITUENCY| Constituency of the MP (if applicable)

Submitted templates are validated (automatically) and moderated (by a human) before inclusion on the site.
