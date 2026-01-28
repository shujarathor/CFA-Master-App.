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
    }        ,
        "Consider Phase": {
            "Hard (Exam Level)": [
                {"question": "During the 'Consider' phase of the Ethical Decision-Making Framework, situational influences are analyzed. Which of the following is a situational influence?", "options": ["Financial technical analysis.", "Obedience to authority.", "GIPS compliance manuals.", "The firm's legal counsel."], "answer": "Obedience to authority.", "explanation": "Situational influences are external pressures, such as group norms or obedience to authority, that can bias judgment."},
                {"question": "When evaluated in the 'Consider' phase, an analyst should seek additional guidance from whom?", "options": ["A competitor firm.", "The CFA Institute Code and Standards.", "Their family members.", "The client's friends."], "answer": "The CFA Institute Code and Standards.", "explanation": "Practitioners should seek independent, objective assessments and guidance from ethical standards."},
                {"question": "Why is it important to brainstorm alternative actions during the 'Consider' phase?", "options": ["To find the most profitable route.", "To avoid a preconceived path and reduce bias.", "To delay the decision as long as possible.", "To ensure the client is not involved."], "answer": "To avoid a preconceived path and reduce bias.", "explanation": "Brainstorming helps avoid 'blind spots' and ensures multiple solutions are evaluated objectively."},
                {"question": "In the 'Consider' phase, internal biases are identified. An example of an internal bias is:", "options": ["Overconfidence.", "Market volatility.", "Strict local laws.", "Client risk tolerance."], "answer": "Overconfidence.", "explanation": "Internal biases, such as overconfidence, are self-driven factors that can cloud ethical judgment."},
                {"question": "The 'Consider' phase primarily focuses on:", "options": ["Gathering facts.", "Analyzing situational influences and alternative paths.", "Making the final decision.", "Reflecting on previous years' data."], "answer": "Analyzing situational influences and alternative paths.", "explanation": "This phase is about looking at the pressures and options before taking action."}
            ],
            "Brutal (Above Exam)": [
                {"question": "An analyst is pressured by a supervisor to ignore a reporting error to meet a bonus deadline. According to the 'Consider' phase, which situational influence is the MOST likely cause of 'ethical fading' here?", "options": ["The technicality of the error.", "The incentive structure (bonus deadline).", "The size of the client's portfolio.", "The lack of GIPS verification."], "answer": "The incentive structure (bonus deadline).", "explanation": "Incentives are powerful situational pressures that can cause the ethical dimensions of a decision to fade from view."},
                {"question": "Which situational influence is described as 'Social Proof' in the 'Consider' phase?", "options": ["Following a written law.", "Doing what everyone else is doing (group norms).", "Directly obeying a CEO's order.", "Seeking a legal opinion."], "answer": "Doing what everyone else is doing (group norms).", "explanation": "Social proof occurs when individuals mirror the behavior of the group, even if it is unethical."},
                {"question": "If an analyst decides to proceed with an unethical action because they believe they are 'smart enough to manage the fallout,' they are primarily exhibiting:", "options": ["Loyalty to Employer.", "Overconfidence bias.", "Professionalism.", "Independence."], "answer": "Overconfidence bias.", "explanation": "Overconfidence in one's own ethicality or ability is a major internal bias identified in the framework."},
                {"question": "The 'Consider' phase requires an analyst to seek 'additional guidance.' This is crucial when:", "options": ["The answer is clearly right or wrong.", "The situation falls outside clear 'right' vs 'wrong' boundaries.", "The client is not looking.", "The firm's profit is at risk."], "answer": "The situation falls outside clear 'right' vs 'wrong' boundaries.", "explanation": "The framework is specifically designed for ambiguous scenarios where rules aren't enough."},
                {"question": "A member seeks an 'independent assessment' during the Consider phase. This is meant to:", "options": ["Share the blame.", "Gain an objective perspective on potential biases.", "Speed up the decision-making process.", "Avoid reporting to compliance."], "answer": "Gain an objective perspective on potential biases.", "explanation": "External objective views help highlight situational influences that the member might be blind to."}
            ]
        },
        "Act/Reflect Phase": {
            "Hard (Exam Level)": [
                {"question": "In the 'Act' phase, what is a valid alternative to making the decision yourself?", "options": ["Ignoring the issue.", "Elevating the issue to a higher authority.", "Wait for the client to notice.", "Quit the job immediately."], "answer": "Elevating the issue to a higher authority.", "explanation": "The 'Act' phase includes making a decision or elevating concerns to a supervisor or compliance."},
                {"question": "When should the 'Reflect' phase occur?", "options": ["Only if the decision was wrong.", "After the action has been taken.", "Before identifying the facts.", "Only if the client complains."], "answer": "After the action has been taken.", "explanation": "Reflection is the final step to review the path taken and learn for future decisions."},
                {"question": "The primary goal of the 'Reflect' phase is:", "options": ["To avoid future legal fees.", "To improve future ethical decision-making.", "To find someone to blame.", "To maximize the next quarter's bonus."], "answer": "To improve future ethical decision-making.", "explanation": "Reflection allows the practitioner to learn from the outcome and strengthen their ethical judgment."},
                {"question": "During the 'Act' phase, a member should choose an option that they can:", "options": ["Keep secret.", "Defend publicly.", "Profit from most.", "Explain to their family only."], "answer": "Defend publicly.", "explanation": "Ethical actions should be defensible to the public, the profession, and the client."},
                {"question": "Reflecting on your 'strengths and weaknesses' is part of which phase?", "options": ["Identify", "Consider", "Act", "Reflect"], "answer": "Reflect", "explanation": "The final step involves a self-assessment of how one handled the ethical dilemma."}
            ],
            "Brutal (Above Exam)": [
                {"question": "An analyst's decision resulted in a short-term financial loss for the firm. During 'Reflect,' the analyst should:", "options": ["Regret the decision.", "Evaluate if the decision upheld the integrity of the profession despite the loss.", "Focus on how to recover the money.", "Apologize to the supervisor for the lost revenue."], "answer": "Evaluate if the decision upheld the integrity of the profession despite the loss.", "explanation": "Reflection must focus on the adherence to the Code of Ethics, which places professional integrity above personal or firm gain."},
                {"question": "Which is an example of 'Ethical Fading' that might be identified during the Reflect phase?", "options": ["Learning a new law.", "The ethical aspects of the decision disappearing as the focus shifted to financial targets.", "Improving compliance manuals.", "Updating client records."], "answer": "The ethical aspects of the decision disappearing as the focus shifted to financial targets.", "explanation": "Ethical fading is a critical concept where pressures make the 'right thing' invisible during the decision process."},
                {"question": "If a member decides to 'Elevate the issue' in the Act phase, they must:", "options": ["Consider their responsibility complete once the boss knows.", "Follow up to ensure appropriate action was taken.", "Inform the client immediately.", "Post the issue on social media."], "answer": "Follow up to ensure appropriate action was taken.", "explanation": "Elevating is not enough; one must ensure that the ethical issue is actually addressed."},
                {"question": "How does the 'Reflect' phase contribute to 'Professionalism'?", "options": ["By increasing technical skills.", "By building a reputation for consistent, high-quality ethical judgment.", "By avoiding all risk.", "By focusing on legal loopholes."], "answer": "By building a reputation for consistent, high-quality ethical judgment.", "explanation": "Continuous reflection builds the 'muscle memory' needed for professional integrity."},
                {"question": "In a 'Brutal' case where no action was taken, the 'Reflect' phase would focus on:", "options": ["The money saved.", "Why situational influences prevented action (Identify the failure).", "The lack of a client complaint.", "The supervisor's approval."], "answer": "Why situational influences prevented action (Identify the failure).", "explanation": "If no action was taken when one was needed, reflection must identify which biases or pressures caused the failure."}
            ]
        }

