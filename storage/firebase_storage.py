import datetime
from firebase_admin import storage


class FileStorage:
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
        blob = bucket.blob(f'images/{url.split("/")[-1]}')
        blob.delete()
