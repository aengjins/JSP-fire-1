import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

#제목
st.title("🔥 진주시 화재")
st.header("1. 진주시 화재 발생 정보")
#막대그래프 출력
df = pd.read_excel("진주시 화재 발생 정보(막대그래프).xlsx")

# 발화요인대분류별 빈도수 계산
cause_counts = df["발화요인대분류"].value_counts()

# 막대그래프 그리기
fig, ax = plt.subplots()
ax.bar(cause_counts.index, cause_counts.values, color='firebrick')
ax.set_xlabel("발화요인 대분류")
ax.set_ylabel("건수")
ax.set_title("발화요인 대분류에 따른 화재 발생 건수")
plt.xticks(rotation=45)

# Streamlit에 그래프 표시
st.pyplot(fig)