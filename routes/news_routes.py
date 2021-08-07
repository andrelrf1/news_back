from flask import Blueprint
from routes import api
from controllers.news_controller import ListNews, FindNews, CreateNews, DeleteNews, UpdateNews, UploadImage

news_routes = Blueprint('news_routes', __name__)

api.add_resource(ListNews, '/news')
api.add_resource(CreateNews, '/news/create')
api.add_resource(FindNews, '/news/find/<int:news_id>')
api.add_resource(DeleteNews, '/news/delete/<int:news_id>')
api.add_resource(UpdateNews, '/news/update/<int:news_id>')
api.add_resource(UploadImage, '/upload')
