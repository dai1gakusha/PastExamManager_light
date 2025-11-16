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
    st.markdown("## 📊 成績デモページ")

    import pandas as pd

    try:
        df = pd.read_csv("data_demo/scores_demo.csv")
        st.write("### デモ成績一覧（CSV読込）")
        st.dataframe(df)
    except Exception as e:
        st.error(f"CSVの読込でエラーが発生しました: {e}")


elif page == "word_demo":
    st.markdown("## 📝 英単語デモページ")

    import pandas as pd
    import random

    df = pd.read_csv("data_demo/words_demo.csv")

    # 1問ランダムに出題
    q = df.sample(1).iloc[0]

    st.write(f"### 問題：{q['英単語']} の意味は？")

    choices = [q['選択肢1'], q['選択肢2'], q['選択肢3']]
    answer = q['正解']  # 正解番号

    # ラジオボタンで選択
    user = st.radio("選択肢", ['1. ' + choices[0], '2. ' + choices[1], '3. ' + choices[2]])

    if st.button("回答する"):
        selected = int(user[0])  # '1. ~'の最初の数字を取り出す
        if selected == answer:
            st.success("正解！")
        else:
            st.error(f"不正解… 正解は「{choices[answer-1]}」でした。")

elif page == "exam_demo":
    st.markdown("## 📚 過去問デモページ（準備中）")