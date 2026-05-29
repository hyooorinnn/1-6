import streamlit as st
import random

# 1. 웹페이지 기본 설정 (가장 상단에 위치해야 오류가 안 납니다)
st.set_page_config(page_title="연애 코칭 AI 닥터", page_icon="💖", layout="centered")

# 2. 세션 상태(Session State) 초기화
# 버튼을 클릭해도 데이터가 날아가지 않도록 저장소를 만듭니다.
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "situation" not in st.session_state:
    st.session_state.situation = ""

# --- 앱 메인 타이틀 ---
st.title("💖 연애 코칭 AI 닥터")
st.write("당신의 연애 고민을 해결해 드립니다. 가장 쉬운 코칭 시스템!")
st.markdown("---")

# --- STEP 1: 사용자 이름 입력 ---
if st.session_state.step == 1:
    st.subheader("💡 먼저 당신에 대해 알려주세요.")
    name_input = st.text_input("당신의 이름(또는 닉네임)은 무엇인가요?", placeholder="예: 홍길동")
    
    if st.button("다음 단계로 이동 👉"):
        if name_input.strip() == "":
            st.warning("이름을 입력하셔야 코칭을 시작할 수 있어요!")
        else:
            st.session_state.user_name = name_input
            st.session_state.step = 2
            st.rerun()  # 화면을 새로고침하여 다음 스텝으로 이동

# --- STEP 2: 고민 유형 선택 ---
elif st.session_state.step == 2:
    st.subheader(f"✨ {st.session_state.user_name}님, 어떤 연애 고민이 있으신가요?")
    
    situation_list = [
        "선택하세요",
        "짝사랑하는 사람에게 자연스럽게 카톡 보내는 법",
        "소개팅 나가서 어색함을 깨는 대화 주제",
        "최근 연인과 자꾸 싸우는데 화해하는 법",
        "권태기 극복을 위한 신선한 데이트 추천"
    ]
    
    selected_sit = st.selectbox("현재 나의 상황은?", situation_list)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전으로"):
            st.session_state.step = 1
            st.rerun()
            
    with col2:
        if st.button("코칭 받기 🔮"):
            if selected_sit == "선택하세요":
                st.warning("고민 유형을 선택해 주세요!")
            else:
                st.session_state.situation = selected_sit
                st.session_state.step = 3
                st.rerun()

# --- STEP 3: 맞춤형 코칭 결과 출력 ---
elif st.session_state.step == 3:
    st.subheader("🔮 AI 연애 닥터의 맞춤 처방전")
    st.info(f"**{st.session_state.user_name}님의 고민:** {st.session_state.situation}")
    
    # 고민별 맞춤형 답변 데이터베이스 (딕셔너리 형태)
    coaching_responses = {
        "짝사랑하는 사람에게 자연스럽게 카톡 보내는 법": [
            "질문으로 끝나는 카톡을 보내세요! '오늘 날씨 진짜 좋던데 주말에 뭐 해요?'처럼 상대방이 답장하기 편한 가벼운 일상 질문이 좋습니다.",
            "상대방의 관심사를 활용하세요. SNS에 올라온 맛집이나 취미 사진을 보고 '여기 좋아 보이던데 어디예요?'라고 물어보는 것이 가장 자연스럽습니다."
        ],
        "소개팅 나가서 어색함을 깨는 대화 주제": [
            "음식, 여행, 최근 본 재미있는 밈(Meme) 이야기를 해보세요. 호불호가 갈리지 않고 누구나 쉽게 대화를 이어갈 수 있는 치트키 주제입니다.",
            "칭찬으로 시작하세요! '오늘 입으신 옷 색상이 정말 잘 어울리시네요' 같은 구체적이고 과하지 않은 칭찬은 긴장을 풀어줍니다."
        ],
        "최근 연인과 자꾸 싸우는데 화해하는 법": [
            "'너 때문에'가 아니라 '내 기분은 그랬어'라는 대화법(I-Message)을 쓰세요. 상대방을 비난하지 않고 내 감정을 먼저 전달하는 것이 핵심입니다.",
            "감정이 격해졌을 때는 30분만 시간을 갖고 감정을 가라앉힌 뒤 이야기하세요. 홧김에 하는 말은 후회만 남깁니다."
        ],
        "권태기 극복을 위한 신선한 데이트 추천": [
            "두 사람이 처음 만났던 장소나 첫 데이트 코스를 그대로 다시 가보세요. 잊고 있던 풋풋한 감정이 다시 살아날 거예요.",
            "공방 원데이 클래스, 실내 클라이밍 등 한 번도 같이 해보지 않은 '새로운 도전'을 함께 하며 도파민을 자극해 보세요!"
        ]
    }
    
    # 무작위로 하나의 조언을 선택해 출력
    advice = random.choice(coaching_responses[st.session_state.situation])
    
    st.success(f"📌 **핵심 코칭:** {advice}")
    
    # 응원 문구
    st.balloons() # 축하 효과 애니메이션
    
    if st.button("🔄 처음부터 다시 하기"):
        # 세션 초기화 후 1단계로 이동
        st.session_state.step = 1
        st.session_state.user_name = ""
        st.session_state.situation = ""
        st.rerun()
