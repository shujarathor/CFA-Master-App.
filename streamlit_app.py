import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: Ethics Mastery", layout="wide")

# --- THE PERMANENT DATABASE ---
if 'master_db' not in st.session_state:
    st.session_state.master_db = {
        "Standard I": [], "Standard II": [], "Standard III": [],
        "Standard IV": [], "Standard V": [], "Standard VI": [], "Standard VII": []
    }
# Database for Flashcards
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = {
        "Standard I": [] # This will be populated by the Data Drop
    }

if 'performance' not in st.session_state: st.session_state.performance = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'f_idx' not in st.session_state: st.session_state.f_idx = 0

# --- SIDEBAR: NAVIGATION ---
st.sidebar.title("📟 Ethics Command Center")
selected_std = st.sidebar.selectbox("Select Standard", list(st.session_state.master_db.keys()))
diff_mode = st.sidebar.radio("Select Difficulty", ["Hard-Learning", "Above-Exam Level"])

if st.sidebar.button(f"🔄 Reset {selected_std} Progress"):
    st.session_state.q_idx = 0
    st.session_state.f_idx = 0
    st.rerun()

# --- MAIN INTERFACE ---
tabs = st.tabs(["🎯 Practice Tank", "🗂️ Flashcard Deck", "📊 Performance Lab"])

with tabs[0]: # PRACTICE TANK
    active_pool = [q for q in st.session_state.master_db[selected_std] if q['level'] == diff_mode]
    if not active_pool:
        st.info("Tank empty. Data Drop required.")
    elif st.session_state.q_idx >= len(active_pool):
        st.success("🏆 Module Complete!")
    else:
        q = active_pool[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1}")
        st.write(q['question'])
        choice = st.radio("Select Answer:", q['options'], key=f"q_{st.session_state.q_idx}")
        if st.button("📡 Submit"):
            if choice == q['correct']:
                st.success(f"✔️ {q['rationale']}")
                st.session_state.performance.append({"Standard": selected_std, "Result": "Pass"})
            else:
                st.error(f"❌ {q['rationale']}")
                st.session_state.performance.append({"Standard": selected_std, "Result": "Fail"})
        if st.button("Next Question ➡️"):
            st.session_state.q_idx += 1
            st.rerun()

with tabs[1]: # FLASHCARDS
    f_pool = st.session_state.flashcards.get(selected_std, [])
    if not f_pool:
        st.info("No flashcards loaded for this Standard.")
    else:
        card = f_pool[st.session_state.f_idx]
        st.subheader(f"Flashcard {st.session_state.f_idx + 1}")
        with st.expander("👁️ VIEW SCENARIO (Front)"):
            st.write(card['front'])
        with st.expander("🧠 VIEW REASONING (Back)"):
            st.info(card['back'])
        
        col1, col2 = st.columns(2)
        if col1.button("⬅️ Previous"):
            st.session_state.f_idx = max(0, st.session_state.f_idx - 1)
            st.rerun()
        if col2.button("Next ➡️"):
            st.session_state.f_idx = min(len(f_pool)-1, st.session_state.f_idx + 1)
            st.rerun()
