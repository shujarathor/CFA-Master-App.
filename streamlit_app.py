import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Algo Clone", layout="centered")

# ==============================================================================
# 1. THE CONTENT HIERARCHY (The "Algo" Structure)
# ==============================================================================
# Structure: SECTION -> FOLDER -> DECK -> [Cards]
library = {
    "CFA Level 1 (The Section)": {
        "Ethics (The Folder)": {
            "Standard I - Hard (The Deck)": [
                {"q": "Analyst lives in No Law country, works for Strict Law firm. Follow which?", "ans": "Firm's Home Law (Strict)", "why": "I(A): Follow the strictest applicable law."},
                {"q": "Client offers bonus for FUTURE performance. Requirement?", "ans": "Written Consent", "why": "I(B): Future work requires written permission from employer."},
                {"q": "Arrested for peaceful protest. Violation?", "ans": "No", "why": "I(D): Civil disobedience does not reflect on professional integrity."},
                {"q": "Issuer pays for commercial flight. Violation?", "ans": "No", "why": "Allowed if disclosed, though paying your own way is best practice."},
                {"q": "Supervisor fails to set up compliance system. Violation?", "ans": "Yes (I(A))", "why": "Supervisors must assume responsibility for compliance."}
            ],
            "Standard I - Brutal (The Deck)": [
                 {"q": "Citizen of Strict Law, works in Weak Law, trades in No Law. Follow?", "ans": "Strict Law (Home)", "why": "I(A): Home law applies to citizens if stricter than local/Code."}
            ]
        },
        "Economics (The Folder)": {
            "Elasticity (The Deck)": [
                {"q": "Price drops, Revenue Increases. Elasticity is?", "ans": "Elastic", "why": "Quantity % change > Price % change.", "chart": "elastic"},
                {"q": "Steep Demand Curve. Good is likely a?", "ans": "Necessity", "why": "Inelastic demand.", "chart": "inelastic"}
            ]
        }
    }
}

# ==============================================================================
# 2. THE ENGINE
# ==============================================================================
def get_chart(chart_type):
    fig = go.Figure()
    if chart_type == "elastic":
        x = np.linspace(0, 10, 100); y = 10 - 0.5 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue', width=4)))
        fig.update_layout(title="Elastic Demand", height=250, margin=dict(l=20,r=20,t=30,b=20))
    elif chart_type == "inelastic":
        x = np.linspace(0, 5, 100); y = 10 - 2 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='red', width=4)))
        fig.update_layout(title="Inelastic Demand", height=250, margin=dict(l=20,r=20,t=30,b=20))
    return fig

# CSS to look like a Study App
st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 12px; height: 3em; font-weight: bold; background-color: #4a90e2; color: white;}
    div[data-testid="stExpander"] {background-color: #f5f7fa; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🗂️ Library")

# --- HIERARCHY SELECTORS ---
# 1. SECTION
selected_section = st.sidebar.selectbox("Section", list(library.keys()))
# 2. FOLDER
selected_folder = st.sidebar.selectbox("Folder", list(library[selected_section].keys()))
# 3. DECK
selected_deck = st.sidebar.selectbox("Deck", list(library[selected_section][selected_folder].keys()))

# LOAD DECK
deck = library[selected_section][selected_folder][selected_deck]
total = len(deck)

# SESSION STATE
session_key = f"{selected_section}-{selected_folder}-{selected_deck}"
if 'session_id' not in st.session_state or st.session_state.session_id != session_key:
    st.session_state.session_id = session_key
    st.session_state.idx = 0
    st.session_state.flipped = False # Track if card is flipped

idx = st.session_state.idx
card = deck[idx]

# --- THE INTERFACE ---
st.caption(f"{selected_section} / {selected_folder} / {selected_deck}")
st.progress((idx + 1) / total)

# TABS: STUDY MODE vs QUIZ MODE
mode = st.radio("Mode", ["Flashcard (Study)", "Quiz (Test)"], horizontal=True, label_visibility="collapsed")

if mode == "Flashcard (Study)":
    # --- FLASHCARD VIEW ---
    st.markdown("### 🃏 Flashcard")
    
    container = st.container(border=True)
    
    # FRONT OF CARD
    if not st.session_state.flipped:
        if "chart" in card:
            container.plotly_chart(get_chart(card['chart']), use_container_width=True)
        container.markdown(f"## {card['q']}")
        container.caption("Tap 'Flip' to see answer")
        
        if st.button("🔄 Flip Card"):
            st.session_state.flipped = True
            st.rerun()
            
    # BACK OF CARD
    else:
        container.markdown(f"## {card['ans']}")
        container.info(f"**Rationale:** {card['why']}")
        
        c1, c2 = st.columns(2)
        if c1.button("⬅️ Back to Front"):
            st.session_state.flipped = False
            st.rerun()
        if c2.button("Next Card ➡️"):
            if idx < total - 1:
                st.session_state.idx += 1
                st.session_state.flipped = False
                st.rerun()
            else:
                st.success("Deck Complete!")
                if st.button("Restart Deck"):
                    st.session_state.idx = 0
                    st.session_state.flipped = False
                    st.rerun()

else:
    # --- QUIZ VIEW (Original) ---
    st.markdown("### 📝 Quiz")
    if "chart" in card:
        st.plotly_chart(get_chart(card['chart']), use_container_width=True)
    st.write(f"**Q{idx+1}:** {card['q']}")
    
    with st.expander("Show Answer"):
        st.write(f"**Answer:** {card['ans']}")
        st.write(f"**Why:** {card['why']}")
    
    if st.button("Next Question"):
        if idx < total - 1:
            st.session_state.idx += 1
            st.rerun()
        else:
            st.success("Finished!")
