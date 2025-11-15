import streamlit as st

st.title("📘 PastExamManager Light (Demo)")

st.write("これはネット公開用のライト版です。")
st.write("この画面がネット上で表示されていれば、公開は成功です。")

st.markdown("---")
st.subheader("今後の拡張メモ")
st.write(
    """
- ここに「過去問一覧」ボタンや、「成績デモ」ボタンを追加していきます。
- ページ分割（複数ページ構成）は、後で `pages/` フォルダと一緒に整えていきます。
"""
)