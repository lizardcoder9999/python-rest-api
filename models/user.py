import pymongo
import bcrypt

#MONGO_SETUP##################################################################################################
client = pymongo.MongoClient('mongodb+srv://:!@cluster0.ffqsi.mongodb.net/curdapi?retryWrites=true&w=majority')
db = client['curdapi']
user_col = db['users']
admin_col = db['admin']
##############################################################################################################



class UserModel:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def find_by_email(cls,email):
        return user_col.find_one({"email":email})

    @classmethod 
    def find_apikey(cls,admin):
        admin = admin_col.find_one({"admin":admin})
        apikey = admin['api_key']
        return apikey

    def save_to_db(self):
        hashed_pass = bcrypt.hashpw(self.password.encode('utf-8'),bcrypt.gensalt())
        user_col.insert_one({"name":self.name,"email":self.email,"password":hashed_pass})


    
