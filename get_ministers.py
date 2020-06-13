import urllib.request, json
import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
from database import myDb

cabinet_url = "https://members.parliament.uk/Government/Cabinet"

# Instantiate the db
mongo = myDb()


def get_minister_names():
    """
    This function will go to the parliament website, and get
    a dictionary of all the departments and its members.
    """
    cabinet_data = {}

    get_html = requests.get(cabinet_url)
    html = get_html.content
    soup = BeautifulSoup(html, "html.parser")
    minister_list = soup.select("#tab-pane > div > div")

    for minister in minister_list:
        department = minister.contents[1].text.strip()
        cabinet_data[department] = []

    for minister in minister_list:
        department = minister.contents[1].text.strip()
        cabinet_data[department].append(
            minister.contents[3]
            .contents[-2]
            .contents[3]
            .contents[1]
            .contents[1]
            .contents[1]
            .contents[3]
            .text.strip()
        )

    return cabinet_data


def get_db_id(cabinet_office):
    for department, minister_list in cabinet_office.items():
        for minister in minister_list:
            query = {"name": minister}
            id = myDb.get_one("mp_email_list", query)._id
            minister_list.remove(minister)
            minister_list.append(id)
    return cabinet_office


print(get_db_id(get_minister_names()))
