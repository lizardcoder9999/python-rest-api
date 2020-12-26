from flask import Flask 
from flask_restful import Api 
from resources.user import UserLogin,UserRegister
from resources.post import AddPost,DeletePost
from resources.admin import AdminUpdate,AddAdmin,AdminLogin,DeleteAdmin
import os
import dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
app.config['TESTING'] = True
api = Api(app)


api.add_resource(UserRegister,'/v1/newuser') 
api.add_resource(UserLogin,'/v1/loginuser')
api.add_resource(AddPost,'/v1/addpost')
api.add_resource(DeletePost,'/v1/deletepost')
api.add_resource(AddAdmin,'/v1/admin/add')
api.add_resource(DeleteAdmin,'/v1/admin/delete')
api.add_resource(AdminLogin,'/v1/admin/adminlogin')
api.add_resource(AdminUpdate,'/v1/admin/adminupdate')





if __name__ == "__main__":
    app.run(port=4000,debug=True)