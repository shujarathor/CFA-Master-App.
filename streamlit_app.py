import streamlit as st
import pandas as pd

st.set_page_config(page_title="Professor G: Ethics Mastery", layout="wide")

# --- THE PERMANENT DATABASE: 60 UNIQUE ENTRIES FOR STANDARD I ---
if 'master_db' not in st.session_state:
    st.session_state.master_db = {
        "Standard I": [
            # --- HARD-LEARNING (1-30) ---
            {"id": 1, "level": "Hard-Learning", "focus": "I(A)", "question": "Analyst works in Country A (no law), trades in Country B (weak law). CFA Code is stricter. Follow which?", "options": ["Country B Law", "CFA Code", "Home Law"], "correct": "CFA Code", "rationale": "Follow the stricter of the Law or the Code."},
            {"id": 2, "level": "Hard-Learning", "focus": "I(C)", "question": "Plagiarizing a report by changing names but keeping price targets is a violation of:", "options": ["I(C) Misrepresentation", "I(B) Independence", "I(A) Law"], "correct": "I(C) Misrepresentation", "rationale": "Standard I(C) prohibits misrepresenting others' work as your own."},
            {"id": 3, "level": "Hard-Learning", "focus": "I(B)", "question": "A client offers a bonus for future performance. What is required to accept?", "options": ["Verbal consent", "Written consent from employer", "Disclosure only"], "correct": "Written consent from employer", "rationale": "Future bonuses require written permission from the employer."},
            {"id": 4, "level": "Hard-Learning", "focus": "I(A)", "question": "If you suspect illegal activity, your first professional obligation is to:", "options": ["Report to police", "Dissociate", "Ask for a raise"], "correct": "Dissociate", "rationale": "Standard I(A) mandates dissociation from illegal acts."},
            {"id": 5, "level": "Hard-Learning", "focus": "I(D)", "question": "Professional misconduct includes:", "options": ["Personal bankruptcy", "Lying on a resume", "Non-work related protest"], "correct": "Lying on a resume", "rationale": "Lying on a resume is a deceitful act violating I(D)."},
            {"id": 6, "level": "Hard-Learning", "focus": "I(B)", "question": "Issuer-paid travel is allowed if:", "options": ["Hotel is luxury", "Firm pays transport", "Report is neutral"], "correct": "Firm pays transport", "rationale": "Firms must pay their own travel to stay independent."},
            {"id": 7, "level": "Hard-Learning", "focus": "I(C)", "question": "Guaranteeing returns on a risky investment violates:", "options": ["I(C)", "V(B)", "III(A)"], "correct": "I(C)", "rationale": "Guaranteeing returns misrepresents the nature of risk."},
            {"id": 8, "level": "Hard-Learning", "focus": "I(A)", "question": "When laws conflict, follow the:", "options": ["Home law", "Stricter law", "Code"], "correct": "Stricter law", "rationale": "Adhere to the most stringent applicable rule."},
            {"id": 9, "level": "Hard-Learning", "focus": "I(B)", "question": "Banking pressure to issue 'Buy' ratings violates:", "options": ["I(B)", "I(A)", "II(B)"], "correct": "I(B)", "rationale": "Independence must be maintained despite internal pressure."},
            {"id": 10, "level": "Hard-Learning", "focus": "I(C)", "question": "Using 3rd party research without citation violates:", "options": ["I(C)", "I(B)", "I(A)"], "correct": "I(C)", "rationale": "Attribute all third-party material properly."},
            {"id": 11, "level": "Hard-Learning", "focus": "I(D)", "question": "Standard I(D) prohibits:", "options": ["Negligence", "Dishonesty", "Losing money"], "correct": "Dishonesty", "rationale": "I(D) targets acts of deceit and dishonesty."},
            {"id": 12, "level": "Hard-Learning", "focus": "I(B)", "question": "Past performance client gifts require:", "options": ["Pre-approval", "Disclosure", "Rejection"], "correct": "Disclosure", "rationale": "Past gifts only require disclosure to the employer."},
            {"id": 13, "level": "Hard-Learning", "focus": "I(A)", "question": "If you can't stop an illegal act, you must:", "options": ["Resign", "Dissociate", "Tell CFAI"], "correct": "Dissociate", "rationale": "Dissociation is the required minimum step."},
            {"id": 14, "level": "Hard-Learning", "focus": "I(C)", "question": "Standard I(C) applies to verbal statements?", "options": ["Yes", "No", "Only if recorded"], "correct": "Yes", "rationale": "I(C) covers all forms of misrepresentation."},
            {"id": 15, "level": "Hard-Learning", "focus": "I(D)", "question": "Intoxication while performing work duties is:", "options": ["Allowed", "A violation of I(D)", "Personal matter"], "correct": "A violation of I(D)", "rationale": "Conduct impairing duty violates professional integrity."},
            {"id": 16, "level": "Hard-Learning", "focus": "I(B)", "question": "Avoid which travel from an issuer?", "options": ["Bus", "Private Jet", "Commercial flight"], "correct": "Private Jet", "rationale": "Lavish travel provided by an issuer threatens objectivity."},
            {"id": 17, "level": "Hard-Learning", "focus": "I(A)", "question": "A supervisor who ignores a violation violates:", "options": ["I(A)", "No one", "Standard IV"], "correct": "I(A)", "rationale": "Supervisors have an active duty to ensure compliance."},
            {"id": 18, "level": "Hard-Learning", "focus": "I(C)", "question": "A simple clerical error in a report is:", "options": ["Negligence", "No violation", "Manipulation"], "correct": "No violation", "rationale": "I(C) targets intentional or reckless misrepresentation."},
            {"id": 19, "level": "Hard-Learning", "focus": "I(B)", "question": "A $25 client gift to an analyst is:", "options": ["Violation", "Acceptable", "Always banned"], "correct": "Acceptable", "rationale": "Tokens of nominal value are generally okay with disclosure."},
            {"id": 20, "level": "Hard-Learning", "focus": "I(D)", "question": "Medical crisis bankruptcy is:", "options": ["Violation", "No violation", "Fraud"], "correct": "No violation", "rationale": "Personal financial tragedy without deceit is not a violation."},
            {"id": 21, "level": "Hard-Learning", "focus": "I(B)", "question": "Soft Dollars are allowed if they:", "options": ["Pay analyst salary", "Benefit the client", "Are hidden"], "correct": "Benefit the client", "rationale": "Soft dollars must benefit the end client."},
            {"id": 22, "level": "Hard-Learning", "focus": "I(C)", "question": "Claiming you passed Level 1 on the first try is:", "options": ["Violation", "Factual statement", "Misconduct"], "correct": "Factual statement", "rationale": "True factual statements about exam status are permitted."},
            {"id": 23, "level": "Hard-Learning", "focus": "I(A)", "question": "When law is unclear, you should:", "options": ["Guess", "Consult Counsel", "Ignore it"], "correct": "Consult Counsel", "rationale": "Legal counsel is the appropriate resource for clarity."},
            {"id": 24, "level": "Hard-Learning", "focus": "I(B)", "question": "A coffee from a client is:", "options": ["Violation", "Not a violation", "Requires CFAI report"], "correct": "Not a violation", "rationale": "Nominal tokens do not compromise independence."},
            {"id": 25, "level": "Hard-Learning", "focus": "I(C)", "question": "Claiming credit for a firm-owned model is:", "options": ["Violation", "Allowed", "Efficiency"], "correct": "Violation", "rationale": "Standard I(C) requires accurate authorship representation."},
            {"id": 26, "level": "Hard-Learning", "focus": "I(D)", "question": "Public intoxication at a professional gala is:", "options": ["Violation", "Personal", "Okay after 9 PM"], "correct": "Violation", "rationale": "Reflects poorly on the professional community."},
            {"id": 27, "level": "Hard-Learning", "focus": "I(B)", "question": "Writing a report on a firm where you are a Director is:", "options": ["Violation", "Best practice", "Allowed with bold text"], "correct": "Violation", "rationale": "Dire conflict of independence and objectivity."},
            {"id": 28, "level": "Hard-Learning", "focus": "I(A)", "question": "Dissociation requires notifying the government?", "options": ["Yes", "No", "Only for fraud"], "correct": "No", "rationale": "Code does not require reporting to authorities."},
            {"id": 29, "level": "Hard-Learning", "focus": "I(C)", "question": "Using a quote without citation is:", "options": ["Violation", "No violation", "Allowed if brief"], "correct": "Violation", "rationale": "Standard I(C) requires citation for all non-original work."},
            {"id": 30, "level": "Hard-Learning", "focus": "I(D)", "question": "Cheating on personal taxes is a violation of:", "options": ["I(D)", "VII(A)", "No violation"], "correct": "I(D)", "rationale": "Deceitful personal acts reflect on professional integrity."},

            # --- ABOVE-EXAM LEVEL (31-60) ---
            {"id": 31, "level": "Above-Exam Level", "focus": "I(A)", "question": "Global context: Country A citizen, works in B, trades in C. Which rule is the baseline?", "options": ["Host Country", "Home Country", "Strictest of all"], "correct": "Strictest of all", "rationale": "Standard I(A) mandates adherence to the most stringent rule available."},
            {"id": 32, "level": "Above-Exam Level", "focus": "I(B)", "question": "Accepting perks from a client-directed broker violates I(B)?", "options": ["Yes", "No", "Only if trades are poor"], "correct": "Yes", "rationale": "Perks compromise objectivity regardless of client direction."},
            {"id": 33, "level": "Above-Exam Level", "focus": "I(C)", "question": "Cherry-picking only 'up-market' years for a performance track record is:", "options": ["Marketing", "Misrepresentation", "Standard Practice"], "correct": "Misrepresentation", "rationale": "Misleading performance presentation violates I(C)."},
            {"id": 34, "level": "Above-Exam Level", "focus": "I(D)", "question": "A non-violent civil disobedience conviction is a violation of I(D)?", "options": ["Yes", "No", "Always"], "correct": "No", "rationale": "I(D) targets acts of dishonesty or impairment of professional integrity."},
            {"id": 35, "level": "Above-Exam Level", "focus": "I(B)", "question": "Salary tied directly to the success of an IPO the analyst is reviewing violates I(B)?", "options": ["Yes", "No", "Standard"], "correct": "Yes", "rationale": "Compensation structures threatening objectivity are violations."},
            {"id": 36, "level": "Above-Exam Level", "focus": "I(A)", "question": "Internal reporting fulfills dissociation if the illegal act continues?", "options": ["Yes", "No", "Only for theft"], "correct": "No", "rationale": "If reporting fails and the act continues, you must stop working on that specific area."},
            {"id": 37, "level": "Above-Exam Level", "focus": "I(C)", "question": "Using firm research without citing a former colleague is okay?", "options": ["Yes", "No", "Only if retired"], "correct": "Yes", "rationale": "Research belongs to the firm, not the individual employee."},
            {"id": 38, "level": "Above-Exam Level", "focus": "I(B)", "question": "Issuer pays for private flight because no others exist. Violation?", "options": ["Yes", "No", "Depends on cost"], "correct": "Yes", "rationale": "Analyst firm must find commercial alternatives or pay for private flight themselves."},
            {"id": 39, "level": "Above-Exam Level", "focus": "I(D)", "question": "Involved in a legal but deceptive tax scheme. Violation?", "options": ["Yes", "No", "Only if fined"], "correct": "Yes", "rationale": "Deceptive acts, even if legal, reflect poorly on integrity."},
            {"id": 40, "level": "Above-Exam Level", "focus": "I(C)", "question": "Presenting hypothetical data as actual is a violation?", "options": ["Yes", "No", "Allowed if disclosed later"], "correct": "Yes", "rationale": "Hypothetical data must be explicitly labeled."},
            {"id": 41, "level": "Above-Exam Level", "focus": "I(A)", "question": "Is resignation the only way to dissociate?", "options": ["No", "Yes", "Only for felonies"], "correct": "No", "rationale": "Dissociation can be project-specific or via internal reporting."},
            {"id": 42, "level": "Above-Exam Level", "focus": "I(B)", "question": "Marketing team vetting research ratings for 'consistency' is a violation?", "options": ["Yes", "No", "Standard"], "correct": "Yes", "rationale": "Threatens the independence of the research process."},
            {"id": 43, "level": "Above-Exam Level", "focus": "I(C)", "question": "Using public government data without citation is allowed?", "options": ["Yes", "No", "Only if it is local"], "correct": "Yes", "rationale": "Public factual data often does not require specific citation under I(C)."},
            {"id": 44, "level": "Above-Exam Level", "focus": "I(D)", "question": "Felony drug possession conviction automatically violates I(D)?", "options": ["No", "Yes", "Only if at work"], "correct": "No", "rationale": "I(D) requires an impact on professional judgment or integrity."},
            {"id": 45, "level": "Above-Exam Level", "focus": "I(B)", "question": "An offer of a bonus for a 'favorable' report must be reported to the firm?", "options": ["Yes", "No", "Only if accepted"], "correct": "Yes", "rationale": "Attempts to influence must be reported immediately to supervisors."},
            {"id": 46, "level": "Above-Exam Level", "focus": "I(A)", "question": "Supervisor fails to actively test a compliance system. Violation?", "options": ["Yes", "No", "Only if fraud occurs"], "correct": "Yes", "rationale": "Active testing of systems is part of supervisory duty under I(A)."},
            {"id": 47, "level": "Above-Exam Level", "focus": "I(C)", "question": "Copying a peer's rationale but using original math is plagiarism?", "options": ["Yes", "No", "Efficiency"], "correct": "Yes", "rationale": "Plagiarism includes copying ideas and logic, not just text."},
            {"id": 48, "level": "Above-Exam Level", "focus": "I(B)", "question": "Issuer pays for an analyst's factory tour bus transport. Okay?", "options": ["Yes", "No", "Only for 1st class"], "correct": "Yes", "rationale": "Modest local transport for tours is generally acceptable and not a violation."},
            {"id": 49, "level": "Above-Exam Level", "focus": "I(D)", "question": "Deceiving a charity during personal volunteering violates I(D)?", "options": ["Yes", "No", "Personal matter"], "correct": "Yes", "rationale": "Deceit in any context harms professional reputation."},
            {"id": 50, "level": "Above-Exam Level", "focus": "I(C)", "question": "Knowingly using a model with a small error is a violation?", "options": ["Yes", "No", "If error is <1%"], "correct": "Yes", "rationale": "Knowingly distributing errors is misrepresentation."},
            {"id": 51, "level": "Above-Exam Level", "focus": "I(A)", "question": "Following a weak law because a boss ordered it is okay?", "options": ["No", "Yes", "Boss is liable"], "correct": "No", "rationale": "Individual responsibility is paramount; boss orders do not excuse violations."},
            {"id": 52, "level": "Above-Exam Level", "focus": "I(B)", "question": "Taking discounted IPO shares from a company you cover is a violation?", "options": ["Yes", "No", "Allowed if disclosed"], "correct": "Yes", "rationale": "Accepting perks from covered entities creates bias."},
            {"id": 53, "level": "Above-Exam Level", "focus": "I(C)", "question": "Using Bloomberg terminal chart without attribution is plagiarism?", "options": ["Yes", "No", "Only if you made it"], "correct": "Yes", "rationale": "Proper source attribution is required for terminal data."},
            {"id": 54, "level": "Above-Exam Level", "focus": "I(D)", "question": "Personal civil lawsuit for contract dispute is a violation?", "options": ["No", "Yes", "If you lose"], "correct": "No", "rationale": "Civil disputes usually don't reflect on integrity unless fraud is found."},
            {"id": 55, "level": "Above-Exam Level", "focus": "I(B)", "question": "Standard lunch provided by issuer during factory tour is okay?", "options": ["Yes", "No", "Requires CFAI report"], "correct": "Yes", "rationale": "Tokens of nominal value during meetings are acceptable."},
            {"id": 56, "level": "Above-Exam Level", "focus": "I(A)", "question": "Does dissociation require reporting to the government authorities?", "options": ["No", "Yes", "Recommended"], "correct": "No", "rationale": "Not required by the CFA Code itself."},
            {"id": 57, "level": "Above-Exam Level", "focus": "I(C)", "question": "Failing to disclose change in model logic is misrepresentation?", "options": ["Yes", "No", "Only if price changed"], "correct": "Yes", "rationale": "Basis of recommendation must be clear for the client to understand."},
            {"id": 58, "level": "Above-Exam Level", "focus": "I(D)", "question": "Plagiarizing a personal hobby blog is a violation of I(D)?", "options": ["Yes", "No", "Only for finance"], "correct": "Yes", "rationale": "Deceit reflects on professional integrity regardless of topic."},
            {"id": 59, "level": "Above-Exam Level", "focus": "I(B)", "question": "Forced attendance at lavish party threatens independence?", "options": ["Yes", "No", "Only if you drink"], "correct": "Yes", "rationale": "Lavish entertainment is a threat even if employer-mandated."},
            {"id": 60, "level": "Above-Exam Level", "focus": "I(C)", "question": "Using firm research from 10 years ago without attribution is allowed?", "options": ["Yes", "No", "Only for seniors"], "correct": "Yes", "rationale": "Firm property can be shared internally without individual credit attribution."},
        ],
        "Standard II": [], "Standard III": [], "Standard IV": [], "Standard V": [], "Standard VI": [], "Standard VII": []
    }

