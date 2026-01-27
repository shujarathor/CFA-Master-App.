import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: Ethics Mastery", layout="wide")

# --- 1. FULLY HARD-CODED DATABASE (STANDARD I) ---
if 'master_db' not in st.session_state:
    st.session_state.master_db = {
        "Standard I": [
            # --- 30 HARD-LEARNING QUESTIONS ---
            {"id": 1, "level": "Hard-Learning", "focus": "I(A) Knowledge of the Law", "question": "An analyst's home country has no laws on a specific issue, but they do business in a country where the local law is less strict than the CFA Code. What must they follow?", "options": ["Local Law", "The Code and Standards", "No requirement"], "correct": "The Code and Standards", "rationale": "Members must follow the stricter of the law or the Code. If the law is less strict, the Code prevails."},
            {"id": 2, "level": "Hard-Learning", "focus": "I(C) Misrepresentation", "question": "Changing the name on a research report and presenting it as your own without changing the content is:", "options": ["Efficiency", "Plagiarism", "Market Manipulation"], "correct": "Plagiarism", "rationale": "Standard I(C) strictly prohibits misrepresenting work created by others as your own."},
            {"id": 3, "level": "Hard-Learning", "focus": "I(B) Independence", "question": "A client offers a bonus for future performance. To accept, the analyst needs:", "options": ["Verbal consent", "Written consent from employer", "To just disclose it"], "correct": "Written consent from employer", "rationale": "Bonuses for future performance require written permission from the employer."},
            {"id": 4, "level": "Hard-Learning", "focus": "I(A) Knowledge of the Law", "question": "If you suspect a colleague of illegal activity, the first step is to:", "options": ["Call the police", "Dissociate from the activity", "Wait for the SEC"], "correct": "Dissociate from the activity", "rationale": "Standard I(A) emphasizes dissociation as the primary responsibility."},
            {"id": 5, "level": "Hard-Learning", "focus": "I(D) Misconduct", "question": "Conduct that reflects poorly on professional integrity, even if not work-related, is a violation of:", "options": ["I(A)", "I(D)", "VII(A)"], "correct": "I(D)", "rationale": "Standard I(D) covers actions like fraud or deceit that damage the profession's reputation."},
            {"id": 6, "level": "Hard-Learning", "focus": "I(B) Independence", "question": "An issuer-paid due diligence trip is allowed ONLY if:", "options": ["The hotel is 5-star", "The firm pays for transportation", "The analyst stays neutral"], "correct": "The firm pays for transportation", "rationale": "Firms should pay for their own travel and lodging to maintain independence."},
            {"id": 7, "level": "Hard-Learning", "focus": "I(C) Misrepresentation", "question": "Guaranteeing a specific return on a risky investment violates:", "options": ["I(C) Misrepresentation", "V(B) Communication", "III(A) Loyalty"], "correct": "I(C) Misrepresentation", "rationale": "Guaranteeing returns on non-guaranteed investments misrepresents risk."},
            {"id": 8, "level": "Hard-Learning", "focus": "I(A) Knowledge of the Law", "question": "When a conflict of law exists, the member must:", "options": ["Follow the home law", "Follow the stricter law", "Ask a lawyer"], "correct": "Follow the stricter law", "rationale": "Standard I(A) requires adherence to the strictest applicable rule."},
            {"id": 9, "level": "Hard-Learning", "focus": "I(B) Objectivity", "question": "Sell-side analysts being pressured by investment banking to issue 'Buy' ratings violates:", "options": ["I(B) Independence", "I(A) Law", "II(B) Manipulation"], "correct": "I(B) Independence", "rationale": "Independence and objectivity must be maintained regardless of internal pressure."},
            {"id": 10, "level": "Hard-Learning", "focus": "I(C) Plagiarism", "question": "Using third-party research without citing the source is a violation of:", "options": ["I(C)", "I(B)", "I(A)"], "correct": "I(C)", "rationale": "Standard I(C) requires proper attribution for all third-party material."},
            {"id": 11, "level": "Hard-Learning", "focus": "I(D) Integrity", "question": "Professional misconduct includes which of the following?", "options": ["Personal bankruptcy", "Civil disobedience", "Lying on a resume"], "correct": "Lying on a resume", "rationale": "Lying on a resume is an act of deceit reflecting on professional integrity."},
            {"id": 12, "level": "Hard-Learning", "focus": "I(B) Gifts", "question": "A gift from a client for past performance requires:", "options": ["Pre-approval", "Disclosure to employer", "Rejection"], "correct": "Disclosure to employer", "rationale": "Gifts for past performance require disclosure; future performance requires permission."},
            {"id": 13, "level": "Hard-Learning", "focus": "I(A) Dissociation", "question": "If you cannot stop an illegal act within your firm, you MUST:", "options": ["Resign immediately", "Dissociate from the act", "Inform the CFAI"], "correct": "Dissociate from the act", "rationale": "Dissociation is the minimum requirement."},
            {"id": 14, "level": "Hard-Learning", "focus": "I(C) Oral Misrepresentation", "question": "Does Standard I(C) apply to oral communications?", "options": ["Yes", "No", "Only if recorded"], "correct": "Yes", "rationale": "Standard I(C) covers all forms of misrepresentation, including verbal."},
            {"id": 15, "level": "Hard-Learning", "focus": "I(D) Misconduct", "question": "Standard I(D) prohibits which of the following?", "options": ["Traffic violations", "Substance abuse at work", "Non-work related protest"], "correct": "Substance abuse at work", "rationale": "Conduct that impairs professional duty is a violation."},
            {"id": 16, "level": "Hard-Learning", "focus": "I(B) Research", "question": "Analysts should avoid which travel arrangements from an issuer?", "options": ["Standard hotel", "Chartered private jet", "Commercial flight"], "correct": "Chartered private jet", "rationale": "Lavish travel provided by an issuer threatens independence."},
            {"id": 17, "level": "Hard-Learning", "focus": "I(A) Supervisor Role", "question": "If a supervisor is aware of a law violation but takes no action:", "options": ["Violation of I(A)", "No violation", "Only subordinate is liable"], "correct": "Violation of I(A)", "rationale": "Supervisors have a duty to ensure compliance."},
            {"id": 18, "level": "Hard-Learning", "focus": "I(C) Modifying Reports", "question": "Releasing a report with a typo in the ticker symbol is:", "options": ["Negligence", "A mistake (No Violation)", "Manipulation"], "correct": "A mistake (No Violation)", "rationale": "Standard I(C) targets intentional or reckless misrepresentation."},
            {"id": 19, "level": "Hard-Learning", "focus": "I(B) Gifts", "question": "A $50 gift from a client to an analyst is:", "options": ["Violation", "Acceptable with disclosure", "Prohibited"], "correct": "Acceptable with disclosure", "rationale": "Modest gifts from clients are generally acceptable if disclosed."},
            {"id": 20, "level": "Hard-Learning", "focus": "I(D) Bankruptcy", "question": "Personal bankruptcy due to medical crisis is:", "options": ["Violation of I(D)", "Not a violation", "Violation of I(A)"], "correct": "Not a violation", "rationale": "Personal financial tragedy without deceit does not violate I(D)."},
            {"id": 21, "level": "Hard-Learning", "focus": "I(B) Soft Dollars", "question": "Accepting 'Soft Dollars' for research services is:", "options": ["Violation", "Allowed with disclosure", "Always illegal"], "correct": "Allowed with disclosure", "rationale": "Soft dollars are acceptable if they benefit the client."},
            {"id": 22, "level": "Hard-Learning", "focus": "I(C) Credentials", "question": "Claiming you 'passed all 3 levels on the first try' is:", "options": ["Violation", "Factual statement", "Misrepresentation"], "correct": "Factual statement", "rationale": "Factual statements about exam history are permitted."},
            {"id": 23, "level": "Hard-Learning", "focus": "I(A) Legal Advice", "question": "If unsure about a law, a member should:", "options": ["Consult counsel", "Guess", "Ask a colleague"], "correct": "Consult counsel", "rationale": "Seeking legal advice is the appropriate step."},
            {"id": 24, "level": "Hard-Learning", "focus": "I(B) Tokens", "question": "Accepting a coffee from a client during a meeting is:", "options": ["Violation", "Not a violation", "Requires disclosure"], "correct": "Not a violation", "rationale": "Tokens of nominal value do not compromise independence."},
            {"id": 25, "level": "Hard-Learning", "focus": "I(C) Models", "question": "Presenting firm-owned model results as your own creation is:", "options": ["Violation", "Allowed", "Depends on contract"], "correct": "Violation", "rationale": "Standard I(C) requires accurate representation of authorship."},
            {"id": 26, "level": "Hard-Learning", "focus": "I(D) Misconduct", "question": "Drunkenness during a professional conference is:", "options": ["Violation", "Not a violation", "Allowed after hours"], "correct": "Violation", "rationale": "Reflects poorly on the integrity of the profession."},
            {"id": 27, "level": "Hard-Learning", "focus": "I(B) Objectivity", "question": "Writing a report on a company while working for them is:", "options": ["Conflict (I(B))", "Allowed", "Illegal"], "correct": "Conflict (I(B))", "rationale": "This creates a massive threat to objectivity."},
            {"id": 28, "level": "Hard-Learning", "focus": "I(A) Dissociation", "question": "Does dissociation require reporting to the government?", "options": ["Yes", "No", "Only for felonies"], "correct": "No", "rationale": "The Code does not require reporting to authorities."},
            {"id": 29, "level": "Hard-Learning", "focus": "I(C) Plagiarism", "question": "Using a quote from a famous economist without citation is:", "options": ["Violation", "Not a violation", "Allowed if common"], "correct": "Violation", "rationale": "Citation is required for all non-original work."},
            {"id": 30, "level": "Hard-Learning", "focus": "I(D) Dishonesty", "question": "Sharing exam questions after the CFA exam is a violation of:", "options": ["VII(A)", "I(D)", "Both"], "correct": "Both", "rationale": "It is misconduct and a violation of candidate duties."},

            # --- 30 ABOVE-EXAM LEVEL QUESTIONS ---
            {"id": 31, "level": "Above-Exam Level", "focus": "I(A) Jurisdictions", "question": "Citizen of Country A, works in Country B, trades in Country C. Which rule prevails?", "options": ["Home law", "Host law", "Strictest of all"], "correct": "Strictest of all", "rationale": "Standard I(A) requires the most stringent regulation."},
            {"id": 32, "level": "Above-Exam Level", "focus": "I(B) Brokerage", "question": "Client directs broker who provides luxury perks to the analyst. Violation?", "options": ["Yes, I(B)", "No, client directed", "Only if trades are poor"], "correct": "Yes, I(B)", "rationale": "Accepting perks compromising objectivity is a violation."},
            {"id": 33, "level": "Above-Exam Level", "focus": "I(C) Benchmarking", "question": "Selecting only best years to show a track record is:", "options": ["Marketing", "Misrepresentation", "Standard"], "correct": "Misrepresentation", "rationale": "Cherry-picking data to mislead is a violation of I(C)."},
            {"id": 34, "level": "Above-Exam Level", "focus": "I(D) Convictions", "question": "Felony non-violent protest. Automatic violation of I(D)?", "options": ["Yes", "No", "Depends on firm"], "correct": "No", "rationale": "Standard I(D) targets acts of dishonesty/professional impairment."},
            {"id": 35, "level": "Above-Exam Level", "focus": "I(B) Pressure", "question": "Salary tied directly to the success of an IPO being reviewed. Is this:", "options": ["Incentive", "Violation of I(B)", "Standard"], "correct": "Violation of I(B)", "rationale": "Structures threatening objectivity are violations."},
            {"id": 36, "level": "Above-Exam Level", "focus": "I(A) Knowledge", "question": "Reporting a violation to a supervisor fulfills the duty of dissociation?", "options": ["Yes", "No", "Only if supervisor agrees"], "correct": "No", "rationale": "Reporting is the first step; if the act continues, further dissociation is required."},
            {"id": 37, "level": "Above-Exam Level", "focus": "I(C) Plagiarism", "question": "Using firm research without citing a departed colleague is:", "options": ["Violation", "Allowed", "Only if colleague is senior"], "correct": "Allowed", "rationale": "Research belongs to the firm; citation of former employees is not required."},
            {"id": 38, "level": "Above-Exam Level", "focus": "I(B) Independence", "question": "An analyst accepts a flight to a remote area from an issuer because no commercial flights exist. The firm does not reimburse. Violation?", "options": ["Yes", "No", "Only if report is biased"], "correct": "Yes", "rationale": "Firms must pay for their own due diligence travel costs."},
            {"id": 39, "level": "Above-Exam Level", "focus": "I(D) Professionalism", "question": "A member is involved in a legal but unethical tax avoidance scheme. Violation?", "options": ["Yes, I(D)", "No, it is legal", "Only if clients are involved"], "correct": "Yes, I(D)", "rationale": "Conduct that reflects poorly on professional reputation violates I(D)."},
            {"id": 40, "level": "Above-Exam Level", "focus": "I(C) Misrepresentation", "question": "Presenting hypothetical performance as actual performance is:", "options": ["Violation", "Marketing", "Allowed with disclosure"], "correct": "Violation", "rationale": "Hypothetical data must be clearly labeled as such."},
            {"id": 41, "level": "Above-Exam Level", "focus": "I(A) Dissociation", "question": "Resigning from a firm is the only way to dissociate from an illegal act?", "options": ["Yes", "No", "Only for fraud"], "correct": "No", "rationale": "Dissociation can include stopping work on a specific project or reporting internally."},
            {"id": 42, "level": "Above-Exam Level", "focus": "I(B) Objectivity", "question": "A research report is vetted by a firm's marketing team to 'align messaging'. Violation?", "options": ["Yes, I(B)", "No", "Only if facts change"], "correct": "Yes, I(B)", "rationale": "Marketing vetting threatens the independence of research."},
            {"id": 43, "level": "Above-Exam Level", "focus": "I(C) Data Attribution", "question": "Using a data table from a government agency without citation is:", "options": ["Allowed", "Violation", "Allowed if public"], "correct": "Allowed", "rationale": "Factual data from government or public sources often does not require citation, but it is best practice."},
            {"id": 44, "level": "Above-Exam Level", "focus": "I(D) Personal Life", "question": "A member is convicted of a non-violent felony drug possession. Violation of I(D)?", "options": ["Yes", "No", "Only if at work"], "correct": "No", "rationale": "Typically not a violation unless it impairs professional judgment or integrity."},
            {"id": 45, "level": "Above-Exam Level", "focus": "I(B) External Influence", "question": "A client offers to pay an analyst for a 'favorable' report. The analyst stays objective. Violation?", "options": ["Yes", "No", "Only if analyst accepts"], "correct": "Yes", "rationale": "The offer itself must be reported; accepting any part of it is a violation."},
            {"id": 46, "level": "Above-Exam Level", "focus": "I(A) Supervision", "question": "A supervisor implements a compliance system but never tests it. Violation of I(A)?", "options": ["Yes", "No", "Only if a violation occurs"], "correct": "Yes", "rationale": "Supervisors must actively ensure compliance systems are effective."},
            {"id": 47, "level": "Above-Exam Level", "focus": "I(C) Plagiarism", "question": "Copying a peer's rationale but using original numbers is:", "options": ["Violation", "Allowed", "Efficiency"], "correct": "Violation", "rationale": "Copying the rationale or 'thinking' is plagiarism."},
            {"id": 48, "level": "Above-Exam Level", "focus": "I(B) Travel", "question": "Issuer pays for an analyst's economy flight for a factory tour. Violation?", "options": ["Yes", "No", "Only if 1st class"], "correct": "Yes", "rationale": "Analysts must avoid issuer-paid travel to maintain objectivity."},
            {"id": 49, "level": "Above-Exam Level", "focus": "I(D) Misconduct", "question": "Committing tax fraud in personal filings is a violation of:", "options": ["I(D)", "I(A)", "No violation"], "correct": "I(D)", "rationale": "Acts of deceit, even if personal, reflect on professional integrity."},
            {"id": 50, "level": "Above-Exam Level", "focus": "I(C) Misrepresentation", "question": "Using a model that contains a known minor error without correction is:", "options": ["Violation", "Mistake", "Allowed if error is small"], "correct": "Violation", "rationale": "Knowingly using erroneous models is misrepresentation."},
            {"id": 51, "level": "Above-Exam Level", "focus": "I(A) Knowledge", "question": "An analyst follows the less strict local law because they were 'ordered' by their boss. Violation?", "options": ["Yes", "No", "Only the boss is liable"], "correct": "Yes", "rationale": "Individual responsibility exists regardless of supervisor orders."},
            {"id": 52, "level": "Above-Exam Level", "focus": "I(B) Independence", "question": "Participating in a heavily discounted IPO of a company you cover is:", "options": ["Incentive", "Violation of I(B)", "Allowed if disclosed"], "correct": "Violation of I(B)", "rationale": "Accepting discounted shares from a covered entity creates bias."},
            {"id": 53, "level": "Above-Exam Level", "focus": "I(C) Plagiarism", "question": "A member uses a chart from a Bloomberg terminal without citation. Violation?", "options": ["Yes", "No", "Only if they claim they made it"], "correct": "Yes", "rationale": "Proper attribution for terminal data or charts is required."},
            {"id": 54, "level": "Above-Exam Level", "focus": "I(D) Misconduct", "question": "Being sued in a civil court for a personal contract dispute is:", "options": ["Violation", "Not a violation", "Violation if you lose"], "correct": "Not a violation", "rationale": "Civil disputes usually do not reflect on professional integrity unless deceit is found."},
            {"id": 55, "level": "Above-Exam Level", "focus": "I(B) Objectivity", "question": "Issuer pays for lunch during an all-day factory tour. Violation?", "options": ["Yes", "No", "Depends on the food"], "correct": "No", "rationale": "Tokens of nominal value (like a standard lunch) are acceptable during business meetings."},
            {"id": 56, "level": "Above-Exam Level", "focus": "I(A) Law", "question": "An analyst dissociation requires them to notify the CFA Institute?", "options": ["Yes", "No", "Recommended"], "correct": "No", "rationale": "Notification is not required for dissociation under the Code."},
            {"id": 57, "level": "Above-Exam Level", "focus": "I(C) Misrepresentation", "question": "Failing to disclose a significant change in a model's logic is:", "options": ["Violation", "Efficiency", "Allowed"], "correct": "Violation", "rationale": "Investors must be informed of the 'basis' of recommendations."},
            {"id": 58, "level": "Above-Exam Level", "focus": "I(D) Dishonesty", "question": "Plagiarizing a blog post about cooking. Violation of I(D)?", "options": ["Yes", "No", "Only if on a work site"], "correct": "Yes", "rationale": "Any act of dishonesty, even personal, can violate I(D)."},
            {"id": 59, "level": "Above-Exam Level", "focus": "I(B) Independence", "question": "A manager forces an analyst to attend a lavish client party. Violation?", "options": ["Yes, I(B)", "No", "Only if analyst drinks"], "correct": "Yes, I(B)", "rationale": "Lavish entertainment threatens independence even if firm-mandated."},
            {"id": 60, "level": "Above-Exam Level", "focus": "I(C) Plagiarism", "question": "Using a chart from a firm research report written 10 years ago without attribution is:", "options": ["Allowed", "Violation", "Recommended"], "correct": "Allowed", "rationale": "Firm property can be shared internally without individual attribution."},
        ],
        "Standard II": [], "Standard III": [], "Standard IV": [], "Standard V": [], "Standard VI": [], "Standard VII": []
    }

