import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import streamlit as st
import pandas as pd

# ✅ 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'       # 윈도우
# plt.rcParams['font.family'] = 'AppleGothic'       # 맥OS
plt.rcParams['axes.unicode_minus'] = False          # 마이너스 부호 깨짐 방지

# 🔽 데이터 불러오기
df = pd.read_excel("진주시 화재 발생 정보(막대그래프).xlsx")
cause_counts = df["발화요인대분류"].value_counts()

# 🔽 Streamlit 앱
st.title("🔥 진주시 화재")
st.header("1. 진주시 화재 발생 정보")

# 🔽 matplotlib 그래프 생성
fig, ax = plt.subplots()
ax.bar(cause_counts.index, cause_counts.values, color='firebrick')
ax.set_xlabel("발화요인 대분류")
ax.set_ylabel("건수")
ax.set_title("발화요인 대분류에 따른 화재 발생 건수")
plt.xticks(rotation=45)

# 🔽 그래프 출력
st.pyplot(fig)