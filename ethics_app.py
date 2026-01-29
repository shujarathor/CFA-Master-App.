import streamlit as st
import pandas as pd

st.set_page_config(page_title="CFA Ethics War Room", layout="wide")
st.title("🛡️ CFA Level 1: Ethics & GIPS")

# --- INITIALIZE SESSION STATE ---
if "score_history" not in st.session_state:
    st.session_state.score_history = []  # Stores 1 for correct, 0 for incorrect

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice Drills", "🗂️ Flashcards", "💀 Brutal Mock", "📈 Performance"])

# --- DROPDOWN MENU DATA ---
# FIXED: III(A) removed the comma to match the CSV data structure
ethics_hierarchy = {
    "LM 1: Ethical Decision-Making": ["Framework Overview", "Identify Phase", "Consider Phase", "Act/Reflect Phase"],
    "Standard I: Professionalism": ["I(A) Knowledge of the Law", "I(B) Independence & Objectivity", "I(C) Misrepresentation", "I(D) Misconduct"],
    "Standard II: Integrity of Capital Markets": ["II(A) Material Nonpublic Info", "II(B) Market Manipulation"],
    "Standard III: Duties to Clients": ["III(A) Loyalty Prudence & Care", "III(B) Suitability", "III(C) Performance Presentation", "III(D) Confidentiality"],
    "Standard IV: Duties to Employers": ["IV(A) Loyalty", "IV(B) Additional Compensation", "IV(C) Responsibilities of Supervisors"],
    "Standard V: Investment Analysis": ["V(A) Diligence & Reasonable Basis", "V(B) Communication", "V(C) Record Retention"],
    "Standard VI: Conflicts of Interest": ["VI(A) Disclosure", "VI(B) Priority of Transactions", "VI(C) Referral Fees"],
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
            # Handle potential lookup errors if text doesn't match exactly
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
    st.subheader("💀 The Brutal Mock")
    st.warning("Mock Vault under construction. Please use Practice Tab for now.")

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