if 'flashcards' not in st.session_state:
    st.session_state.flashcards = {
        "Standard I": [
            {"front": "Scenario: Local law is stricter than the Code.", "back": "Follow Local Law."},
            {"front": "Scenario: Code is stricter than Local Law.", "back": "Follow the Code."},
            {"front": "What is the primary step for dissociation?", "back": "Stop working on the activity or report it internally."},
            {"front": "Does Standard I(C) apply to verbal communication?", "back": "Yes, it applies to all forms of misrepresentation."},
            {"front": "When is a client gift a violation of I(B)?", "back": "When it is a future bonus and you don't have written permission."},
            {"front": "Is personal bankruptcy a violation of I(D)?", "back": "No, unless it involves deceit or fraud."},
            {"front": "Who owns research models created at a firm?", "back": "The firm owns them."},
            {"front": "Can you use a public chart without citation?", "back": "Factual public data often doesn't need it, but it's best to cite."},
            {"front": "What is the baseline for global jurisdictions?", "back": "Adhere to the most stringent regulation available."},
            {"front": "Is dissociation enough if illegal acts continue?", "back": "In extreme cases, resignation may be necessary."},
        ]
    }

# --- 2. STATE & SIDEBAR ---
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'f_idx' not in st.session_state: st.session_state.f_idx = 0
if 'performance' not in st.session_state: st.session_state.performance = []
if 'los_notes' not in st.session_state: st.session_state.los_notes = ""

