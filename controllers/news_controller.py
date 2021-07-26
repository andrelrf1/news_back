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

        data = NewsModel(args['title'], args['sub_title'], result, args['author'], args['is_main_news'],
                         json.dumps(args['tags']), args['news'], json.dumps(args['fonts']))
        data.save_news()

        return {'success': True}


class ListNews(Resource):
    def get(self):
        result = NewsModel.find_all()
        data = []

        for news in result:
            this_news = news.to_json()
            this_news['tags'] = json.loads(this_news['tags'])
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
            this_news['tags'] = json.loads(this_news['tags'])
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
        if args is None or len(args.keys()) == 0:
            return {
                'success': False,
                'message': 'Nothing sent to update'
            }

        elif news:
            for item in args.keys():
                if item == 'image':
                    pass
                elif item == 'tags':
                    news.tags = json.dumps(args['tags'])
                elif item == 'fonts':
                    json.dumps(args['fonts'])
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
