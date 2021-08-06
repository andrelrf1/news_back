import datetime
from typing import Union
from models import db


class NewsModel:
    id: str = None
    title: str = None
    subtitle: str = None
    img_url: str = None
    author: str = None
    is_main_news: bool = None
    theme: str = None
    news_format: str = None
    news: str = None
    fonts: str = None
    read_time: int = None

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
    def find_news(cls, news_id: str) -> Union['NewsModel', None]:
        raw_news = db.collection('news').document(news_id).get()
        news_dict = raw_news.to_dict()
        if news_dict:
            news = NewsModel(news_dict['title'], news_dict['subtitle'], news_dict['img_url'], news_dict['author'],
                             news_dict['is_main_news'], news_dict['theme'], news_dict['format'], news_dict['news'],
                             news_dict['fonts'], news_dict['read_time'])
            news.id = news_id
            return news

        else:
            return None

    @classmethod
    def find_all(cls) -> list['NewsModel']:
        collection = db.collection('news')
        docs = collection.stream()
        list_news = []
        for raw_news in docs:
            news_dict = raw_news.to_dict()
            news = NewsModel(news_dict['title'], news_dict['subtitle'], news_dict['img_url'], news_dict['author'],
                             news_dict['is_main_news'], news_dict['theme'], news_dict['format'], news_dict['news'],
                             news_dict['fonts'], news_dict['read_time'])
            news.id = raw_news.id
            list_news.append(news)

        return list_news

    @classmethod
    def find_main_news(cls) -> Union['NewsModel', None]:
        raw_news = db.collection('news').where('is_main_news', '==', True).get()
        for i in raw_news:
            news_dict = i.to_dict()
            news = NewsModel(news_dict['title'], news_dict['subtitle'], news_dict['img_url'], news_dict['author'],
                             news_dict['is_main_news'], news_dict['theme'], news_dict['format'], news_dict['news'],
                             news_dict['fonts'], news_dict['read_time'])
            news.id = i.id
            return news

        else:
            return None

    def save_news(self) -> None:
        date = datetime.datetime.now()
        news = db.collection('news').document(f'{int(date.timestamp() * 1000)}' if self.id is None else self.id)
        news.set({
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
        })

    def delete_news(self) -> None:
        db.collection('news').document(self.id).delete()
