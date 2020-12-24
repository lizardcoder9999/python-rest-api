import pymongo
import bcrypt


#Mongo DB
client = pymongo.MongoClient('mongodb+srv://:@cluster0.ffqsi.mongodb.net/curdapi?retryWrites=true&w=majority')
db = client['curdapi']
admin_col = db['admin']


class AdminModel:
    def __init__(self,admin,api_key,password):
        self.admin = admin
        self.api_key = api_key
        self.password = password

    @classmethod
    def find_by_username(cls,admin):
        return admin_col.find_one({"admin":admin})

    def save_to_db(self):
        hashed_pass = bcrypt.hashpw(self.password.encode('utf-8'),bcrypt.gensalt())
        admin_col.insert_one({"admin":self.admin,"api_key":self.api_key,"password":hashed_pass})

    @classmethod
    def delete_admin(cls,admin):
        admin_col.delete_one({"admin":admin})

    @classmethod 
    def find_apikey(cls,admin):
        admin = admin_col.find_one({"admin":admin})
        apikey = admin['api_key']
        return apikey

    @classmethod
    def update_admin(cls,adminusername,adminkey,password):
        hashed_pass =  bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        query = {"admin":adminusername}
        updated_values = {"$set":{"admin":adminusername,"password":hashed_pass,"api_key":adminkey}}

        admin_col.update_one(query,updated_values)
