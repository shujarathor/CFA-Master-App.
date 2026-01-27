import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: CFA Study Portal", layout="wide")

# --- INITIALIZATION (The Database) ---
if 'db' not in st.session_state:
    st.session_state.db = []
if 'scores' not in st.session_state:
    st.session_state.scores = {"Correct": 0, "Total": 0}
if 'notes' not in st.session_state:
    st.session_state.notes = ""

# --- SIDEBAR: PERFORMANCE & TOOLS ---
st.sidebar.title("📊 Study Dashboard")
st.sidebar.metric("Accuracy", f"{(st.session_state.scores['Correct']/st.session_state.scores['Total']*100 if st.session_state.scores['Total'] > 0 else 0):.1f}%")
st.sidebar.write(f"Questions Attempted: {st.session_state.scores['Total']}")

if st.sidebar.button("🔄 Reset All Progress"):
    st.session_state.scores = {"Correct": 0, "Total": 0}
    st.session_state.db = []
    st.rerun()

# --- MAIN INTERFACE ---
tabs = st.tabs(["📝 Practice Quiz", "🗂️ Flashcards", "📓 LOS Notes", "📈 Performance Review"])

# 1. PRACTICE QUIZ TAB
with tabs[0]:
    st.header("CFA Level 1 Exam Simulation")
    # Example Question Logic
    st.subheader("Topic: Ethics - Standard I(A) Knowledge of the Law")
    st.write("An analyst is covered by stricter local laws than the Code and Standards. Which should they follow?")
    
    choice = st.radio("Select Answer:", ["The Code and Standards", "The stricter local law", "The less strict law"])
    
    if st.button("📡 Submit to Professor G"):
        st.session_state.scores["Total"] += 1
        if choice == "The stricter local law":
            st.success("✔️ CORRECT: You must follow the stricter of the two.")
            st.session_state.scores["Correct"] += 1
            st.session_state.db.append({"Topic": "Ethics", "Status": "Correct"})
        else:
            st.error("❌ INCORRECT: Always adhere to the stricter law.")
            st.session_state.db.append({"Topic": "Ethics", "Status": "Incorrect"})

# 2. LOS NOTES TAB
with tabs[2]:
    st.header("LOS Study Notes")
    st.info("Generating notes for: LOS 1.a - Describe the structure of the CFA Institute Professional Conduct Program.")
    new_note = st.text_area("Add your observations here:", placeholder="Type insights from our chat here...")
    if st.button("💾 Save to Study Guide"):
        st.session_state.notes += f"\n- {new_note}"
        st.toast("Note Saved!")
    st.markdown("### Your Compiled Study Guide")
    st.write(st.session_state.notes)

# 3. PERFORMANCE REVIEW TAB
with tabs[3]:
    st.header("Session History")
    if st.session_state.db:
        df = pd.DataFrame(st.session_state.db)
        st.table(df)
    else:
        st.write("No questions attempted yet.")
