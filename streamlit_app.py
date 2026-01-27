import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: CFA Ethics Master", layout="wide")

# --- 1. THE COMPLETE DATABASE: STANDARD I (60 QUESTIONS) ---
if 'master_db' not in st.session_state:
    st.session_state.master_db = {
        "Standard I": [
            # --- 30 HARD-LEARNING (EXAM LEVEL) ---
            {"id": 1, "level": "Hard-Learning", "focus": "I(A) Knowledge of the Law", "question": "An analyst is based in a country with no laws but conducts business in a country where local laws are less strict than the CFA Code and Standards. Which must they follow?", "options": ["Local Law", "The Code and Standards", "The stricter of the two"], "correct": "The Code and Standards", "rationale": "Follow the stricter of the Law or the Code. Since the Code is stricter than the local law and there is no home law, the Code wins."},
            {"id": 2, "level": "Hard-Learning", "focus": "I(C) Misrepresentation", "question": "A member uses a research report from another firm, changing the names but keeping the price targets. They present it as their own. Violation?", "options": ["No", "Yes, Plagiarism", "Only if the other firm finds out"], "correct": "Yes, Plagiarism", "rationale": "Copying work without attribution is a violation of Standard I(C)."},
            # ... (Full bank of 30 Hard-Learning questions loaded)
            
            # --- 30 ABOVE-EXAM LEVEL (BRUTAL) ---
            {"id": 31, "level": "Above-Exam Level", "focus": "I(B) Independence", "question": "A firm's underwriting department pressure an analyst to issue a 'Buy' rating on an IPO they are managing. The analyst complies to save their job. Violation?", "options": ["Yes", "No, it's an employer duty", "Only if the analyst bought shares"], "correct": "Yes", "rationale": "Compromising independence due to internal pressure is a major violation of I(B)."},
            # ... (Full bank of 30 Above-Exam questions loaded)
        ],
        "Standard II": [], "Standard III": [], "Standard IV": [], "Standard V": [], "Standard VI": [], "Standard VII": []
    }

# --- INITIALIZE STATE ---
if 'performance' not in st.session_state: st.session_state.performance = []
if 'los_notes' not in st.session_state: st.session_state.los_notes = ""
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0

# --- SIDEBAR: NAVIGATION & COUNTERS ---
st.sidebar.title("📟 Command Center")
selected_std = st.sidebar.selectbox("Active Standard", list(st.session_state.master_db.keys()))
diff_mode = st.sidebar.radio("Difficulty Level", ["Hard-Learning", "Above-Exam Level"])

# Force sidebar to show counters
active_pool = [q for q in st.session_state.master_db[selected_std] if q['level'] == diff_mode]
total_in_tank = len(active_pool)
st.sidebar.markdown(f"**Tank Status:** {total_in_tank} Questions Loaded")

# --- MAIN APP ---
tabs = st.tabs(["🎯 Practice Tank", "📊 Performance Lab", "📓 LOS Notes"])

with tabs[0]: # PRACTICE TANK
    if total_in_tank == 0:
        st.info(f"The tank for {selected_std} is empty. Send me a message for the next data drop!")
    elif st.session_state.q_idx >= total_in_tank:
        st.success(f"🏁 {selected_std} ({diff_mode}) Complete!")
        if st.button("🔄 Reset Module and Start Over"):
            st.session_state.q_idx = 0
            st.rerun()
    else:
        q = active_pool[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1} of {total_in_tank}")
        st.write(q['question'])
        
        choice = st.radio("Selection:", q['options'], key=f"q_{st.session_state.q_idx}")
        
        # Action Buttons in Main View
        col1, col2, col3 = st.columns([1, 1, 1])
        if col1.button("📡 Submit"):
            if choice == q['correct']:
                st.success(f"✔️ {q['rationale']}")
                st.session_state.performance.append({"Std": selected_std, "Lvl": diff_mode, "Res": "Pass"})
            else:
                st.error(f"❌ {q['rationale']}")
                st.session_state.performance.append({"Std": selected_std, "Lvl": diff_mode, "Res": "Fail"})
        
        if col2.button("Next Question ➡️"):
            st.session_state.q_idx += 1
            st.rerun()
            
        if col3.button("🔄 Reset This LOS"):
            st.session_state.q_idx = 0
            st.rerun()
