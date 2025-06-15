import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🔥 진주시 화재")
st.header("1. 진주시 화재 발생 정보")

# 엑셀 파일 불러오기
df = pd.read_excel("진주시 화재 발생 정보(막대그래프).xlsx")

# 발화요인대분류별 빈도수 계산
cause_counts = df["발화요인대분류"].value_counts().reset_index()
cause_counts.columns = ["발화요인대분류", "건수"]  # plotly는 이 형식이 더 편리함

# Plotly 막대그래프 그리기
fig = px.bar(
    cause_counts,
    x="발화요인대분류",
    y="건수",
    title="발화요인 대분류에 따른 화재 발생 건수",
    labels={"발화요인대분류": "발화요인 대분류", "건수": "화재 발생 건수"},
    color="건수",
    color_continuous_scale="Reds"
)

fig.update_layout(xaxis_tickangle=-45)

# Streamlit에 그래프 출력
st.plotly_chart(fig)