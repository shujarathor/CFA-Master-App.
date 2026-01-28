import streamlit as st
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# ==============================================================================
# 1. CONFIGURATION & STYLE
# ==============================================================================
st.set_page_config(page_title="CFA Master System", layout="wide")

st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; font-weight: bold; background-color: #0052cc; color: white;}
    .stProgress > div > div > div > div {background-color: #0052cc;}
    div[data-testid="stExpander"] {background-color: #f8f9fa; border-radius: 10px; border: 1px solid #e0e0e0;}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. THE GRAPH ENGINE
# ==============================================================================
def get_chart(chart_type):
    fig = go.Figure()
    layout_args = dict(height=300, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor='rgba(0,0,0,0)')
    
    if chart_type == "elastic":
        x = np.linspace(0, 10, 100); y = 10 - 0.5 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#0052cc', width=4), name='Demand'))
        fig.update_layout(title="Elastic Demand", xaxis_title="Q", yaxis_title="P", **layout_args)
        
    elif chart_type == "inelastic":
        x = np.linspace(0, 5, 100); y = 10 - 2 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#d93025', width=4), name='Demand'))
        fig.update_layout(title="Inelastic Demand", xaxis_title="Q", yaxis_title="P", **layout_args)

    elif chart_type == "perfect_competition":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=[5]*100, mode='lines', line=dict(color='#0052cc', width=4), name='P=MR'))
        fig.update_layout(title="Perfect Competition (Price Taker)", xaxis_title="Q", yaxis_title="P", **layout_args)

    elif chart_type == "shift_right":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=10-x, mode='lines', line=dict(color='grey', dash='dot'), name='D'))
        fig.add_trace(go.Scatter(x=x, y=x, mode='lines', line=dict(color='black'), name='S1'))
        fig.add_trace(go.Scatter(x=x, y=x-2, mode='lines', line=dict(color='green', width=3), name='S2 (Shift)'))
        fig.update_layout(title="Supply Shift Right", xaxis_title="Q", yaxis_title="P", **layout_args)
        
    return fig

