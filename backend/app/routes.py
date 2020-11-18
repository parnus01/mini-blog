from flask import jsonify
from app import app
from app.models import User, Blog as MyBlog
from flask import request
from flask_restful import Resource
from peewee import DoesNotExist
import base64
import hashlib


def validate_auth_token():
    token = request.headers['TEST-Token']
    return str(base64.b64decode(token), 'utf-8')


@app.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()

    username = req_data['username']
    password = req_data['password']

    if not username or not password:
        return jsonify({"msg": "Invalid request"}), 400

    try:
        user = User.get(User.username == username)
    except DoesNotExist:
        return jsonify({"msg": "Authorize fail"}), 401

    if hashlib.md5(password.encode('utf-8')).hexdigest() != user.password:
        return jsonify({"msg": "Invalid username or password"}), 403

    token = base64.b64encode(str(user.id).encode('utf-8'))
    return jsonify(
        {'success': True, 'token': str(token, 'utf-8')}
    ), 200


class BlogListResource(Resource):
    def get(self):
        def __clean_data(blog):
            return {
                'id': blog.id,
                'name': blog.name,
                'content': blog.content,
                'status': blog.status,
                'category': blog.category,
                'author': blog.author.username
            }

        query = MyBlog.select(
            MyBlog.id, MyBlog.name, MyBlog.content, MyBlog.status, MyBlog.category, User.username
        ).join(User, attr='author')

        result = [__clean_data(blog) for blog in query]
        return {'blogs': result}, 200

    def post(self):
        req = request.json
        author_id = validate_auth_token()
        MyBlog.create(name=req['name'],
                      content=req['content'],
                      catgory=req['category'],
                      status=req['status'],
                      author_id=author_id
                      )
        return {'success': True}, 200


class BlogResource(Resource):
    def delete(self, blog_id):
        author_id = validate_auth_token()
        blog = MyBlog[blog_id]

        if str(blog.author_id) != author_id:
            return jsonify({"msg": "Permission denied"}), 403
        return {'success': True},

    def put(self, blog_id):
        req = request.json
        author_id = validate_auth_token()
        blog = MyBlog[blog_id]

        if str(blog.author_id) != author_id:
            return jsonify({"msg": "Permission denied"}), 403

        blog = MyBlog[blog_id]
        blog.name = req['name']
        blog.content = req['content']
        blog.category = req['category']
        blog.status = req['status']
        blog.save()  # Execute the query, returning number of rows updated.

        return {'success': True},
