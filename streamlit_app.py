import streamlit as st

st.set_page_config(page_title="Professor G Companion", layout="centered")
st.title("📟 Professor G: CFA App v1.1")

st.info("System Online: Economics Module Loaded.")

# Text-only question for instant loading on iPad
st.subheader("Topic: Economics - AD/AS")
st.write("If the government significantly increases corporate tax rates, which of the following best describes the resulting shift?")

user_choice = st.radio("Select Option:", ["AD shifts to the left", "SRAS shifts to the right", "AD shifts to the right"])

if st.button("📡 Submit to Professor G"):
    if user_choice == "AD shifts to the left":
        st.success("✔️ CORRECT: Higher corporate taxes reduce investment spending, causing AD to shift left.")
    else:
        st.error("❌ RE-CALIBRATE: Try again! Think about how taxes affect business spending.")
