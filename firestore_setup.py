import firebase_admin
from firebase_admin import credentials, firestore

# Firebaseの認証情報を設定
cred = credentials.Certificate("demoapps-a5fd2-firebase-adminsdk-7bfjk-b480fa2850.json")
firebase_admin.initialize_app(cred)

# Firestoreに接続
db = firestore.client()

print("✅ Firestore に接続成功！")
