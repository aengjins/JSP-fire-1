import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ✅ 윈도우 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 기호 깨짐 방지

# 🔽 제목
st.title("🔥 진주시 화재")
st.header("1. 진주시 화재 발생 정보")

# 🔽 데이터 불러오기
df = pd.read_excel("진주시 화재 발생 정보(막대그래프).xlsx")

# 🔽 발화요인 빈도수 집계
if "발화요인대분류" in df.columns:
    cause_counts = df["발화요인대분류"].value_counts()

    # 🔽 그래프 그리기
    fig, ax = plt.subplots()
    ax.bar(cause_counts.index, cause_counts.values, color='firebrick')
    ax.set_title("발화요인 대분류에 따른 화재 발생 건수")
    ax.set_xlabel("발화요인 대분류")
    ax.set_ylabel("건수")
    plt.xticks(rotation=45)

    # 🔽 Streamlit에 표시
    st.pyplot(fig)
else:
    st.warning("❗ '발화요인대분류' 컬럼을 찾을 수 없습니다.")