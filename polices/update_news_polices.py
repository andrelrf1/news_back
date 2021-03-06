from flask_restful import reqparse
from werkzeug.datastructures import FileStorage

validator = reqparse.RequestParser(bundle_errors=True)
validator.add_argument('title', type=str, help='type String')
validator.add_argument('subtitle', type=str, help='type String')
validator.add_argument('image', type=FileStorage, help='type File', location='files')
validator.add_argument('author', type=str, help='type String')
validator.add_argument('is_main_news', type=bool, help='type String')
validator.add_argument('theme', type=str, help='type String')
validator.add_argument('format', type=str, help='type String')
validator.add_argument('news', type=str, help='type String')
validator.add_argument('fonts', action='append', help='type List')
validator.add_argument('read_time', type=int, help='type int')
