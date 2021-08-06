import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./my_credentials.json')
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'news-storage-ea132.appspot.com'
})

db = firestore.client()
