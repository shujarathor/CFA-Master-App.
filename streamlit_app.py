import streamlit as st

st.set_page_config(page_title="Professor G Companion", layout="centered")
st.title("📟 Professor G: CFA Master v1.2")

# Sidebar for LOS Tracking
st.sidebar.header("Study Progress")
st.sidebar.progress(15) # Example: 15% through Economics

st.info("System Online: Advanced Visual Module Loaded.")

# Economics Question with Visual Context
st.subheader("Topic: Economics - AD/AS Equilibrium")

# This creates a professional 'Callout' to simulate where the graph would be
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Aggregate_Demand_and_Supply.svg/1200px-Aggregate_Demand_and_Supply.svg.png", caption="Figure 1: AD/AS Framework")

st.markdown("""
**Scenario:** The government significantly increases corporate tax rates. 
According to the AD/AS model, what is the most likely immediate impact?
""")

user_choice = st.radio("Select the correct shift:", [
    "AD shifts to the left, decreasing price level and output",
    "SRAS shifts to the right, increasing output",
    "AD shifts to the right, increasing price level"
])

if st.button("📡 Submit to Professor G"):
    if "AD shifts to the left" in user_choice:
        st.success("✔️ CORRECT: Higher taxes reduce investment spending, shifting AD left.")
        st.write("**Rationale:** This lead to a decrease in both real GDP and the price level.")
    else:
        st.error("❌ RE-CALIBRATE: Think about business investment incentives.")
