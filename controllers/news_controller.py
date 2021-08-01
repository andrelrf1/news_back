from flask_restful import Resource
from models.news_model import NewsModel
from polices.create_news_polices import validator as create_polices
from polices.update_news_polices import validator as update_polices
from storage.firebase_storage import FileStorage
import json


class CreateNews(Resource):
    def post(self):
        args = create_polices.parse_args(strict=True)
        result = None
        if 'image' in args.keys() and args['image'] is not None:
            storage = FileStorage()
            result = storage.upload_file(args['image'], args['image'].content_type)

        data = NewsModel(args['title'], args['subtitle'], result, args['author'], args['is_main_news'], args['theme'],
                         args['format'], args['news'], json.dumps(args['fonts']))
        data.save_news()

        return {'success': True}


class ListNews(Resource):
    def get(self):
        result = NewsModel.find_all()
        data = []

        for news in result:
            this_news = news.to_json()
            this_news['fonts'] = json.loads(this_news['fonts'])
            data.append(this_news)

        return {
            'success': True,
            'data': data
        }


class FindNews(Resource):
    def get(self, news_id):
        news = NewsModel.find_news(news_id)

        if news:
            this_news = news.to_json()
            this_news['fonts'] = json.loads(this_news['fonts'])

            return {
                'success': True,
                'data': this_news
            }

        return {
            'success': True,
            'data': None
        }


class UpdateNews(Resource):
    def put(self, news_id):
        args = update_polices.parse_args()
        news = NewsModel.find_news(news_id)
        if all([x is None for x in args.values()]):
            return {
                       'success': False,
                       'message': 'Nothing sent to update'
                   }, 400

        elif news:
            for item in args.keys():
                if args[item] is not None:
                    if item == 'image':
                        storage = FileStorage()
                        result = storage.upload_file(args['image'], args['image'].content_type)
                        news.img_url = result

                    elif item == 'fonts':
                        news.fonts = json.dumps(args['fonts'])

                    else:
                        setattr(news, item, args[item])

            news.save_news()
            return {
                'success': True
            }

        else:
            return {
                       'success': False,
                       'data': 'News not found'
                   }, 400


class DeleteNews(Resource):
    def delete(self, news_id):
        news = NewsModel.find_news(news_id)
        if news:
            news.delete_news()
            return {'success': True}

        else:
            return {
                       'success': False,
                       'message': 'news not found'
                   }, 400
