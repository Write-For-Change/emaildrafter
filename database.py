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

    get_all(collection):
        Returns a cursor pointing to all of the items in a collection.

    insert_one(collection,row):
        Inserts the row into the chosen collection.
    """

    client = None
    uri = None
    db_name = None

    def __init__(self, uri=None):
        if uri is None:
            load_dotenv()
            uri = os.getenv("MONGODB_URI")
        if not uri:
            raise ValueError(
                "MongoDB URI not provided to constructor nor specified in MONGODB_URI envvar"
            )
        self.uri = uri
        self.client = pymongo.MongoClient(self.uri)
        self.db_name = re.findall("heroku_[a-z|1-9]*", self.uri)[0]

    def get_db_uri(self):
        return self.uri

    def get_db_client(self):
        return self.client

    def get_db_collection(self, collection_name):
        return self.client[self.db_name][collection_name.replace(" ", "_")]

    def get_one(self, collection, query):
        return self.get_db_collection(collection).find_one(query)

    def get_all(self, collection):
        return self.get_db_collection(collection).find()

    def get_all_matching(self, collection, query):
        return self.get_db_collection(collection).find(query)

    def insert_one(self, collection, row):
        return self.get_db_collection(collection).insert_one(row)

    def update_one(self, collection, query, row):
        return self.get_db_collection(collection).replace_one(query, row)
