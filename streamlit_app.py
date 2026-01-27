import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="CFA Ecosystem (iPad)", layout="centered")

# ==============================================================================
# 1. THE CONTENT VAULT (YOUR QUESTION BANK)
# ==============================================================================
# EDIT THIS SECTION TO ADD MORE QUESTIONS
library = {
    "Ethics": {
        "Standard I: Professionalism": {
            "Hard (Exam Level)": [
                {"q": "1. Analyst lives in 'No Law' country, works for 'Strict Law' firm, trades in 'Weak Law' country. Follow which?", "opt": ["Residence", "Firm's Home Law", "Weak Law"], "ans": "Firm's Home Law", "why": "I(A): Follow the strictest applicable law. Firm (Strict) > Code > No/Weak Law."},
                {"q": "2. Client offers a bonus for FUTURE performance. Requirement?", "opt": ["Disclosure", "Written Consent", "Verbal Consent"], "ans": "Written Consent", "why": "I(B): Additional comp for future work requires written consent from employer."},
                {"q": "3. Arrested for peaceful protest (civil disobedience). Violation?", "opt": ["Yes, I(D)", "No", "Only if convicted"], "ans": "No", "why": "I(D): Targets professional dishonesty. Civil disobedience does not reflect on integrity."},
                {"q": "4. Issuer pays for Commercial Flight to site. Policy allows. Violation?", "opt": ["Yes", "No", "Only if First Class"], "ans": "No", "why": "I(B): Modest travel is allowed if disclosed, though paying your own way is Best Practice."},
                {"q": "5. Supervisor fails to set up compliance system. Violation?", "opt": ["IV(C)", "I(A)", "I(B)"], "ans": "I(A)", "why": "I(A): Supervisors must assume responsibility for compliance."}
            ],
            "Hard ++ (Brutal)": [
                {"q": "1. Global: Citizen of Strict Law country, works in Weak Law, trades in No Law. Code is middle. Follow?", "opt": ["Strict (Home)", "Weak (Local)", "Code"], "ans": "Strict (Home)", "why": "I(A): If Home law > Code > Local, and you are a citizen, Home law applies."},
                {"q": "2. Firm pays for analyst to attend a lavish 'Educational' conference in Vegas. Violation?", "opt": ["Yes", "No", "Only if spouse comes"], "ans": "Yes", "why": "I(B): Lavish location/entertainment overshadows education. Independence threat."},
                {"q": "3. Analyst deletes emails that are under regulatory investigation. Violation?", "opt": ["I(D)", "I(C)", "V(C)"], "ans": "I(D)", "why": "I(D): Obstruction of justice/deceit. Also Record Retention violations."}
            ]
        },
        "Standard II: Integrity of Capital Markets": {
            "Hard (Exam Level)": [
                 {"q": "1. Trading on information overhead in a lift (Merger rumor). Violation?", "opt": ["II(A)", "No", "Mosaic"], "ans": "No", "why": "Overheard rumor is not 'Material Non-Public' if source is unknown/unreliable."},
                 {"q": "2. Using a 'Mosaic' of non-material non-public info + public info. Violation?", "opt": ["Yes", "No", "Only if profits"], "ans": "No", "why": "Mosaic Theory allows using non-material non-public info to form a conclusion."}
            ],
            "Hard ++ (Brutal)": []
        },
        "ETHICS FINAL MOCK": {
            "Full Mock (Hard++)": [
                {"q": "Mock Q1: ... (Paste 100 Qs here later)", "opt": ["A", "B", "C"], "ans": "A", "why": "..."}
            ]
        }
    },
    
    "Economics": {
        "Elasticity & Demand": {
            "Hard (Exam Level)": [
                 {"q": "1. Refer to Chart A (Elastic). Price drops, Revenue...?", "opt": ["Increases", "Decreases", "Same"], "ans": "Increases", "why": "Elastic Region: %Q > %P. Revenue UP.", "chart": "elastic"},
                 {"q": "2. Refer to Chart B (Inelastic). Good is likely...?", "opt": ["Luxury", "Necessity", "Substitute"], "ans": "Necessity", "why": "Inelastic = Consumers buy regardless of price.", "chart": "inelastic"}
            ],
            "Hard ++ (Brutal)": []
        },
        "ECONOMICS FINAL MOCK": {
            "Full Mock (Hard++)": []
        }
    }
}

# ==============================================================================
# 2. THE CHART ENGINE (Built-in)
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

# ==============================================================================
# 3. THE APP INTERFACE
# ==============================================================================
# CSS Styling to make it look like the "Gemini Widget"
st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 12px; height: 3em; font-weight: bold; background-color: #0052cc; color: white;}
    .stProgress > div > div > div > div {background-color: #0052cc;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🧭 CFA Ecosystem")

# --- HIERARCHY SELECTORS ---
# 1. Select Module
selected_module = st.sidebar.selectbox("1. Topic", list(library.keys()))

# 2. Select Sub-Topic
sub_topics = list(library[selected_module].keys())
selected_topic = st.sidebar.selectbox("2. Module", sub_topics)

# 3. Select Difficulty
difficulty_levels = list(library[selected_module][selected_topic].keys())
selected_diff = st.sidebar.radio("3. Intensity", difficulty_levels)

# --- LOAD QUIZ ---
quiz_data = library[selected_module][selected_topic][selected_diff]
session_key = f"{selected_module}-{selected_topic}-{selected_diff}"

# Session State Logic
if 'active_session' not in st.session_state or st.session_state.active_session != session_key:
    st.session_state.active_session = session_key
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.checked = False
    st.session_state.mistakes = []

# --- DISPLAY CARD ---
st.caption(f"{selected_module} > {selected_topic} > {selected_diff}")

if not quiz_data:
    st.info("🚧 Questions coming soon! Paste them in the 'library' dictionary in the code.")
    st.stop()

total = len(quiz_data)
idx = st.session_state.current_q

if idx < total:
    q = quiz_data[idx]
    
    # Progress Bar
    col1, col2 = st.columns([4,1])
    col1.progress((idx) / total)
    col2.markdown(f"**{st.session_state.score} / {total}**")
    
    # Chart Render
    if "chart" in q:
        st.plotly_chart(get_chart(q['chart']), use_container_width=True)

    # Question Text
    st.markdown(f"### Q{idx+1}: {q['q']}")
    
    # Options
    choice = st.radio("Select Answer:", q['opt'], key=f"q_{idx}")
    
    # Buttons
    c1, c2 = st.columns(2)
    if c1.button("Check Answer"):
        st.session_state.checked = True
        
    if st.session_state.checked:
        if choice == q['ans']:
            st.success(f"✅ Correct! \n\n{q['why']}")
            if f"scored_{idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"scored_{idx}"] = True
        else:
            st.error(f"❌ Incorrect. \n\n**Correct:** {q['ans']} \n\n**Rationale:** {q['why']}")
            # Save mistake
            if q not in st.session_state.mistakes: st.session_state.mistakes.append(q)
        
        if c2.button("Next Question ➡️"):
            st.session_state.current_q += 1
            st.session_state.checked = False
            st.rerun()

else:
    # --- SUMMARY SCREEN ---
    st.balloons()
    st.title("🏆 Module Complete")
    st.metric("Final Score", f"{st.session_state.score}/{total}")
    
    if st.session_state.mistakes:
        with st.expander("⚠️ Review Your Mistakes"):
            for m in st.session_state.mistakes:
                st.markdown(f"**Q:** {m['q']}")
                st.info(f"**Answer:** {m['ans']} | {m['why']}")
                st.markdown("---")
    
    if st.button("🔄 Restart"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.checked = False
        st.rerun()
