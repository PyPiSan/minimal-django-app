from pymongo import MongoClient


client = pymongo.MongoClient('connection_string')
db = client['db_name']