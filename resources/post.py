from flask_restful import Resource,reqparse
from models.post import PostModel


class AddPost(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('author',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )

    parser.add_argument('text',

    type = str,
    required= True,
    help = "This field cannot be empty"

    )
    parser.add_argument('image',

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
        data = AddPost.parser.parse_args()

        if PostModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            data = AddPost.parser.parse_args()

            add_post = PostModel(data['title'],data['author'],data['text'],data['image'])
            add_post.save_to_db()

            return {"message":"success"},201


class DeletePost(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',

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

    def delete(self):
        data = DeletePost.parser.parse_args()

        if PostModel.find_apikey(data['admin']) != data['api_key']:
            return {"message":"unauthorized request"},403

        else:
            data = DeletePost.parser.parse_args()
            PostModel.delete_post(data['title'])
            return {"message":"deleted"},202



        

