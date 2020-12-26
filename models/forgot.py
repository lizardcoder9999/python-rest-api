import pymongo
import bcrypt
import os
import dotenv
import secrets
import datetime

#Mongo DB
client = pymongo.MongoClient(str(os.getenv('MONGODB_URI')))
db = client['curdapi']
token_col =db['tokens']


class ForgotModel:
    def __init__(self,username,token,time):
        self.username = username
        self.token = token
        self.time = time