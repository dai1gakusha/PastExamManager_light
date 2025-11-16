import streamlit as st

st.title("📘 PastExamManager Light (Demo)")
st.write("これはネット公開用のライト版です。")
st.write("生徒情報を含まない、安全なデモページです。")

st.markdown("---")
st.subheader("メニュー")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 成績デモ"):
        st.session_state["page"] = "score_demo"

with col2:
    if st.button("📝 英単語デモ"):
        st.session_state["page"] = "word_demo"

with col3:
    if st.button("📚 過去問デモ"):
        st.session_state["page"] = "exam_demo"


# ▼ ページ表示（今は仮）
page = st.session_state.get("page", None)

if page == "score_demo":
    st.markdown("## 📊 成績デモページ（準備中）")

elif page == "word_demo":
    st.markdown("## 📝 英単語デモページ（準備中）")

elif page == "exam_demo":
    st.markdown("## 📚 過去問デモページ（準備中）")