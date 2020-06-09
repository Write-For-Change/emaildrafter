import pymongo
import os
import re
from dotenv import load_dotenv


class myDb:
    """
    A class used to represent the MongoDB

    Attributes
    ----------
    client: pymongo.MongoClient
        A reference to the MongoDB client.
    uri: string
        The URL used for the MongoDB driver. This will be stored on the Heroku for prod and in an .env file for test.
    db_name: string
        The name of the database we are using.

    Methods
    -------
    get_db_uri()
        Returns the MongoDB URL.

    get_db_client()
        Returns the active MongoClient.

    get_db_collection(collection_name)
        Returns a reference to the specifield collection in the active client.

    get_one(collection, query)
        Returns a cursor containing all the items from the collection that match the query.
    """

    client = None
    uri = None
    db_name = None

    def __init__(self, uri=os.environ["MONGODB_URI"]):
        if self.uri == None:
            load_dotenv()
            self.uri = os.getenv("MONGODB_URI")
        self.client = pymongo.MongoClient(uri)
        self.db_name = re.findall("heroku_[a-z|1-9]*", self.uri)[0]

    def get_db_uri(self):
        return self.uri

    def get_db_client(self):
        if self.client == None:
            raise ValueError("You must set a URI")
        else:
            return self.client

    def get_db_collection(self, collection_name):
        if self.client == None:
            raise ValueError("You need to set a URI")
        else:
            return self.client[self.db_name][collection_name.replace(" ", "_")]

    def get_one(self, collection, query):
        return self.get_db_collection(collection).find_one(query)
