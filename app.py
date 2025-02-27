import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebaseの認証情報を設定（初回のみ実行）
if not firebase_admin._apps:
    cred = credentials.Certificate("demoapps-a5fd2-firebase-adminsdk-7bfjk-b480fa2850.json")
    firebase_admin.initialize_app(cred)

# Firestore に接続
db = firestore.client()

# タイトル
st.title("🍽 冷蔵庫の食材リスト")

# Firestore から食材データを取得
ingredients_ref = db.collection("ingredients")
ingredients = ingredients_ref.stream()

# UI に食材リストを表示
st.subheader("📌 現在の食材")
for ingredient in ingredients:
    data = ingredient.to_dict()
    st.write(f"🛒 {data['name']}（{data['quantity']}個）")

# 食材の追加フォーム
st.subheader("➕ 食材を追加")
new_ingredient = st.text_input("食材名を入力")
new_quantity = st.number_input("個数", min_value=1, step=1)

if st.button("追加"):
    if new_ingredient:
        # Firestore に新しい食材を追加
        db.collection("ingredients").add({"name": new_ingredient, "quantity": new_quantity})
        st.success(f"{new_ingredient} を追加しました！")
        # st.experimental_rerun()
        st.rerun()

# 食材の削除機能
st.subheader("🗑 食材を削除")
for ingredient in ingredients_ref.stream():
    data = ingredient.to_dict()
    doc_id = ingredient.id  # Firestore のドキュメントID

    if st.button(f"❌ {data['name']} を削除", key=doc_id):
        db.collection("ingredients").document(doc_id).delete()
        st.success(f"{data['name']} を削除しました！")
        # st.experimental_rerun()
        st.rerun()


