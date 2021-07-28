from flask import Flask
from flask_cors import CORS
from routes import api
from models import db
from routes.news_routes import news_routes
import os

app = Flask(__name__)
app.register_blueprint(news_routes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)


@app.before_first_request
def start_db():
    db.create_all()


if __name__ == '__main__':
    api.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