if 'flashcards' not in st.session_state:
    st.session_state.flashcards = {
        "Standard I": [
            {"front": "Scenario: Local law is stricter than Code.", "back": "Result: Follow Local Law."},
            {"front": "Standard I(C): Plagiarism rule.", "back": "Result: Cite all non-original work."},
            {"front": "Standard I(D): Personal Conduct.", "back": "Result: Only violation if deceit/integrity is harmed."},
            {"front": "Dissociation Step 1.", "back": "Result: Internal reporting/Stop working on act."},
            {"front": "Issuer-paid travel rule.", "back": "Result: Banned unless firm pays transport."},
            {"front": "Standard I(B): Client gifts.", "back": "Result: Disclosure (Past) / Permission (Future)."},
            {"front": "Global Jurisdictions.", "back": "Result: Follow the strictest rule of all."},
            {"front": "Oral Misrepresentation.", "back": "Result: Prohibited under I(C)."},
            {"front": "Soft Dollars.", "back": "Result: Allowed if client benefits."},
            {"front": "Reporting to Government.", "back": "Result: Not required by CFA Code."},
        ]
    }

# --- STATE MANAGEMENT ---
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'f_idx' not in st.session_state: st.session_state.f_idx = 0
if 'performance' not in st.session_state: st.session_state.performance = []
if 'los_notes' not in st.session_state: st.session_state.los_notes = ""

