from typing import Union
from models import db


class NewsModel(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    subtitle = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.Text)
    author = db.Column(db.String(75), nullable=False)
    is_main_news = db.Column(db.Boolean, nullable=False)
    theme = db.Column(db.String(20), nullable=False)
    news_format = db.Column(db.String(20), nullable=False)
    news = db.Column(db.Text, nullable=False)
    fonts = db.Column(db.Text, nullable=False)
    read_time = db.Column(db.Integer, nullable=False)

    def __init__(self, title: str, subtitle: str, img_url: str, author: str, is_main_news: bool, theme: str,
                 news_format: str, news: str, fonts: str, read_time: int):
        self.title = title
        self.subtitle = subtitle
        self.img_url = img_url
        self.author = author
        self.is_main_news = is_main_news
        self.theme = theme
        self.news_format = news_format
        self.news = news
        self.fonts = fonts
        self.read_time = read_time

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'img_url': self.img_url,
            'author': self.author,
            'is_main_news': self.is_main_news,
            'theme': self.theme,
            'format': self.news_format,
            'news': self.news,
            'fonts': self.fonts,
            'read_time': self.read_time
        }

    @classmethod
    def find_news(cls, news_id) -> Union['NewsModel', None]:
        news = cls.query.filter_by(id=news_id).first()
        if news:
            return news

        else:
            return None

    @classmethod
    def find_all(cls) -> list['NewsModel']:
        news = cls.query.all()
        return news

    @classmethod
    def find_main_news(cls) -> Union['NewsModel', None]:
        news = cls.query.filter_by(is_main_news=True).first()
        return news

    def save_news(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_news(self) -> None:
        db.session.delete(self)
        db.session.commit()
