from flask_restful import reqparse
from werkzeug.datastructures import FileStorage

validator = reqparse.RequestParser(bundle_errors=True)
validator.add_argument('title', type=str, required=True, help='type String, this argument is required')
validator.add_argument('sub_title', type=str, required=True, help='type String, this argument is required')
validator.add_argument('image', type=FileStorage, required=False, help='type File')
validator.add_argument('author', type=str, required=True, help='type String, this argument is required')
validator.add_argument('is_main_news', type=bool, required=True, help='type bool, this argument is required')
validator.add_argument('tags', type=dict, required=True, help='type Object, this argument is required')
validator.add_argument('news', type=str, required=True, help='type String, this argument is required')
validator.add_argument('fonts', action='append', required=True, help='type List, this argument is required')
