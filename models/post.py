import pymongo
import os
import dotenv

#MONGO_SETUP##################################################################################################
client = pymongo.MongoClient(str(os.getenv('MONGODB_URI')))
db = client['curdapi']
post_col = db['posts']
admin_col = db['admin']
##############################################################################################################


class PostModel:
    def __init__(self,title,author,text,image):
        self.title = title
        self.author = author
        self.text = text
        self.image = image

    @classmethod 
    def find_apikey(cls,admin):
        admin = admin_col.find_one({"admin":admin})
        apikey = admin['api_key']
        return apikey

    def save_to_db(self):
        post_col.insert_one({"title":self.title,"author":self.author,"text":self.text,"imagelink":self.image})


    @classmethod
    def delete_post(cls,title):
        post_col.delete_one({"title":title})
