import pymongo





client = pymongo.MongoClient("mongodb+srv://marios:letmein345@cluster0-kondl.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