# ==============================================================================
# 3. THE DATA STRUCTURE
# ==============================================================================
library = {
    "Economics": {
        "LOS 1: Topics in Demand and Supply Analysis": {
            "Hard (Exam Level)": [
                {"q": "If cross-price elasticity is negative, the goods are:", "opt": ["Substitutes", "Complements", "Inferior"], "ans": "Complements", "why": "Price of A up -> Demand for B down."},
                {"q": "Income elasticity is 1.5. The good is:", "opt": ["Necessity", "Luxury", "Inferior"], "ans": "Luxury", "why": "Income elasticity > 1."},
                {"q": "A price ceiling set BELOW equilibrium results in:", "opt": ["Surplus", "Shortage", "No Effect"], "ans": "Shortage", "why": "Qd > Qs at the capped price."},
                {"q": "Substitution effect is always:", "opt": ["Positive", "Negative", "Ambiguous"], "ans": "Negative", "why": "Higher price always encourages substitution away."},
                {"q": "In the elastic region, a Price Decrease leads to:", "opt": ["Higher Revenue", "Lower Revenue", "Same Revenue"], "ans": "Higher Revenue", "why": "%Q increase > %P decrease.", "chart": "elastic"},
                {"q": "Unit Elastic Demand means Marginal Revenue is:", "opt": ["Positive", "Negative", "Zero"], "ans": "Zero", "why": "Total Revenue is maximized at unit elasticity."},
                {"q": "Consumer Surplus is the area:", "opt": ["Below Demand Above Price", "Above Supply Below Price", "Below Supply"], "ans": "Below Demand Above Price", "why": "Difference between willingness to pay and price paid."},
                {"q": "For a Giffen Good, the demand curve slopes:", "opt": ["Upward", "Downward", "Vertical"], "ans": "Upward", "why": "Negative Income effect > Substitution effect."},
                {"q": "Deadweight loss represents:", "opt": ["Allocative Inefficiency", "Excess Profit", "Tax Revenue"], "ans": "Allocative Inefficiency", "why": "Loss of total surplus due to market distortion."},
                {"q": "The tax burden falls on the consumer if Demand is:", "opt": ["Elastic", "Inelastic", "Perfectly Elastic"], "ans": "Inelastic", "why": "Consumers cannot switch away, so they pay the tax.", "chart": "inelastic"}
            ],
            "Brutal (Above Exam)": [
                {"q": "For a Giffen Good, the Income Effect is:", "opt": ["Negative & < Sub Effect", "Negative & > Sub Effect", "Positive"], "ans": "Negative & > Sub Effect", "why": "Strong negative income effect dominates substitution effect."},
                {"q": "Stable Cobweb model requires:", "opt": ["Supply steeper than Demand", "Demand steeper than Supply", "Slopes equal"], "ans": "Demand steeper than Supply", "why": "Demand must be less elastic than supply for convergence."},
                {"q": "If Demand is P = 100 - 2Q, Marginal Revenue (MR) is:", "opt": ["100 - 2Q", "100 - 4Q", "100 - Q"], "ans": "100 - 4Q", "why": "MR has twice the slope of a linear Demand curve."},
                {"q": "Utility Maximization condition:", "opt": ["MUx = MUy", "MUx/Px = MUy/Py", "Px = Py"], "ans": "MUx/Px = MUy/Py", "why": "Marginal utility per dollar must be equal across goods."},
                {"q": "Slope of the Indifference Curve is:", "opt": ["MRS", "MRT", "MPL"], "ans": "MRS", "why": "Marginal Rate of Substitution (willingness to trade)."},
                {"q": "Income Elast -0.5, Price Elast -0.4. Price +10%, Income +10%. Q change?", "opt": ["-9%", "-1%", "+1%"], "ans": "-9%", "why": "(-0.4*10) + (-0.5*10) = -4% - 5% = -9%."},
                {"q": "Quota Rent accrues to:", "opt": ["Government", "License Holder", "Consumer"], "ans": "License Holder", "why": "The importer captures the price gap."},
                {"q": "A Subsidy benefits the producer most if Demand is:", "opt": ["Perfectly Elastic", "Perfectly Inelastic", "Unit Elastic"], "ans": "Perfectly Elastic", "why": "Price doesn't fall for consumers, so producers keep the full subsidy."},
                {"q": "Production function Q = K^0.6 L^0.5. Returns to Scale?", "opt": ["Constant", "Decreasing", "Increasing"], "ans": "Increasing", "why": "Exponents sum to 1.1 (>1)."},
                {"q": "Linear Demand intercept elasticity is:", "opt": ["Zero", "One", "Infinity"], "ans": "Infinity", "why": "At the Y-intercept, Q is zero, making ratio infinite."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Elasticity Formula", "ans": "%ΔQ / %ΔP", "why": "Measure of responsiveness."},
                {"q": "Giffen Good", "ans": "Inferior + Upward Sloping", "why": "Income Effect > Substitution Effect."},
                {"q": "Consumer Surplus", "ans": "Area below D, above P", "why": "Net benefit to buyers."},
                {"q": "Deadweight Loss", "ans": "Lost Total Surplus", "why": "Inefficiency marker."},
                {"q": "Cross Elasticity (+)", "ans": "Substitutes", "why": "Move together."},
                {"q": "Cross Elasticity (-)", "ans": "Complements", "why": "Move opposite."},
                {"q": "Normal Good", "ans": "Income Elast > 0", "why": "Buy more as you get richer."},
                {"q": "Inferior Good", "ans": "Income Elast < 0", "why": "Buy less as you get richer."},
                {"q": "Price Floor", "ans": "Min Price (Surplus)", "why": "Set above equilibrium."},
                {"q": "Price Ceiling", "ans": "Max Price (Shortage)", "why": "Set below equilibrium."}
            ]
        },
        "LOS 2: The Firm and Market Structures": {
            "Hard (Exam Level)": [
                {"q": "Perfect Competition Demand Curve is:", "opt": ["Horizontal", "Vertical", "Downward"], "ans": "Horizontal", "why": "Firm is a Price Taker.", "chart": "perfect_competition"},
                {"q": "Profit Maximization Rule for ALL firms:", "opt": ["MR = MC", "P = ATC", "TR = TC"], "ans": "MR = MC", "why": "Universal rule for max profit."},
                {"q": "Monopolistic Competition products are:", "opt": ["Identical", "Differentiated", "Unique"], "ans": "Differentiated", "why": "Differentiation allows some pricing power."},
                {"q": "Kinked Demand Curve explains:", "opt": ["Price Rigidity in Oligopoly", "Monopoly Pricing", "Perfect Comp"], "ans": "Price Rigidity in Oligopoly", "why": "Competitors follow price cuts but ignore hikes."},
                {"q": "Natural Monopoly arises from:", "opt": ["Economies of Scale", "Legal Barriers", "Collusion"], "ans": "Economies of Scale", "why": "Declining ATC over the entire range of demand."},
                {"q": "Nash Equilibrium definition:", "opt": ["Optimal joint outcome", "Best response to rival", "Cheating"], "ans": "Best response to rival", "why": "No incentive to deviate unilaterally."},
                {"q": "HHI (Herfindahl-Hirschman Index) measures:", "opt": ["Concentration", "Elasticity", "Inflation"], "ans": "Concentration", "why": "Sum of squared market shares."},
                {"q": "Cartels fail mainly because:", "opt": ["Incentive to cheat", "Government regulations", "Low profits"], "ans": "Incentive to cheat", "why": "Individual MR > MC creates incentive to overproduce."},
                {"q": "Shutdown Point in Short Run:", "opt": ["P < AVC", "P < ATC", "P < MC"], "ans": "P < AVC", "why": "Revenue cannot even cover variable costs."},
                {"q": "Breakeven Point:", "opt": ["P = ATC", "P = AVC", "MR = MC"], "ans": "P = ATC", "why": "Zero Economic Profit."},
                {"q": "First-Degree Price Discrimination:", "opt": ["Zero Consumer Surplus", "High Consumer Surplus", "Deadweight Loss"], "ans": "Zero Consumer Surplus", "why": "Monopolist extracts all surplus."},
                {"q": "Long Run Profit in Monopolistic Competition:", "opt": ["Zero", "Positive", "Negative"], "ans": "Zero", "why": "Low barriers to entry erode profit."},
                {"q": "Concentration Ratio (N-Firm):", "opt": ["Sum of top N shares", "Sum of squared shares", "Gini Coeff"], "ans": "Sum of top N shares", "why": "Simple measure of market control."},
                {"q": "Oligopoly is characterized by:", "opt": ["Interdependence", "Independence", "Price Taking"], "ans": "Interdependence", "why": "Strategic gaming is key."},
                {"q": "Supply Curve for Monopoly:", "opt": ["Undefined", "MC Curve", "Upward Sloping"], "ans": "Undefined", "why": "No unique P-Q relationship; depends on Demand shift."}
            ],
            "Brutal (Above Exam)": [
                {"q": "Cournot Model variable:", "opt": ["Quantity", "Price", "Capacity"], "ans": "Quantity", "why": "Firms choose Q simultaneously."},
                {"q": "Bertrand Model variable:", "opt": ["Price", "Quantity", "Entry"], "ans": "Price", "why": "Price war drives P down to MC."},
                {"q": "Stackelberg Model feature:", "opt": ["Leader/Follower", "Simultaneous moves", "Collusion"], "ans": "Leader/Follower", "why": "First mover advantage exists."},
                {"q": "Dominant Firm Model sets price based on:", "opt": ["Residual Demand", "Market Demand", "Marginal Cost"], "ans": "Residual Demand", "why": "Market Demand minus Fringe Supply."},
                {"q": "HHI for a Monopoly (1 firm):", "opt": ["10,000", "1,000", "100"], "ans": "10,000", "why": "100 squared = 10,000."},
                {"q": "Allocative Efficiency occurs when:", "opt": ["P = MC", "P = ATC", "MR = MC"], "ans": "P = MC", "why": "Value to consumer equals cost of production."},
                {"q": "X-Inefficiency refers to:", "opt": ["Waste due to lack of competition", "Deadweight Loss", "Allocative Loss"], "ans": "Waste due to lack of competition", "why": "Monopolies become lazy on costs."},
                {"q": "Lerner Index formula:", "opt": ["(P-MC)/P", "P/MC", "MC/P"], "ans": "(P-MC)/P", "why": "Measures market power markup."},
                {"q": "Second-Degree Price Discrimination:", "opt": ["Quantity Discounts", "Identity-based", "Time-based"], "ans": "Quantity Discounts", "why": "Based on volume purchased."},
                {"q": "Collusion is unstable if:", "opt": ["Cheater MR > MC", "Cheater P < ATC", "High Penalty"], "ans": "Cheater MR > MC", "why": "Profit motive to break agreement."},
                {"q": "Kinked Demand Gap is in the:", "opt": ["MR Curve", "MC Curve", "ATC Curve"], "ans": "MR Curve", "why": "Discontinuity due to asymmetric elasticity."},
                {"q": "Productive Efficiency:", "opt": ["Min ATC", "Min AVC", "P=MC"], "ans": "Min ATC", "why": "Producing at lowest possible cost."},
                {"q": "Dual-Curve Monopoly transforms:", "opt": ["Consumer Surplus to Producer Surplus", "DWL to Tax", "PS to CS"], "ans": "Consumer Surplus to Producer Surplus", "why": "Extracts willingness to pay."},
                {"q": "Contestable Market Theory:", "opt": ["Threat of entry disciplines firms", "Regulation is needed", "High Barriers"], "ans": "Threat of entry disciplines firms", "why": "Hit-and-run entry keeps prices low."},
                {"q": "Porter's 5 Forces - High Switching Costs:", "opt": ["Low Buyer Power", "High Buyer Power", "High Rivalry"], "ans": "Low Buyer Power", "why": "Customers are locked in."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Perfect Competition", "ans": "Many firms, Identical Product, Price Taker", "why": "Horizontal Demand."},
                {"q": "Monopoly", "ans": "One Firm, Unique Product, Price Maker", "why": "High Barriers."},
                {"q": "Oligopoly", "ans": "Few Firms, Interdependent", "why": "Strategic behavior."},
                {"q": "Monopolistic Competition", "ans": "Differentiated Products, Low Barriers", "why": "Zero LR Economic Profit."},
                {"q": "HHI", "ans": "Sum of Squared Market Shares", "why": "Concentration Metric."},
                {"q": "Nash Equilibrium", "ans": "Best response to opponent's strategy", "why": "Game Theory core."},
                {"q": "Natural Monopoly", "ans": "Falling ATC over relevant range", "why": "Economies of Scale."},
                {"q": "Profit Max", "ans": "MR = MC", "why": "Always."},
                {"q": "Shutdown Point (SR)", "ans": "P < AVC", "why": "Cash flow negative."},
                {"q": "Breakeven", "ans": "P = ATC", "why": "Zero Economic Profit."}
            ]
        },
        "LOS 3: Aggregate Output, Prices, and Growth": {
            "Hard (Exam Level)": [
                {"q": "GDP Deflator formula:", "opt": ["Nominal GDP / Real GDP", "Real / Nominal", "CPI / PPI"], "ans": "Nominal GDP / Real GDP", "why": "Measures price level changes."},
                {"q": "Structural Unemployment:", "opt": ["Skills Mismatch", "Business Cycle", "Voluntary"], "ans": "Skills Mismatch", "why": "Long-term shift in economy."},
                {"q": "Frictional Unemployment:", "opt": ["Job Search Gap", "Recession", "Skills Gap"], "ans": "Job Search Gap", "why": "Short-term transition."},
                {"q": "Cyclical Unemployment:", "opt": ["Recession Related", "Voluntary", "Seasonal"], "ans": "Recession Related", "why": "Caused by low Aggregate Demand."},
                {"q": "Natural Rate of Unemployment includes:", "opt": ["Frictional + Structural", "Cyclical + Frictional", "Zero Unemployment"], "ans": "Frictional + Structural", "why": "Unemployment when economy is at full potential."},
                {"q": "Agg Demand shifts Right if:", "opt": ["Taxes Decrease", "Rates Increase", "Imports Rise"], "ans": "Taxes Decrease", "why": "More disposable income."},
                {"q": "Short Run Agg Supply (SRAS) shifts Left if:", "opt": ["Input Costs Rise", "Tech Improves", "Taxes Fall"], "ans": "Input Costs Rise", "why": "Cost-push inflation."},
                {"q": "Long Run Agg Supply (LRAS) is:", "opt": ["Vertical", "Horizontal", "Upward Sloping"], "ans": "Vertical", "why": "determined by potential output, independent of price."},
                {"q": "Recessionary Gap:", "opt": ["Real GDP < Potential GDP", "Real GDP > Potential", "Full Employment"], "ans": "Real GDP < Potential GDP", "why": "High unemployment."},
                {"q": "Inflationary Gap:", "opt": ["Real GDP > Potential GDP", "Real GDP < Potential", "Deflation"], "ans": "Real GDP > Potential GDP", "why": "Upward pressure on prices."},
                {"q": "Sustainable Growth Rate:", "opt": ["Retention Rate x ROE", "Dividend Payout x ROE", "NI / Sales"], "ans": "Retention Rate x ROE", "why": "g = b * ROE."},
                {"q": "Solow Growth Model Long Run driver:", "opt": ["Technology", "Capital", "Labor"], "ans": "Technology", "why": "Capital hits diminishing returns."},
                {"q": "Capital Deepening:", "opt": ["Increase in Capital per Worker", "Increase in Tech", "Increase in Labor"], "ans": "Increase in Capital per Worker", "why": "Moving along the productivity curve."},
                {"q": "Stagflation:", "opt": ["High Inflation + High Unemployment", "Low Infl + Low Unemp", "High Growth"], "ans": "High Inflation + High Unemployment", "why": "Caused by SRAS shift left."},
                {"q": "Participation Rate:", "opt": ["Labor Force / Working Age Pop", "Employed / Labor Force", "Unemployed / Pop"], "ans": "Labor Force / Working Age Pop", "why": "Measure of active workforce."}
            ],
            "Brutal (Above Exam)": [
                {"q": "Bernoulli's Hypothesis (Utility):", "opt": ["Marginal Utility Diminishes", "Utility is Linear", "Risk Loving"], "ans": "Marginal Utility Diminishes", "why": "Concave utility function implies risk aversion."},
                {"q": "IS Curve represents equilibrium in:", "opt": ["Goods Market", "Money Market", "Labor Market"], "ans": "Goods Market", "why": "Investment = Savings."},
                {"q": "LM Curve represents equilibrium in:", "opt": ["Money Market", "Goods Market", "Forex"], "ans": "Money Market", "why": "Liquidity Preference = Money Supply."},
                {"q": "Neoclassical Growth Theory assumes:", "opt": ["Diminishing Returns to Capital", "Constant Returns", "Increasing Returns"], "ans": "Diminishing Returns to Capital", "why": "Leads to steady state."},
                {"q": "Endogenous Growth Theory assumes:", "opt": ["Returns to Capital don't diminish", "Diminishing Returns", "Exogenous Tech"], "ans": "Returns to Capital don't diminish", "why": "R&D/Knowledge spillover prevents stagnation."},
                {"q": "Dutch Disease:", "opt": ["Resource boom hurts manufacturing", "Banking crisis", "High Inflation"], "ans": "Resource boom hurts manufacturing", "why": "Currency appreciation makes exports uncompetitive."},
                {"q": "Okun's Law Relationship:", "opt": ["Inverse: GDP and Unemployment", "Direct: GDP and Inflation", "Inverse: Inflation/Unemp"], "ans": "Inverse: GDP and Unemployment", "why": "High growth reduces unemployment."},
                {"q": "Phillips Curve (Short Run):", "opt": ["Inflation vs Unemployment tradeoff", "Tax vs Revenue", "Growth vs Rates"], "ans": "Inflation vs Unemployment tradeoff", "why": "Inverse relationship."},
                {"q": "Phillips Curve (Long Run):", "opt": ["Vertical at NAIRU", "Downward Sloping", "Horizontal"], "ans": "Vertical at NAIRU", "why": "No tradeoff in LR; money is neutral."},
                {"q": "Laspeyres Index Bias:", "opt": ["Upward (Substitution Bias)", "Downward", "None"], "ans": "Upward (Substitution Bias)", "why": "Ignores consumers switching to cheaper goods."},
                {"q": "Paasche Index uses:", "opt": ["Current weights", "Base weights", "Average weights"], "ans": "Current weights", "why": "Underestimates inflation due to substitution."},
                {"q": "Fisher Index:", "opt": ["Geometric Mean of Laspeyres & Paasche", "Arithmetic Mean", "Sum"], "ans": "Geometric Mean of Laspeyres & Paasche", "why": "Removes bias."},
                {"q": "Cost-Push Inflation caused by:", "opt": ["Left shift in SRAS", "Right shift in AD", "Money Supply"], "ans": "Left shift in SRAS", "why": "Supply shock (e.g., Oil price spike)."},
                {"q": "Demand-Pull Inflation caused by:", "opt": ["Right shift in AD", "Right shift in SRAS", "Productivity"], "ans": "Right shift in AD", "why": "Too much money chasing too few goods."},
                {"q": "Liquidity Trap:", "opt": ["Monetary policy ineffective", "Fiscal ineffective", "High Rates"], "ans": "Monetary policy ineffective", "why": "Demand for money is perfectly elastic at zero bound."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "GDP Deflator", "ans": "Nominal / Real", "why": "Price Index."},
                {"q": "Frictional Unemp", "ans": "Job Search Gap", "why": "Short Term."},
                {"q": "Structural Unemp", "ans": "Skills Mismatch", "why": "Long Term."},
                {"q": "Cyclical Unemp", "ans": "Recession / Low AD", "why": "Bad Economy."},
                {"q": "Stagflation", "ans": "High Infl + High Unemp", "why": "Supply Shock."},
                {"q": "LRAS Curve", "ans": "Vertical", "why": "Potential Output."},
                {"q": "Recessionary Gap", "ans": "Real < Potential GDP", "why": "Deflationary pressure."},
                {"q": "Inflationary Gap", "ans": "Real > Potential GDP", "why": "Price pressure."},
                {"q": "Sustainable Growth", "ans": "Retention Rate * ROE", "why": "g = b * ROE."},
                {"q": "Diminishing Returns", "ans": "MPK falls as K rises", "why": "Solow Model key."}
            ]
        },
        "LOS 4: Understanding Business Cycles": { "Hard (Exam Level)": [], "Brutal (Above Exam)": [], "Flashcards (10 Cards)": [] },
        "LOS 5: Monetary and Fiscal Policy": { "Hard (Exam Level)": [], "Brutal (Above Exam)": [], "Flashcards (10 Cards)": [] },
        "LOS 6: International Trade and Capital Flows": { "Hard (Exam Level)": [], "Brutal (Above Exam)": [], "Flashcards (10 Cards)": [] },
        "LOS 7: Currency Exchange Rates": { "Hard (Exam Level)": [], "Brutal (Above Exam)": [], "Flashcards (10 Cards)": [] },
        "MOCK EXAM": {
            "Full Mock": []
        }
    }
}
        
# 4. STATE MANAGEMENT
# ==============================================================================
if 'history' not in st.session_state: st.session_state.history = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'checked' not in st.session_state: st.session_state.checked = False
if 'fc_flipped' not in st.session_state: st.session_state.fc_flipped = False
if 'm_idx' not in st.session_state: st.session_state.m_idx = 0
if 'm_score' not in st.session_state: st.session_state.m_score = 0

# ==============================================================================
# 5. THE INTERFACE
# ==============================================================================
st.sidebar.title("🧭 CFA Ecosystem")

# MODULE SELECTOR
if not library["Economics"]:
    st.warning("⚠️ Database Empty. Please Paste Data Blocks into 'library' dictionary.")
    st.stop()

los_keys = list(library["Economics"].keys())
# Filter out Mock from LOS dropdown
practice_keys = [k for k in los_keys if "MOCK" not in k]

if practice_keys:
    selected_los = st.sidebar.selectbox("Select LOS", practice_keys)
else:
    selected_los = None

# RESET BUTTON
if st.sidebar.button("🔄 Reset All"):
    for key in ['q_idx', 'score', 'checked', 'fc_flipped', 'm_idx', 'm_score']:
        if key in st.session_state: del st.session_state[key]
    st.rerun()

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice Questions", "🃏 Flashcards", "💀 Brutal Mock", "📊 Performance"])

# --- TAB 1: PRACTICE ---
with tab1:
    if selected_los:
        available_levels = [k for k in library["Economics"][selected_los].keys() if "Flashcard" not in k]
        level = st.radio("Difficulty", available_levels, horizontal=True)
        
        q_list = library["Economics"][selected_los][level]
        total = len(q_list)
        idx = st.session_state.q_idx
        
        if idx < total:
            q = q_list[idx]
            # Progress
            c1, c2 = st.columns([5,1])
            c1.progress((idx)/total)
            c2.markdown(f"**{st.session_state.score}/{total}**")
            
            # Content
            if "chart" in q: st.plotly_chart(get_chart(q['chart']), use_container_width=True)
            st.markdown(f"### Q{idx+1}: {q['q']}")
            choice = st.radio("Select:", q['opt'], key=f"q_{idx}")
            
            # Logic
            b1, b2 = st.columns(2)
            if b1.button("Check Answer"): st.session_state.checked = True
            
            if st.session_state.checked:
                if choice == q['ans']:
                    st.success(f"✅ Correct! \n\n{q['why']}")
                    if f"done_{idx}" not in st.session_state:
                        st.session_state.score += 1
                        st.session_state[f"done_{idx}"] = True
                else:
                    st.error(f"❌ Wrong. Answer: {q['ans']} \n\n{q['why']}")
                
                if b2.button("Next ➡️"):
                    st.session_state.q_idx += 1
                    st.session_state.checked = False
                    st.rerun()
        else:
            st.balloons()
            st.success("Module Complete!")
            # Save to History
            st.session_state.history.append({
                "Time": datetime.now().strftime("%H:%M"), 
                "Module": selected_los, 
                "Score": f"{st.session_state.score}/{total}"
            })

# --- TAB 2: FLASHCARDS ---
with tab2:
    if selected_los and "Flashcards (10 Cards)" in library["Economics"][selected_los]:
        fc_deck = library["Economics"][selected_los]["Flashcards (10 Cards)"]
        fc_idx = st.session_state.get("fc_idx", 0)
        
        if fc_idx < len(fc_deck):
            card = fc_deck[fc_idx]
            with st.container(border=True):
                st.caption(f"Card {fc_idx+1}/{len(fc_deck)}")
                if not st.session_state.fc_flipped:
                    st.markdown(f"## {card['q']}")
                    if st.button("Flip 🔄"): st.session_state.fc_flipped = True; st.rerun()
                else:
                    st.markdown(f"## {card['ans']}")
                    st.info(card['why'])
                    if st.button("Next Card ➡️"): 
                        st.session_state.fc_idx = fc_idx + 1
                        st.session_state.fc_flipped = False
                        st.rerun()
        else:
            st.button("Restart Deck", on_click=lambda: st.session_state.update({"fc_idx":0}))

# --- TAB 3: MOCK EXAM ---
with tab3:
    st.header("💀 The 300-Question Mock")
    if "MOCK EXAM" in library["Economics"]:
        mock_qs = library["Economics"]["MOCK EXAM"]["Full Mock"]
        m_idx = st.session_state.m_idx
        
        if m_idx < len(mock_qs):
            mq = mock_qs[m_idx]
            st.progress(m_idx/len(mock_qs))
            st.write(f"**Mock Q{m_idx+1}**")
            st.markdown(f"### {mq['q']}")
            m_choice = st.radio("Select:", mq['opt'], key=f"m_{m_idx}")
            
            if st.button("Submit Mock Answer"):
                if m_choice == mq['ans']: 
                    st.success("Correct")
                    st.session_state.m_score += 1
                else: 
                    st.error(f"Wrong. Answer: {mq['ans']}")
                
                if st.button("Next Mock Q"):
                    st.session_state.m_idx += 1
                    st.rerun()
        else:
            st.success(f"Mock Complete! Score: {st.session_state.m_score}/{len(mock_qs)}")

# --- TAB 4: PERFORMANCE ---
with tab4:
    if st.session_state.history:
        st.dataframe(st.session_state.history)
    else:
        st.info("No practice sessions completed yet.")
