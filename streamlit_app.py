import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Professor G Companion", layout="wide")
st.title("📟 Professor G: CFA Master v1.6")

# --- SIDEBAR: GAME THEORY CONTROLS ---
st.sidebar.header("🕹️ Game Theory: Market Moves")
st.sidebar.write("Simulate player actions to see the shift:")

# Toggles for AD and AS shifts
ad_shift = st.sidebar.slider("Aggregate Demand (Government/Fed Move)", -3.0, 3.0, 0.0)
as_shift = st.sidebar.slider("Short-Run Supply (Energy/Wage Shock)", -3.0, 3.0, 0.0)

# --- GRAPH LOGIC ---
x = np.linspace(0, 10, 100)
ad_base = 10 - x
sras_base = x

# New Shifted Curves
ad_new = (10 + ad_shift) - x
sras_new = x - as_shift

fig = go.Figure()
# Static base lines for reference
fig.add_trace(go.Scatter(x=x, y=ad_base, name='Base AD', line=dict(color='lightgrey', dash='dot')))
fig.add_trace(go.Scatter(x=x, y=sras_base, name='Base SRAS', line=dict(color='lightgrey', dash='dot')))
# Dynamic lines that move with your sliders
fig.add_trace(go.Scatter(x=x, y=ad_new, name='Active AD', line=dict(color='blue', width=4)))
fig.add_trace(go.Scatter(x=x, y=sras_new, name='Active SRAS', line=dict(color='red', width=4)))

fig.update_layout(title='Interactive AD/AS Model', xaxis_title='Output (Y)', yaxis_title='Price (P)', height=500)

# --- DISPLAY ---
col1, col2 = st.columns([1.5, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("CFA Level 1: Economics Analysis")
    st.info("Goal: Simulate a 'Corporate Tax Increase.' (Move AD to the left)")
    
    st.write("**Scenario:** The government significantly increases corporate tax rates. Which shift occurred?")
    choice = st.radio("Selection:", ["AD shifts Left", "SRAS shifts Right", "AD shifts Right"])
    
    if st.button("📡 Submit to Professor G"):
        # Correct if choice is AD Left AND the slider is actually moved left
        if choice == "AD shifts Left" and ad_shift < 0:
            st.success("✔️ CORRECT: You simulated the shift perfectly. Higher taxes reduce investment.")
        else:
            st.error("❌ RE-CALIBRATE: Adjust the slider to the left to see the correct economic impact.")
