import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="CFA Ethics War Room", layout="wide")
st.title("🛡️ CFA Level 1: Ethics & GIPS")

# --- INITIALIZE SESSION STATE ---
if "score_history" not in st.session_state:
    st.session_state.score_history = []  # Stores 1 for correct, 0 for incorrect

if "mock_started" not in st.session_state:
    st.session_state.mock_started = False
if "mock_answers" not in st.session_state:
    st.session_state.mock_answers = {}  # Stores user answers for mock

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice Drills", "🗂️ Flashcards", "💀 Brutal Mock", "📈 Performance"])

# --- DROPDOWN MENU DATA ---
ethics_hierarchy = {
    "LM 1: Ethical Decision-Making": ["Framework Overview", "Identify Phase", "Consider Phase", "Act/Reflect Phase"],
    "Standard I: Professionalism": ["I(A) Knowledge of the Law", "I(B) Independence & Objectivity", "I(C) Misrepresentation", "I(D) Misconduct"],
    "Standard II: Integrity of Capital Markets": ["II(A) Material Nonpublic Info", "II(B) Market Manipulation"],
    "Standard III: Duties to Clients": ["III(A) Loyalty Prudence & Care", "III(B) Suitability", "III(C) Performance Presentation", "III(D) Confidentiality"],
    "Standard IV: Duties to Employers": ["IV(A) Loyalty", "IV(B) Additional Compensation", "IV(C) Responsibilities of Supervisors"],
    "Standard V: Investment Analysis": ["V(A) Diligence & Reasonable Basis", "V(B) Communication", "V(C) Record Retention"],
    "Standard VI: Conflicts of Interest": ["VI(A) Disclosure of Conflicts", "VI(B) Priority of Transactions", "VI(C) Referral Fees"],
    "Standard VII: Responsibility as CFA": ["VII(A) Conduct in Program", "VII(B) Reference to CFA Institute"],
    "Global Investment Performance Standards (GIPS)": ["GIPS Fundamentals", "GIPS Composite Construction", "GIPS Presentation & Reporting"]
}

# --- HELPER FUNCTION: NAVIGATION ---
def navigation_buttons(curr_idx, total_questions, session_key):
    col_prev, col_next = st.columns([1, 1])
    
    with col_prev:
        if st.button("⬅️ Previous", key=f"prev_{session_key}"):
            if curr_idx > 0:
                st.session_state[session_key] -= 1
                st.rerun()
            else:
                st.toast("You are at the first question.")

    with col_next:
        if st.button("Next ➡️", key=f"next_{session_key}"):
            if curr_idx < total_questions - 1:
                st.session_state[session_key] += 1
                st.rerun()
            else:
                st.toast("You have reached the end of this section!")

# --- TAB 1: PRACTICE DRILLS ---
with tab1:
    st.subheader("Targeted Practice")
    
    # Selection Menus
    main_selection = st.selectbox("1. Select Main Module:", list(ethics_hierarchy.keys()))
    sub_selection = st.selectbox("2. Select Sub-Topic:", ethics_hierarchy[main_selection])
    st.divider()
    difficulty = st.radio("Select Intensity:", ["Hard (Exam Level)", "Brutal (Above Exam)"], horizontal=True)
    
    # Load Data
    try:
        df = pd.read_csv("ethics_questions.csv")
    except FileNotFoundError:
        st.error("🚨 Error: 'ethics_questions.csv' not found.")
        st.stop()

    # Filter Data
    subset = df[
        (df["Module"] == main_selection) & 
        (df["SubTopic"] == sub_selection) & 
        (df["Difficulty"] == difficulty)
    ]

    if not subset.empty:
        session_key = f"idx_{sub_selection}_{difficulty}"
        if session_key not in st.session_state:
            st.session_state[session_key] = 0
        
        curr_idx = st.session_state[session_key]
        
        # Safety Check
        if curr_idx >= len(subset):
            curr_idx = 0
            st.session_state[session_key] = 0
            
        row = subset.iloc[curr_idx]
        
        st.info(f"**Question {curr_idx + 1} of {len(subset)}**")
        st.markdown(f"### {row['Question']}")
        
        # MAPPING LOGIC
        options_map = {
            row['OptionA']: 'OptionA',
            row['OptionB']: 'OptionB',
            row['OptionC']: 'OptionC'
        }
        
        options_text = list(options_map.keys())
        choice_text = st.radio("Select Answer:", options_text, key=f"rad_{session_key}_{curr_idx}")
        
        if st.button("Check Answer", key=f"check_{session_key}_{curr_idx}"):
            if choice_text in options_map:
                selected_label = options_map[choice_text]
                if selected_label == row['Answer']:
                    st.success("✅ Correct!")
                    st.session_state.score_history.append(1)
                else:
                    st.error(f"❌ Incorrect. The correct answer was: {row[row['Answer']]}")
                    st.session_state.score_history.append(0)
                st.markdown(f"**Explanation:** {row['Explanation']}")
            else:
                st.error("Error: Option mismatch. Please report this question.")
            
        st.divider()
        navigation_buttons(curr_idx, len(subset), session_key)

    else:
        st.warning(f"No questions found for **{sub_selection}** at **{difficulty}** level yet.")