# --- SIDEBAR: CONTROLS ---
st.sidebar.title("📟 Command Center")
std = st.sidebar.selectbox("Standard Selection", list(st.session_state.master_db.keys()))
lvl = st.sidebar.radio("Difficulty Level", ["Hard-Learning", "Above-Exam Level"])

active_pool = [q for q in st.session_state.master_db.get(std, []) if q['level'] == lvl]

if st.sidebar.button(f"🔄 Reset {std}"):
    st.session_state.q_idx = 0
    st.session_state.f_idx = 0
    st.rerun()

# --- MAIN INTERFACE ---
t1, t2, t3, t4 = st.tabs(["🎯 Practice Tank", "🗂️ Flashcards", "📊 Performance Lab", "📓 LOS Notes"])

with t1: # PRACTICE TANK
    if not active_pool:
        st.info("Tank empty. Data drop incoming.")
    elif st.session_state.q_idx >= len(active_pool):
        st.success(f"🏁 {std} ({lvl}) Complete! Reset in the sidebar.")
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
        with st.expander("👁️ Front"): st.write(card['front'])
        with st.expander("🧠 Back"): st.info(card['back'])
        col1, col2 = st.columns(2)
        if col1.button("⬅️ Previous"): st.session_state.f_idx = max(0, st.session_state.f_idx - 1); st.rerun()
        if col2.button("Next ➡️"): st.session_state.f_idx = min(len(f_pool)-1, st.session_state.f_idx + 1); st.rerun()

with t4: # LOS NOTES
    st.header("Personal LOS Notes")
    st.session_state.los_notes = st.text_area("Record insights here:", value=st.session_state.los_notes, height=400)
    st.button("💾 Save to Library")
