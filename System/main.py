import pymongo


def main_search(params=""):
    client = pymongo.MongoClient(
        "mongodb+srv://marios:qwertyuiop@cluster0-kondl.gcp.mongodb.net/medix?retryWrites=true&w=majority")

    db = client.get_database("medix")
    patients = db.mdx
    print("got patients", patients)
    data = patients.find_one()
    print("counted documents")
    print(data)
    print("done\n\n")
    # if params == "":
    #     data = patients.find()
    # else:
    #     data = patients.find({'name': params})

    return data


