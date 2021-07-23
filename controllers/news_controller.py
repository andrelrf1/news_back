from flask_restful import Resource
from models.news_model import NewsModel
from polices.create_news_polices import validator as create_polices
import json


class CreateNews(Resource):
    def post(self):
        args = create_polices.parse_args()
        data = NewsModel(args['title'], args['sub_title'], args['img_url'] if 'img_url' in args.keys() else None,
                         args['author'], args['is_main_news'], json.dumps(args['tags']), args['news'],
                         json.dumps(args['fonts']))
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
    def post(self):
        pass


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
