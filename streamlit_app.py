import streamlit as st
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# ==============================================================================
# 1. CONFIGURATION & STYLE
# ==============================================================================
st.set_page_config(page_title="CFA Master System", layout="wide")

st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; font-weight: bold; background-color: #0052cc; color: white;}
    .stProgress > div > div > div > div {background-color: #0052cc;}
    div[data-testid="stExpander"] {background-color: #f8f9fa; border-radius: 10px; border: 1px solid #e0e0e0;}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. THE GRAPH ENGINE
# ==============================================================================
def get_chart(chart_type):
    fig = go.Figure()
    layout_args = dict(height=300, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor='rgba(0,0,0,0)')
    
    if chart_type == "elastic":
        x = np.linspace(0, 10, 100); y = 10 - 0.5 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#0052cc', width=4), name='Demand'))
        fig.update_layout(title="Elastic Demand", xaxis_title="Q", yaxis_title="P", **layout_args)
        
    elif chart_type == "inelastic":
        x = np.linspace(0, 5, 100); y = 10 - 2 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#d93025', width=4), name='Demand'))
        fig.update_layout(title="Inelastic Demand", xaxis_title="Q", yaxis_title="P", **layout_args)

    elif chart_type == "perfect_competition":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=[5]*100, mode='lines', line=dict(color='#0052cc', width=4), name='P=MR'))
        fig.update_layout(title="Perfect Competition (Price Taker)", xaxis_title="Q", yaxis_title="P", **layout_args)

    elif chart_type == "shift_right":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=10-x, mode='lines', line=dict(color='grey', dash='dot'), name='D'))
        fig.add_trace(go.Scatter(x=x, y=x, mode='lines', line=dict(color='black'), name='S1'))
        fig.add_trace(go.Scatter(x=x, y=x-2, mode='lines', line=dict(color='green', width=3), name='S2 (Shift)'))
        fig.update_layout(title="Supply Shift Right", xaxis_title="Q", yaxis_title="P", **layout_args)
        
    return fig

# ==============================================================================
# 3. THE DATA STRUCTURE (EMPTY FOR NOW)
# ==============================================================================
# WE WILL FILL THIS IN BLOCK 2, 3, 4...
library = {
    "Economics": {
        # PASTE LOS BLOCKS HERE LATER
    }
}

# ==============================================================================
# 4. STATE MANAGEMENT
# ==============================================================================
if 'history' not in st.session_state: st.session_state.history = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'checked' not in st.session_state: st.session_state.checked = False
if 'fc_flipped' not in st.session_state: st.session_state.fc_flipped = False
if 'm_idx' not in st.session_state: st.session_state.m_idx = 0
if 'm_score' not in st.session_state: st.session_state.m_score = 0

# ==============================================================================
# 5. THE INTERFACE
# ==============================================================================
st.sidebar.title("🧭 CFA Ecosystem")

# MODULE SELECTOR
if not library["Economics"]:
    st.warning("⚠️ Database Empty. Please Paste Data Blocks into 'library' dictionary.")
    st.stop()

los_keys = list(library["Economics"].keys())
# Filter out Mock from LOS dropdown
practice_keys = [k for k in los_keys if "MOCK" not in k]

if practice_keys:
    selected_los = st.sidebar.selectbox("Select LOS", practice_keys)
else:
    selected_los = None

# RESET BUTTON
if st.sidebar.button("🔄 Reset All"):
    for key in ['q_idx', 'score', 'checked', 'fc_flipped', 'm_idx', 'm_score']:
        if key in st.session_state: del st.session_state[key]
    st.rerun()

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice Questions", "🃏 Flashcards", "💀 Brutal Mock", "📊 Performance"])