st.sidebar.title("📟 Command Center")
std = st.sidebar.selectbox("Standard Selection", list(st.session_state.master_db.keys()))
lvl = st.sidebar.radio("Difficulty Level", ["Hard-Learning", "Above-Exam Level"])

active_pool = [q for q in st.session_state.master_db.get(std, []) if q['level'] == lvl]

if st.sidebar.button(f"🔄 Reset {std}"):
    st.session_state.q_idx = 0
    st.session_state.f_idx = 0
    st.rerun()

# --- 3. MAIN INTERFACE ---
t1, t2, t3, t4 = st.tabs(["🎯 Practice Tank", "🗂️ Flashcards", "📊 Performance Lab", "📓 LOS Notes"])

with t1: # PRACTICE TANK
    if not active_pool:
        st.info("Tank empty. Data drop incoming.")
    elif st.session_state.q_idx >= len(active_pool):
        st.success(f"🏁 {std} ({lvl}) Complete! Reset to start over.")
    else:
        q = active_pool[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1} of {len(active_pool)}")
        st.write(q['question'])
        ans = st.radio("Pick one:", q['options'], key=f"q_{st.session_state.q_idx}")
        c1, col2 = st.columns(2)
        if c1.button("📡 Submit Answer"):
            if ans == q['correct']:
                st.success(f"✔️ {q['rationale']}")
                st.session_state.performance.append({"Std": std, "Res": "Pass"})
            else:
                st.error(f"❌ {q['rationale']}")
                st.session_state.performance.append({"Std": std, "Res": "Fail"})
        if col2.button("Next Question ➡️"):
            st.session_state.q_idx += 1
            st.rerun()

with t2: # FLASHCARDS
    f_pool = st.session_state.flashcards.get(std, [])
    if f_pool:
        card = f_pool[st.session_state.f_idx]
        st.subheader(f"Flashcard {st.session_state.f_idx + 1} of {len(f_pool)}")
        with st.expander("👁️ Front Scenario"): st.write(card['front'])
        with st.expander("🧠 Back Reasoning"): st.info(card['back'])
        col1, col2 = st.columns(2)
        if col1.button("⬅️ Previous"): st.session_state.f_idx = max(0, st.session_state.f_idx - 1); st.rerun()
        if col2.button("Next ➡️"): st.session_state.f_idx = min(len(f_pool)-1, st.session_state.f_idx + 1); st.rerun()

with t4: # LOS NOTES
    st.header("Personal LOS Notes")
    st.session_state.los_notes = st.text_area("Record insights here:", value=st.session_state.los_notes, height=400)
    st.button("💾 Save to Library")
