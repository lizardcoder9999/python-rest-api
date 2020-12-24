from flask_restful import Resource,reqparse
from models.user import UserModel
import bcrypt




class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('email',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )
    parser.add_argument('password',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('name',

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

   

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            if UserModel.find_by_email(data['email']):
                return {"Message": "A user with that email already exists"},400

            user = UserModel(data['name'],data['email'],data['password'])
            user.save_to_db()

            return {"message":"User succesfully registered"},201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('email',

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

    parser.add_argument('api_key',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    def get(self):
        data = UserLogin.parser.parse_args()

        if UserModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            if UserModel.find_by_email(data['email']) is None:
                return {"Message":"User does not exist"},401

            else:
                login_user = UserModel.find_by_email(data['email'])

                if login_user:
                    if bcrypt.checkpw(data['password'].encode('utf-8'),login_user['password']) == True:
                        return {"message":"authorized"},200
                    else:
                        return {"message":"unauthorized"},403


        
            

            

