from flask_restful import reqparse
from werkzeug.datastructures import FileStorage

validator = reqparse.RequestParser(bundle_errors=True)
validator.add_argument('title', type=str, required=True, help='title argument is required')
validator.add_argument('sub_title', type=str, required=True, help='subtitle argument is required')
validator.add_argument('image', type=FileStorage, required=False, help='file argument is required')
validator.add_argument('author', type=str, required=True, help='author argument is required')
validator.add_argument('is_main_news', type=bool, required=True, help='is_main_news argument is required')
validator.add_argument('tags', action='append', required=True, help='tags argument is required')
validator.add_argument('news', type=str, required=True, help='news argument is required')
validator.add_argument('fonts', action='append', required=True, help='fonts argument is required')
