import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk


# 제목
st.title("🔥 진주시 화재")

tab1, tab2, tab3 = st.tabs(['화재 발생 정보', '비상소화장치', '문제 제시'])
with tab1:
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

with tab2:
    st.header("2. 진주시 비상 소화장치")
# 소화기 아이콘 정의
    ICON_URL = "https://i.postimg.cc/2jc0dcDK/fire-extinguisher-icon-cursor-32x32.png"

# 데이터 정의 (진주 비상 소화 장치)
    data = pd.DataFrame({
        'lat': [35.186973, 35.193525, 35.193956, 35.194058, 35.193629, 35.194087, 35.194413, 35.194561, 35.194345, 35.194707, 35.194976, 35.195263, 35.19485, 35.193816, 35.198762, 35.194143, 35.196067, 35.181216, 35.18379, 35.185007, 35.27549, 35.17059, 35.145915, 35.192003, 35.235063, 35.26434, 35.263328, 35.261892, 35.226602, 35.283471, 35.305003, 35.289305, 35.340751, 35.116731],
        'lon': [128.11661, 128.085195, 128.085071, 128.085805, 128.085644, 128.084908, 128.084785, 128.085414, 128.085532, 128.084664, 128.084567, 128.085322, 128.085498, 128.083967, 128.089517, 128.087345, 128.084445, 128.079159, 128.08881, 128.088449, 128.03109, 128.167451, 128.353869, 128.263979, 128.254845, 128.168969, 128.169231, 128.168459, 128.121389, 128.12142, 128.136347, 128.056208, 128.142771, 128.189791],
        'place': [f"연번 {i+1}" for i in range(34)]
    })

# 아이콘 정보 열 추가
    data["icon_data"] = None
    for i in data.index:
        data.at[i, "icon_data"] = {
            "url": ICON_URL,
            "width": 32,
            "height": 32,
            "anchorY": 32
    }

# pydeck 표시
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/navigation-day-v1",
        initial_view_state=pdk.ViewState(
            latitude=35.186973,
            longitude=128.11661,
            zoom=11
        ),
        layers=[
            pdk.Layer(
                type="IconLayer",
                data=data,
                get_icon="icon_data",
                get_position='[lon, lat]',
                get_size=4,
                size_scale=15,
                pickable=True
            )
        ],
        tooltip={"text": "{place}"}
    ))

with tab3:
    st.header("비닐하우스 화재 사고")
    st.write("https://www.gnnews24.kr/news/articleView.html?idxno=21304")