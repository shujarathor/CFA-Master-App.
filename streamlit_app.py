import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: Ethics Mastery", layout="wide")

# --- 1. THE PERMANENT DATABASE ---
if 'master_db' not in st.session_state:
    st.session_state.master_db = {
        "Standard I": [], "Standard II": [], "Standard III": [],
        "Standard IV": [], "Standard V": [], "Standard VI": [], "Standard VII": []
    }
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = { "Standard I": [] }
if 'performance' not in st.session_state: st.session_state.performance = []
if 'los_notes' not in st.session_state: st.session_state.los_notes = ""
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'f_idx' not in st.session_state: st.session_state.f_idx = 0

# --- 2. SIDEBAR: NAVIGATION ---
st.sidebar.title("📟 Ethics Command Center")
selected_std = st.sidebar.selectbox("Select Standard", list(st.session_state.master_db.keys()))
diff_mode = st.sidebar.radio("Select Difficulty", ["Hard-Learning", "Above-Exam Level"])

if st.sidebar.button(f"🔄 Reset {selected_std} Progress"):
    st.session_state.q_idx = 0
    st.session_state.f_idx = 0
    st.rerun()

# --- 3. MAIN INTERFACE ---
tabs = st.tabs(["🎯 Practice Tank", "🗂️ Flashcard Deck", "📊 Performance Lab", "📓 LOS Notes"])

with tabs[0]: # PRACTICE TANK
    active_pool = [q for q in st.session_state.master_db[selected_std] if q['level'] == diff_mode]
    if not active_pool:
        st.info("Tank empty. Waiting for data drop...")
    elif st.session_state.q_idx >= len(active_pool):
        st.success("🏆 Module Complete!")
    else:
        q = active_pool[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1}")
        st.caption(f"Tag: {q['level']} | Focus: {q['focus']}")
        st.write(q['question'])
        choice = st.radio("Select Answer:", q['options'], key=f"q_{st.session_state.q_idx}")
        if st.button("📡 Submit Answer"):
            if choice == q['correct']:
                st.success(f"✔️ CORRECT: {q['rationale']}")
                st.session_state.performance.append({"Standard": selected_std, "Level": q['level'], "Result": "Pass"})
            else:
                st.error(f"❌ INCORRECT: {q['rationale']}")
                st.session_state.performance.append({"Standard": selected_std, "Level": q['level'], "Result": "Fail"})
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
        if col1.button("⬅️ Previous Card"):
            st.session_state.f_idx = max(0, st.session_state.f_idx - 1)
            st.rerun()
        if col2.button("Next Card ➡️"):
            st.session_state.f_idx = min(len(f_pool)-1, st.session_state.f_idx + 1)
            st.rerun()

with tabs[2]: # PERFORMANCE LAB
    st.header("Session Analytics")
    if st.session_state.performance:
        st.dataframe(pd.DataFrame(st.session_state.performance))
    else:
        st.write("Start practicing to see results.")

with tabs[3]: # LOS NOTES
    st.header("Personal Study Notes")
    note_input = st.text_area("Write your insights for this LOS:", value=st.session_state.los_notes, height=300)
    if st.button("💾 Save Notes"):
        st.session_state.los_notes = note_input
        st.toast("Notes Updated!")
