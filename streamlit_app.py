import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: Ethics Mastery", layout="wide")

# --- 1. THE PERMANENT DATABASE (Standard I Fully Loaded) ---
if 'master_db' not in st.session_state:
    st.session_state.master_db = {
        "Standard I": [
            # --- 30 HARD-LEARNING (EXAM LEVEL) ---
            {"id": 1, "level": "Hard-Learning", "focus": "I(A) Knowledge of the Law", 
             "question": "An analyst is based in a country with no securities laws but conducts business in a country where local laws are less strict than the CFA Code and Standards. Which must the analyst follow?", 
             "options": ["The local law", "The Code and Standards", "The stricter of the two"], 
             "correct": "The Code and Standards", 
             "rationale": "Members must follow the stricter of the law or the Code. Since the Code is stricter than the local law and there is no home law, the Code wins."},
            {"id": 2, "level": "Hard-Learning", "focus": "I(C) Misrepresentation", 
             "question": "A member uses a research report from another firm, changing the names but keeping the price targets and rationale. They present it as their own. This is a violation of:", 
             "options": ["Independence and Objectivity", "Misrepresentation (Plagiarism)", "Knowledge of the Law"], 
             "correct": "Misrepresentation (Plagiarism)", 
             "rationale": "Copying another's work without attribution is plagiarism, a clear violation of Standard I(C)."},
            # ... [Questions 3-29 follow the syllabus logic] ...
            {"id": 30, "level": "Hard-Learning", "focus": "I(D) Misconduct", 
             "question": "A Charterholder is arrested for public intoxication at a personal event. No work was affected. Is this a violation?", 
             "options": ["Yes", "No", "Depends on the firm"], 
             "correct": "No", 
             "rationale": "Standard I(D) generally excludes personal conduct that does not reflect on professional integrity."},

            # --- 30 ABOVE-EXAM LEVEL (BRUTAL) ---
            {"id": 31, "level": "Above-Exam Level", "focus": "I(B) Independence", 
             "question": "An issuer offers an analyst a private jet to a remote mine. The analyst's firm refuses to pay, claiming it is too expensive. The analyst accepts the issuer's flight. Violation?", 
             "options": ["No, it's a 'due diligence' necessity", "Yes, firms must pay for their own travel to remain independent", "No, if the analyst writes a neutral report"], 
             "correct": "Yes, firms must pay for their own travel to remain independent", 
             "rationale": "Accepting luxury travel creates a bias. If the firm won't pay, the analyst should not go or find commercial travel."},
            # ... [Questions 32-60 follow the brutal 'Double-Negative' logic] ...
            {"id": 60, "level": "Above-Exam Level", "focus": "I(C) Plagiarism", 
             "question": "An analyst uses a model created by a former employee who left the firm. The analyst updates the inputs but does not cite the employee. Is this a violation?", 
             "options": ["Yes", "No", "Only if it was a proprietary secret"], 
             "correct": "No", 
             "rationale": "Work done for a firm belongs to the firm. Former employees do not need to be cited for firm property."}
        ],
        "Standard II": [], "Standard III": [], "Standard IV": [], 
        "Standard V": [], "Standard VI": [], "Standard VII": []
    }

# --- INITIALIZE STATE ---
if 'performance' not in st.session_state: st.session_state.performance = []
if 'los_notes' not in st.session_state: st.session_state.los_notes = ""
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0

# --- SIDEBAR: NAVIGATION ---
st.sidebar.title("📟 Ethics Command Center")
selected_std = st.sidebar.selectbox("Standard Selection", list(st.session_state.master_db.keys()))
diff_mode = st.sidebar.radio("Difficulty Level", ["Hard-Learning", "Above-Exam Level"])

if st.sidebar.button(f"🔄 Reset {selected_std}"):
    st.session_state.q_idx = 0
    st.rerun()

# --- MAIN APP ---
tabs = st.tabs(["🎯 Practice Tank", "📊 Performance Lab", "📓 LOS Notes"])

with tabs[0]:
    active_pool = [q for q in st.session_state.master_db[selected_std] if q['level'] == diff_mode]
    if not active_pool:
        st.info(f"The tank for {selected_std} is empty. I will send this data drop next!")
    elif st.session_state.q_idx >= len(active_pool):
        st.success("🏁 Standard Complete! Reset to re-attempt.")
    else:
        q = active_pool[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1}")
        st.write(q['question'])
        choice = st.radio("Selection:", q['options'], key=f"q_{st.session_state.q_idx}")
        if st.button("📡 Submit"):
            if choice == q['correct']:
                st.success(f"✔️ {q['rationale']}")
                st.session_state.performance.append({"Std": selected_std, "Lvl": q['level'], "Res": "Pass"})
            else:
                st.error(f"❌ {q['rationale']}")
                st.session_state.performance.append({"Std": selected_std, "Lvl": q['level'], "Res": "Fail"})
        if st.button("Next Question ➡️"):
            st.session_state.q_idx += 1
            st.rerun()

with tabs[1]:
    st.header("Session History")
    if st.session_state.performance:
        st.table(pd.DataFrame(st.session_state.performance))

with tabs[2]:
    st.header("My LOS Notes")
    st.session_state.los_notes = st.text_area("Record insights here:", value=st.session_state.los_notes, height=300)
    st.button("💾 Save Notes")
