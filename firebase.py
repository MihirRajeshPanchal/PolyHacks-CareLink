import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("polyhacks-299d5-firebase-adminsdk-tg434-02fe9c85ca.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'polyhacks').document(u'login')
doc_ref.delete()
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })