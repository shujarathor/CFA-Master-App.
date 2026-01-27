import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Professor G Companion", layout="wide")
st.title("📟 Professor G: CFA Master v1.5")

# 1. Create the Graph Data (AD/AS Model)
x = np.linspace(0, 10, 100)
ad = 10 - x  # Downward sloping AD
sras = x     # Upward sloping SRAS

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=ad, name='AD', line=dict(color='blue', width=4)))
fig.add_trace(go.Scatter(x=x, y=sras, name='SRAS', line=dict(color='red', width=4)))
fig.add_vline(x=5, line_width=3, line_dash="dash", line_color="green", name="LRAS")

fig.update_layout(title='Figure 1: AD/AS Equilibrium',
                  xaxis_title='Real GDP (Y)',
                  yaxis_title='Price Level (P)',
                  showlegend=True, height=400)

# 2. Display the App
col1, col2 = st.columns([1, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Topic: Economics - AD/AS")
    st.write("**Scenario:** The government significantly increases corporate tax rates.")
    
    user_choice = st.radio("Select the correct shift:", [
        "AD shifts to the left",
        "SRAS shifts to the right",
        "AD shifts to the right"
    ])

    if st.button("📡 Submit to Professor G"):
        if user_choice == "AD shifts to the left":
            st.success("✔️ CORRECT: Higher taxes reduce investment spending, shifting AD left.")
        else:
            st.error("❌ RE-CALIBRATE: Think about business investment incentives.")
