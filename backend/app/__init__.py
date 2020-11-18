from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

from app import routes
from app.routes import BlogListResource, BlogResource

api.add_resource(BlogListResource, '/api/blog')

api.add_resource(BlogResource, '/api/blog/<blog_id>')
