from flask import Flask
from flask_cors import CORS
from routes import api
from routes.news_routes import news_routes
import os

app = Flask(__name__)
app.register_blueprint(news_routes)
CORS(app)

if __name__ == '__main__':
    api.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
