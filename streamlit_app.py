import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: Ethics Mastery", layout="wide")

# --- THE PERMANENT DATABASE ---
if 'master_db' not in st.session_state:
    # We will populate these lists with the data drops I send
    st.session_state.master_db = {
        "Standard I": [], "Standard II": [], "Standard III": [],
        "Standard IV": [], "Standard V": [], "Standard VI": [], "Standard VII": []
    }
if 'performance' not in st.session_state: st.session_state.performance = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0

# --- SIDEBAR: NAVIGATION ---
st.sidebar.title("📟 Ethics Command Center")
selected_std = st.sidebar.selectbox("Select Standard", list(st.session_state.master_db.keys()))
diff_mode = st.sidebar.radio("Select Difficulty", ["Hard-Learning", "Above-Exam Level"])

# Reset Module Button
if st.sidebar.button(f"🔄 Reset {selected_std}"):
    st.session_state.q_idx = 0
    st.toast(f"{selected_std} Progress Reset!")

# --- MAIN INTERFACE ---
tabs = st.tabs(["🎯 Practice Tank", "📊 Performance Lab", "📔 LOS Notes"])

with tabs[0]:
    # Filter questions by Standard and Difficulty
    active_pool = [q for q in st.session_state.master_db[selected_std] if q['level'] == diff_mode]
    
    if not active_pool:
        st.info(f"The tank for {selected_std} is empty. Paste the Data Drop into the code to begin.")
    elif st.session_state.q_idx >= len(active_pool):
        st.success("🏆 Module Complete! Use the sidebar to reset or change Standards.")
    else:
        q = active_pool[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1} of {len(active_pool)}")
        st.caption(f"Tag: {q['level']} | Focus: {q['focus']}")
        st.write(q['question'])
        
        choice = st.radio("Select Answer:", q['options'], key=f"q_{selected_std}_{st.session_state.q_idx}")
        
        if st.button("📡 Submit to Professor G"):
            if choice == q['correct']:
                st.success(f"✔️ CORRECT: {q['rationale']}")
                st.session_state.performance.append({"Standard": selected_std, "Level": q['level'], "Result": "Pass"})
            else:
                st.error(f"❌ INCORRECT: {q['rationale']}")
                st.session_state.performance.append({"Standard": selected_std, "Level": q['level'], "Result": "Fail"})
        
        if st.button("Next Question ➡️"):
            st.session_state.q_idx += 1
            st.rerun()

with tabs[1]:
    st.header("Performance Analytics")
    if st.session_state.performance:
        df = pd.DataFrame(st.session_state.performance)
        st.dataframe(df)
    else:
        st.write("No data yet. Start practicing in the Tank!")
