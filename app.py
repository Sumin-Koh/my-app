import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="공부 챌린지 앱", layout="centered")

st.title("📚 공부 챌린지 인증 앱")

# 세션 상태 초기화
if "logs" not in st.session_state:
    st.session_state.logs = []

# 챌린지 이름 및 사용자 이름 입력
st.sidebar.header("👤 사용자 정보")
username = st.sidebar.text_input("이름", key="username")
challenge = st.sidebar.text_input("챌린지 이름", value="7일 공부 인증 챌린지", key="challenge")

# 인증 입력 폼
st.header("✅ 오늘의 공부 인증")
with st.form("log_form"):
    today = datetime.date.today()
    date = st.date_input("날짜", today)
    subject = st.text_input("공부한 내용 (예: 수학 문제집 3장)")
    time_spent = st.number_input("공부 시간 (분)", min_value=0, step=5)
    submit = st.form_submit_button("인증하기")

    if submit:
        if username and subject:
            st.session_state.logs.append({
                "이름": username,
                "챌린지": challenge,
                "날짜": date.strftime("%Y-%m-%d"),
                "내용": subject,
                "시간(분)": time_spent
            })
            st.success("공부 인증이 완료되었습니다!")
        else:
            st.warning("이름과 공부한 내용을 입력해주세요.")

# 인증 내역 출력
st.header("📅 나의 인증 내역")
if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)
    st.dataframe(df.sort_values("날짜", ascending=False), use_container_width=True)
else:
    st.info("아직 인증 내역이 없습니다.")
