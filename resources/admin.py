from flask_restful import Resource,reqparse
from models.admin import AdminModel
import bcrypt


class AddAdmin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('adminusername',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('password',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('admin',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('adminkey',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('api_key',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )


    def post(self):
        data = AddAdmin.parser.parse_args()

        if AdminModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            add_admin = AdminModel(data['adminusername'],data['adminkey'],data['password'])
            add_admin.save_to_db()
            return {"message":"success"},201



class DeleteAdmin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('adminusername',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('api_key',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('admin',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )


    def delete(self):
        data = DeleteAdmin.parser.parse_args()

        if AdminModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else: 
            AdminModel.delete_admin(data['adminusername'])
            return {"message":"deleted"},202


class AdminLogin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('adminusername',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('admin',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('api_key',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('password',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    def get(self):

        data = AdminLogin.parser.parse_args()

        if AdminModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            if AdminModel.find_by_username(data['adminusername']) is None:
                return {"message":"admin does not exist"},401

            else:
                login_admin = AdminModel.find_by_username(data['adminusername'])

                if login_admin: 
                    if bcrypt.checkpw(data['password'].encode('utf-8'),login_admin['password']) == True:
                        return {"message":"authorized"},200

                    else:
                        return {"message":"unauthorized"},403


class AdminUpdate(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('adminusername',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('api_key',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('admin',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )
    
    parser.add_argument('adminkey',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('password',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    def put(self):
        data = AdminUpdate.parser.parse_args()
        if AdminModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            AdminModel.update_admin(data['adminusername'],data['adminkey'],data['password'])
            return {"message":"updated"},202


    
    





            

