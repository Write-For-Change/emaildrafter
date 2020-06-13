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
    count = 1
    dept_array = []
    for department in cabinet_data.keys():
        department_dict = {}
        department_dict["_id"] = count
        department_dict["name"] = department
        department_dict["staff"] = cabinet_data[department]
        dept_array.append(department_dict)
        count += 1
    return dept_array


def get_db_id(cabinet_office):
    array = []
    for department, minister_list in cabinet_office.items():
        for minister in minister_list:
            department = {}
            try:
                id = mongo.get_one("mp_email_list", {"name": minister})["_id"]
            except:
                print("there has been an error with {}".format(minister))
                id = minister
            minister_list.remove(minister)
            minister_list.append(id)
    return cabinet_office


print(get_minister_names())

# mongo.insert_many("mp_cabinet",set_up_id(get_db_id(get_minister_names())))