# --- TAB 2: FLASHCARDS ---
with tab2:
    st.subheader("⚡ Rapid Fire Flashcards")
    
    st.caption(f"Showing Flashcards for: {sub_selection}")
    
    try:
        df_flash = pd.read_csv("ethics_flashcards.csv")
    except FileNotFoundError:
        st.error("🚨 Error: 'ethics_flashcards.csv' not found.")
        st.stop()
        
    # Filter Flashcards
    fc_subset = df_flash[
        (df_flash["Module"] == main_selection) & 
        (df_flash["SubTopic"] == sub_selection)
    ]
    
    if not fc_subset.empty:
        fc_key = f"fc_idx_{sub_selection}"
        if fc_key not in st.session_state:
            st.session_state[fc_key] = 0
            
        fc_idx = st.session_state[fc_key]
        
        # Safety Check
        if fc_idx >= len(fc_subset):
            fc_idx = 0
            st.session_state[fc_key] = 0
            
        fc_row = fc_subset.iloc[fc_idx]
        
        # Flashcard UI
        st.markdown(f"**Card {fc_idx + 1} of {len(fc_subset)}**")
        with st.container(border=True):
            st.markdown(f"## ❓ {fc_row['Front']}")
            if st.checkbox("Show Answer", key=f"reveal_{fc_key}_{fc_idx}"):
                st.markdown(f"## 💡 {fc_row['Back']}")
        
        st.divider()
        navigation_buttons(fc_idx, len(fc_subset), fc_key)
        
    else:
        st.info("No flashcards added for this specific topic yet.")

# --- TAB 3: BRUTAL MOCK ---
with tab3:
    st.subheader("💀 The Brutal Mock Exam")
    st.write("This is a 36-question simulated exam block. No immediate feedback. Score revealed at the end.")
    
    try:
        mock_df = pd.read_csv("ethics_mock.csv")
    except FileNotFoundError:
        st.error("🚨 Error: 'ethics_mock.csv' not found.")
        st.stop()
    
    # --- MOCK SELECTOR ---
    mock_choice = st.selectbox("Select Exam Version:", ["Exam 1", "Exam 2", "Exam 3"])
    
    # Filter for Selected Mock
    mock_subset = mock_df[mock_df["SubTopic"] == mock_choice]
    
    if st.button(f"🚀 Start {mock_choice}") or st.session_state.mock_started:
        st.session_state.mock_started = True
        
        with st.form("mock_form"):
            for idx, row in mock_subset.iterrows():
                st.markdown(f"**{idx + 1}. {row['Question']}**")
                
                options = [row['OptionA'], row['OptionB'], row['OptionC']]
                
                # Save answer to session state
                user_choice = st.radio(
                    "Choose:", 
                    options, 
                    key=f"mock_{idx}", 
                    index=None
                )
            
            submitted = st.form_submit_button("🏁 Submit Exam")
            
            if submitted:
                score = 0
                st.session_state.mock_started = False # Reset
                
                st.divider()
                st.subheader("📋 Results")
                
                for idx, row in mock_subset.iterrows():
                    user_ans = st.session_state.get(f"mock_{idx}")
                    correct_text = row[row['Answer']] 
                    
                    if user_ans == correct_text:
                        score += 1
                        st.caption(f"Question {idx+1}: ✅ Correct")
                    else:
                        st.caption(f"Question {idx+1}: ❌ Incorrect. (Answer: {correct_text})")
                        
                final_score = (score / len(mock_subset)) * 100
                st.metric("Final Score", f"{final_score:.1f}%")
                
                if final_score >= 70:
                    st.success("🎉 You PASSED this Mock Block!")
                else:
                    st.error("You failed this block. Review the weak areas.")

# --- TAB 4: PERFORMANCE ---
with tab4:
    st.subheader("📈 Your Performance")
    
    history = st.session_state.score_history
    if history:
        total_attempted = len(history)
        total_correct = sum(history)
        score_pct = (total_correct / total_attempted) * 100
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Attempted", total_attempted)
        col2.metric("Correct", total_correct)
        col3.metric("Accuracy", f"{score_pct:.1f}%")
        
        st.progress(score_pct / 100)
        
        if score_pct > 70:
            st.success("You are on track to pass!")
        else:
            st.warning("Target is 70%+")
            
        if st.button("Reset Stats"):
            st.session_state.score_history = []
            st.rerun()
    else:
        st.info("Attempt questions in the Practice Tab to see stats!")
