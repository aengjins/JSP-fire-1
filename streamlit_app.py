import streamlit as st
from PIL import Image
st.set_page_config(page_title="진주시 범죄안전지수", layout="wide")
st.title("⛑️안전한 진주 만들기(J.S.P)")
st.error("범죄 정보와 화재 정보를 이용해 안전한 진주 만들기")

tab1, tab2 = st.tabs(['범죄', '화재'])

with tab1:
    
    #이 파일은 멀티페이지에서 발표용으로 했습니다. 같은 zip파일에 필요한 이미지파일도 같이 들어있습니다.
    #그래도 복붙해서 써도 괜찮을겁니다.

    st.title("📍 J.S.P 범죄")

    # 열 생성
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown("""
        <div style='background-color: #f2f2f2; padding: 20px 25px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px; line-height: 1.7;'>

        <h4 style='margin-bottom: 15px;'>❗ 삐빅! 진주는 범죄 안전지수 <span style="color:red;">5등급</span>입니다.</h4>

        <ol>
        <li><strong>2024년 행정안전부가 발표한 지역안전지수</strong>에 따르면<br>
        진주시는 <strong>가장 낮은 안전등급인 5등급</strong>으로 분류되었습니다.</li><br>

        <li>오른쪽은 행정안전부가 발표한 <strong>전국 범죄안전지수 지도</strong>로,<br>
        진주시는 <strong style="color:red;">5등급 (범죄에 매우 취약한 지역)</strong>으로 표시되어 있습니다.</li><br>

        <li>해당 등급은 <strong>범죄 발생 가능성이 높은 지역</strong>으로 간주되며,<br>
        이에 저희는 <strong>범죄율과 어떤 요인이 관련이 있을까</strong>를 고민하게 되었고,<br>
        <strong>효과적인 범죄 예방 방안</strong>을 탐색하게 되었습니다.</li>
        </ol>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        image = Image.open("전국범죄위험등급.jpg")
        st.image(image, caption="2024년 지역안전지수 - 범죄 분야", width=400)



with tab2:
    st.markdown("### 🔥진주시 화재 발생 현황 (2019 ~ 2023년 기준)")
    st.markdown("""
                5년간 진주에서 발생한 화재는 1,353건으로, 연평균 약 270건에 달함.<br>
                계절별로 보면: <br>
                - 겨울철: 375건 (28.5%) - 가장 많은 빈도<br>
                - 봄: 346건<br>
                - 가을: 308건<br>
                - 여름: 302건<br><br>
                장소별로는 비주거시설(33.8%), 야외(25.2%), 주거시설(24.7%) 순.<br>
                주요 원인은 부주의(47.9%), 전기적 요인(14.6%), 원인 미상(14.4%)<br><br>
                """, unsafe_allow_html=True)
    st.markdown("### 📍 경남·전국 대비 진주시 비중")
    st.markdown("""
                - 경남도 전체(2022년 기준): 화재 3,017건<br>
                    → 진주가 차지하는 비율은 (연평균 270 / 총 3,017·(진주 대비 인구 비중으로 조정 안됨)), 대략 9% 내외 추정<br>
                - 전국(2022년 기준): 전국 화재는 약 40,112건,<br>
                    경남은 전국의 **7.5%**를 차지<br>
                    따라서 진주 역시 경남 평균과 비슷하거나 다소 높은 비중을 차지할 수 있음.
                """, unsafe_allow_html=True)
    st.markdown("### ✅ 결론")
    st.markdown("""
                - 진주는 경남도 평균 수준 이상의 화재 발생률을 보이며, 특히 겨울철과 비주거시설에서의 화재가 빈번함<br>
                - 전국 대비 경남 지역의 평균 화재 건수를 미루어 보면, 진주가 차지하는 비중은 상당히 높은 편
                """, unsafe_allow_html=True)