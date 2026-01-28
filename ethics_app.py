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
                    {"question": "Which of the following is the final step in the Ethical Decision-Making Framework?", "options": ["Act", "Reflect", "Consider", "Identify"], "answer": "Reflect", "explanation": "The framework follows a 4-step process: Identify, Consider, Act, and finally Reflect."}
                ],
                "Brutal (Above Exam)": [
                    {"question": "According to the Framework, 'Situational Influences' should be analyzed during which phase?", "options": ["Identify", "Consider", "Act", "Reflect"], "answer": "Consider", "explanation": "The 'Consider' phase is where you analyze biases and situational influences like obedience to authority."}
                ]
            },
            "Identify Phase": {
                "Hard (Exam Level)": [
                    {"question": "During the 'Identify' phase, a professional should point out:", "options": ["Only the primary client.", "The facts, stakeholders, and duties owed.", "The quickest way to resolve the issue.", "Who is to blame."], "answer": "The facts, stakeholders, and duties owed.", "explanation": "Identification requires looking at the facts and everyone to whom a duty is owed."}
                ],
                "Brutal (Above Exam)": [
                    {"question": "Which situational influence is most likely to cause a 'blind spot' during the Identify phase?", "options": ["Focusing on short-term results.", "A clear violation of policy.", "Directly asking for a bribe.", "Presence of a verifier."], "answer": "Focusing on short-term results.", "explanation": "Short-termism is a powerful influence that can lead to 'ethical fading.'"}
                ]
            },
            "Consider Phase": {
                "Hard (Exam Level)": [
                    {"question": "Which of the following is considered a 'situational influence'?", "options": ["A written firm policy.", "Obedience to authority.", "The GIPS standards.", "Local securities law."], "answer": "Obedience to authority.", "explanation": "Situational influences are external factors, such as pressure from a boss, that lead to poor choices."}
                ],
                "Brutal (Above Exam)": [
                    {"question": "An analyst observes misrepresentation but stays silent because 'no one else is speaking up.' This is:", "options": ["Professional Prudence.", "Social Proof.", "Loyalty to Employer.", "Knowledge of Law."], "answer": "Social Proof.", "explanation": "Social Proof is a situational influence where people mirror the behavior of the group."}
                ]
            },
            "Act/Reflect Phase": {
                "Hard (Exam Level)": [
                    {"question": "The primary objective of the 'Reflect' phase is to:", "options": ["Find someone to blame.", "Maximize future bonuses.", "Strengthen future ethical decision-making.", "Ensure legal fees are minimized."], "answer": "Strengthen future ethical decision-making.", "explanation": "Reflection is a continuous improvement step to learn from the outcome."}
                ],
                "Brutal (Above Exam)": [
                    {"question": "An analyst who ignores a failure to act during the 'Reflect' phase is failing in which duty?", "options": ["Duty to Employers.", "Duty to the Integrity of the Profession.", "Duty to the Government.", "Duty to themselves only."], "answer": "Duty to the Integrity of the Profession.", "explanation": "Continuous improvement through reflection is a hallmark of professional integrity."}
                ]
            }
        },
        "Standard I: Professionalism": {
            "I(A) Knowledge of the Law": {
                "Hard (Exam Level)": [
                    {"question": "If CFA Standards are stricter than local law, which must the analyst follow?", "options": ["Local Law", "CFA Standards", "Neither", "The more lenient one"], "answer": "CFA Standards", "explanation": "Standard I(A) requires following the stricter of the two."}
                ],
                "Brutal (Above Exam)": [
                    {"question": "An analyst knows a colleague is violating the law. According to Standard I(A), the analyst must FIRST:", "options": ["Report to the police.", "Dissociate from the activity.", "Contact the CFA Institute.", "Tell the client."], "answer": "Dissociate from the activity.", "explanation": "The first step in Knowledge of the Law is to stop participating in or being associated with the violation."}
                ]
            }
        }
    }
    
