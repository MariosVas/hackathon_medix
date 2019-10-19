import pymongo




def main_search(params=""):
    client = pymongo.MongoClient(
        "mongodb+srv://marios:letmein345@cluster0-kondl.gcp.mongodb.net/test?retryWrites=true&w=majority")
    print("connected")
    db = client.get_database("MedixChallenge")
    print("got DB")
    patients = db.Patients
    print("got patients", patients)
    data = patients.find()
    print("counted documents", data)
    # if params == "":
    #     data = patients.find()
    # else:
    #     data = patients.find({'name': params})
    return data