# --- TAB 1: PRACTICE ---
with tab1:
    if selected_los:
        available_levels = [k for k in library["Economics"][selected_los].keys() if "Flashcard" not in k]
        level = st.radio("Difficulty", available_levels, horizontal=True)
        
        q_list = library["Economics"][selected_los][level]
        total = len(q_list)
        idx = st.session_state.q_idx
        
        if idx < total:
            q = q_list[idx]
            # Progress
            c1, c2 = st.columns([5,1])
            c1.progress((idx)/total)
            c2.markdown(f"**{st.session_state.score}/{total}**")
            
            # Content
            if "chart" in q: st.plotly_chart(get_chart(q['chart']), use_container_width=True)
            st.markdown(f"### Q{idx+1}: {q['q']}")
            choice = st.radio("Select:", q['opt'], key=f"q_{idx}")
            
            # Logic
            b1, b2 = st.columns(2)
            if b1.button("Check Answer"): st.session_state.checked = True
            
            if st.session_state.checked:
                if choice == q['ans']:
                    st.success(f"✅ Correct! \n\n{q['why']}")
                    if f"done_{idx}" not in st.session_state:
                        st.session_state.score += 1
                        st.session_state[f"done_{idx}"] = True
                else:
                    st.error(f"❌ Wrong. Answer: {q['ans']} \n\n{q['why']}")
                
                if b2.button("Next ➡️"):
                    st.session_state.q_idx += 1
                    st.session_state.checked = False
                    st.rerun()
        else:
            st.balloons()
            st.success("Module Complete!")
            # Save to History
            st.session_state.history.append({
                "Time": datetime.now().strftime("%H:%M"), 
                "Module": selected_los, 
                "Score": f"{st.session_state.score}/{total}"
            })

# --- TAB 2: FLASHCARDS ---
with tab2:
    if selected_los and "Flashcards (10 Cards)" in library["Economics"][selected_los]:
        fc_deck = library["Economics"][selected_los]["Flashcards (10 Cards)"]
        fc_idx = st.session_state.get("fc_idx", 0)
        
        if fc_idx < len(fc_deck):
            card = fc_deck[fc_idx]
            with st.container(border=True):
                st.caption(f"Card {fc_idx+1}/{len(fc_deck)}")
                if not st.session_state.fc_flipped:
                    st.markdown(f"## {card['q']}")
                    if st.button("Flip 🔄"): st.session_state.fc_flipped = True; st.rerun()
                else:
                    st.markdown(f"## {card['ans']}")
                    st.info(card['why'])
                    if st.button("Next Card ➡️"): 
                        st.session_state.fc_idx = fc_idx + 1
                        st.session_state.fc_flipped = False
                        st.rerun()
        else:
            st.button("Restart Deck", on_click=lambda: st.session_state.update({"fc_idx":0}))

# --- TAB 3: MOCK EXAM ---
with tab3:
    st.header("💀 The 300-Question Mock")
    if "MOCK EXAM" in library["Economics"]:
        mock_qs = library["Economics"]["MOCK EXAM"]["Full Mock"]
        m_idx = st.session_state.m_idx
        
        if m_idx < len(mock_qs):
            mq = mock_qs[m_idx]
            st.progress(m_idx/len(mock_qs))
            st.write(f"**Mock Q{m_idx+1}**")
            st.markdown(f"### {mq['q']}")
            m_choice = st.radio("Select:", mq['opt'], key=f"m_{m_idx}")
            
            if st.button("Submit Mock Answer"):
                if m_choice == mq['ans']: 
                    st.success("Correct")
                    st.session_state.m_score += 1
                else: 
                    st.error(f"Wrong. Answer: {mq['ans']}")
                
                if st.button("Next Mock Q"):
                    st.session_state.m_idx += 1
                    st.rerun()
        else:
            st.success(f"Mock Complete! Score: {st.session_state.m_score}/{len(mock_qs)}")

# --- TAB 4: PERFORMANCE ---
with tab4:
    if st.session_state.history:
        st.dataframe(st.session_state.history)
    else:
        st.info("No practice sessions completed yet.")
