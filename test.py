from pymongo import MongoClient

client = MongoClient('localhost', 27017) client = MongoClient
( "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
db = client.Kalro_db org = db.users org.insert_one(
{"firstname":"Doe","Secondname":"John","phonenumber":"0712345678"}) for
person in org.find(): print(person)