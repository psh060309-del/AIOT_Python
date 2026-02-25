import streamlit as st
import requests
import os
from google import genai
from dotenv import load_dotenv

# 1. 환경 변수 불러오기
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Gemini 클라이언트 설정
client = genai.Client(api_key=GEMINI_API_KEY)

# --- [추가] 대화 기록 초기화 로직 ---
# 처음 앱을 실행할 때 chat_history가 없으면 빈 리스트로 만들어줍니다.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 2. 날씨 정보를 가져오는 함수
def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric&lang=kr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        return temp, weather_desc
    else:
        return None, None

# 3. 웹 화면 구성
st.title("🌤️ 오늘 뭐 입지? AI 코디네이터")
st.write("대화 기록을 기억하는 AI 코디네이터입니다!")

# [추가] 사이드바에 대화 기록 초기화 버튼 생성
if st.sidebar.button("대화 기록 초기화"):
    st.session_state.chat_history = []
    st.rerun()

# 사용자 입력 받기
city = st.text_input("도시 이름을 영어로 입력해 주세요 (예: Seoul, Busan)")

if st.button("코디 추천받기"):
    if not OPENWEATHER_API_KEY:
        st.error("🚨 OpenWeatherMap API 키를 확인해 주세요.")
    elif city:
        with st.spinner("날씨 정보를 확인하고 코디를 고민 중입니다... 🤔"):
            temp, weather_desc = get_weather(city)
            
            if temp is not None:
                st.success(f"현재 **{city}**의 날씨는 **{weather_desc}**, 기온은 **{temp:.1f}°C** 입니다.")
                
                coordinator_instruction = """
                너는 트렌디하고 센스 있는 패션 코디네이터야. 
                사용자가 현재 기온과 날씨를 알려주면 코디를 제안해줘.
                이전 대화 내용을 기억하고 있으니 맥락에 맞춰서 대답해줘.
                말투는 항상 발랄하고 친절하게!
                """
                
                current_prompt = f"현재 날씨는 {weather_desc}이고, 기온은 {temp}도야. 오늘 어떻게 입고 나가는 게 좋을까?"
                
                # --- [중요: 에러 수정 구간] ---
                # 새로운 SDK 형식에 맞춰 dict 구조를 더 명확히 정의합니다.
                new_message = {"role": "user", "parts": [{"text": current_prompt}]}
                st.session_state.chat_history.append(new_message)

                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        config={
                            "system_instruction": coordinator_instruction
                        },
                        contents=st.session_state.chat_history 
                    )
                    
                    # AI 답변도 같은 형식으로 저장
                    ai_response_text = response.text
                    st.session_state.chat_history.append({"role": "model", "parts": [{"text": ai_response_text}]})
                    
                    st.write("### 👗 AI 코디네이터의 추천")
                    st.write(ai_response_text)
                    
                except Exception as e:
                    st.error(f"에러 발생: {e}")
            else:
                st.error("날씨 정보를 가져오지 못했습니다.")

# --- [추가] 화면 하단에 이전 대화 내용 보여주기 (선택 사항) ---
if st.session_state.chat_history:
    with st.expander("이전 대화 기록 보기"):
        for chat in st.session_state.chat_history:
            role = "나" if chat["role"] == "user" else "AI 코디네이터"
            st.write(f"**{role}**: {chat['parts'][0]}")