import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import storage


class FileStorage:
    cred = credentials.Certificate("./my_credentials.json")
    app = firebase_admin.initialize_app(cred, {
        'storageBucket': 'news-storage-ea132.appspot.com'
    })

    def upload_file(self, file, content_type: str) -> str:
        date = datetime.datetime.now()
        file_blob = f'images/{int(date.timestamp() * 1000)}.{content_type.split("/")[1]}'
        bucket = storage.bucket()
        blob = bucket.blob(file_blob)
        blob.upload_from_file(file, content_type=content_type)
        blob.make_public()

        return f'https://storage.googleapis.com/news-storage-ea132.appspot.com/{file_blob}'

    def delete_file(self, url: str) -> None:
        bucket = storage.bucket()
        blob = bucket.blob(url.split('/')[-1])
        blob.delete()
