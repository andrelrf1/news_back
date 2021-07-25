from typing import Union
from models import db


class NewsModel(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    sub_title = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.Text)
    author = db.Column(db.String(75), nullable=False)
    is_main_news = db.Column(db.Boolean, nullable=False)
    tags = db.Column(db.Text, nullable=False)
    news = db.Column(db.Text, nullable=False)
    fonts = db.Column(db.Text, nullable=False)

    def __init__(self, title: str, sub_title: str, img_url: str, author: str, is_main_news: bool, tags: str, news: str,
                 fonts: str):
        self.title = title
        self.sub_title = sub_title
        self.img_url = img_url
        self.author = author
        self.is_main_news = is_main_news
        self.tags = tags
        self.news = news
        self.fonts = fonts

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'sub_title': self.sub_title,
            'img_url': self.img_url,
            'author': self.author,
            'is_main_news': self.is_main_news,
            'tags': self.tags,
            'news': self.news,
            'fonts': self.fonts
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

    def save_news(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_news(self) -> None:
        db.session.delete(self)
        db.session.commit()
