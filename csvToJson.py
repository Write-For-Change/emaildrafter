import csv
import json
import re
import pymongo

data = []


def appendCon(data):
    with open("mp_cons.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        lines = 0
        for row in csv_reader:
            if lines == 0:
                print(f'Column names are {", ".join(row)}')
                lines += 1
            else:
                firstname = row[1].strip()
                lastname = row[2].strip()
                fullName = firstname + " " + lastname
                con = row[4]
                for obj in data:
                    if obj["name"] == fullName:
                        obj["constituency"] = con
            lines += 1
    print(f"Processed {lines} lines.")


with open("mps_emails.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            firstname = row[0].strip()
            lastname = row[2].strip()
            fullName = firstname + " " + lastname
            email = row[3].strip()
            x = {"name": fullName, "email": email}
            data.append(x)
            line_count += 1
    print(f"Processed {line_count} lines.")
appendCon(data)

# Tell Python where to look for the database.
client = pymongo.MongoClient(
    "mongodb://heroku_b22mk7d6:mpdj7v335osvtda7c3g3ffo2ao@ds121565.mlab.com:21565/heroku_b22mk7d6?retryWrites=false"
)
# Define where the data is stored.
mpCollection = client["heroku_b22mk7d6"]["mp_email_list"]

# Execute the query on the mpCollection
mpDetails = mpCollection.insert_many(data)

with open("data.json", "w") as f:
    json.dump(data, f)
