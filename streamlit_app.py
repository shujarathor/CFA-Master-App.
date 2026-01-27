import streamlit as st

st.set_page_config(page_title="Professor G Companion", layout="centered")
st.title("📟 Professor G: CFA App v1.0")

if 'db' not in st.session_state:
    st.session_state.db = [
        {
            "id": 1,
            "topic": "Economics: AD/AS Equilibrium",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Aggregate_Demand_and_Supply.svg/1200px-Aggregate_Demand_and_Supply.svg.png",
            "q": "If the government significantly increases corporate tax rates, which of the following best describes the resulting shift?",
            "options": ["AD shifts to the left", "SRAS shifts to the right", "AD shifts to the right"],
            "correct": "AD shifts to the left",
            "rationale": "Higher corporate taxes reduce investment spending, causing AD to shift left."
        }
    ]

if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
curr = st.session_state.db[st.session_state.q_idx]

st.image(curr["img"], use_container_width=True)
st.subheader(f"Topic: {curr['topic']}")
st.write(curr["q"])

user_choice = st.radio("Select Option:", curr["options"])

if st.button("📡 Submit to Professor G"):
    if user_choice == curr["correct"]:
        st.success(f"✔️ CORRECT: {curr['rationale']}")
    else:
        st.error(f"❌ RE-CALIBRATE: {curr['rationale']}")
