import streamlit as st

# --- ETHICS DATABASE STRUCTURE ---
# We use a dictionary where keys are the Main Standards and values are lists of Sub-Standards.
ethics_hierarchy = {
    "LM 1: Ethical Decision-Making": ["Framework Overview", "Identify Phase", "Consider Phase", "Act/Reflect Phase"],
    "Standard I: Professionalism": ["I(A) Knowledge of the Law", "I(B) Independence & Objectivity", "I(C) Misrepresentation", "I(D) Misconduct"],
    "Standard II: Integrity of Capital Markets": ["II(A) Material Nonpublic Info", "II(B) Market Manipulation"],
    "Standard III: Duties to Clients": ["III(A) Loyalty, Prudence & Care", "III(B) Suitability", "III(C) Performance Presentation", "III(D) Confidentiality"],
    "Standard IV: Duties to Employers": ["IV(A) Loyalty", "IV(B) Additional Compensation", "IV(C) Responsibilities of Supervisors"],
    "Standard V: Investment Analysis": ["V(A) Diligence & Reasonable Basis", "V(B) Communication", "V(C) Record Retention"],
    "Standard VI: Conflicts of Interest": ["VI(A) Disclosure", "VI(B) Priority of Transactions", "VI(C) Referral Fees"],
    "Standard VII: Responsibility as CFA": ["VII(A) Conduct in Program", "VII(B) Reference to CFA Institute"],
    "LM 4: Introduction to GIPS": ["GIPS Objectives", "GIPS Compliance Claims", "GIPS Nine Sections"]
}

st.set_page_config(page_title="CFA Ethics War Room", layout="wide")
st.title("🛡️ CFA Level 1: Ethics & GIPS")

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📝 Practice Drills", "🗂️ Flashcards", "💀 Brutal Mock"])

with tab1:
    st.subheader("Targeted Practice")
    
    # DOUBLE DROPDOWN LOGIC
    # Dropdown 1: The Main Module
    main_selection = st.selectbox("1. Select Main Module:", list(ethics_hierarchy.keys()))
    
    # Dropdown 2: The Specific LOS / Sub-Standard (Dynamically updates based on Dropdown 1)
    sub_selection = st.selectbox("2. Select Sub-Topic:", ethics_hierarchy[main_selection])
    
    st.divider()
    
    difficulty = st.radio("Select Intensity:", ["Hard (Exam Level)", "Brutal (Above Exam)"], horizontal=True)
    
    st.info(f"Currently Drilling: **{sub_selection}**")

# --- PLACEHOLDERS FOR DATA ---
# We will populate these keys as we generate questions
if "questions" not in st.session_state:
    st.session_state.questions = {} 

# --- QUESTION DATABASE ---
if "ethics_db" not in st.session_state:
    st.session_state.ethics_db = {
        "LM 1: Ethical Decision-Making": {
            "Framework Overview": {
                "Hard (Exam Level)": [
                    {
                        "question": "Which of the following is the final step in the Ethical Decision-Making Framework defined by the CFA Institute?",
                        "options": ["Act", "Reflect", "Consider", "Identify"],
                        "answer": "Reflect",
                        "explanation": "The framework follows a 4-step process: Identify, Consider, Act, and finally Reflect on the outcome and the decision-making process."
                    }
                ],
                "Brutal (Above Exam)": [
                    {
                        "question": "An analyst identifies a conflict of interest but is pressured by a supervisor to ignore it to meet a quarterly target. According to the Ethical Decision-Making Framework, the analyst should 'Consider' which of the following FIRST?",
                        "options": ["The potential for a bonus increase.", "Situational influences such as 'Obedience to Authority'.", "The technical legality of the trade.", "The Firm's internal compliance manual exclusively."],
                        "answer": "Situational influences such as 'Obedience to Authority'.",
                        "explanation": "The 'Consider' phase specifically requires analysts to look beyond just rules and identify situational influences like peer pressure or obedience to authority that might cloud judgment."
                    }
                ]
            }
        },
        "Standard I: Professionalism": {
            "I(A) Knowledge of the Law": {
                "Hard (Exam Level)": [
                    {
                        "question": "An analyst lives in Country A (strict laws) but does business in Country B (loose laws). If the CFA Standards are stricter than Country B but looser than Country A, which must the analyst follow?",
                        "options": ["Country B Law", "CFA Standards", "Country A Law", "International Law"],
                        "answer": "Country A Law",
                        "explanation": "Standard I(A) requires following the strictest of: 1) Local Law, 2) Applicable Law, or 3) CFA Standards. Since Country A law is the strictest, it must be followed."
                    }
                ],
                "Brutal (Above Exam)": [
                    {
                        "question": "An analyst is based in a country where no securities laws exist. They are working on a deal in a cross-border market where the local law explicitly permits a practice that the CFA Code of Ethics prohibits. The analyst's firm policy is silent. The analyst should:",
                        "options": ["Follow the local law of the market as it is the 'Applicable Law'.", "Follow the CFA Code of Ethics as it is stricter than the local law.", "Abstain from the trade entirely until a legal opinion is sought.", "Follow the local law but disclose it to the CFA Institute."],
                        "answer": "Follow the CFA Code of Ethics as it is stricter than the local law.",
                        "explanation": "Standard I(A) dictates that in the absence of law or if the law is less strict than the Code and Standards, the member must follow the Code and Standards."
                    }
                ]
            }
        }
    }
