import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# ==============================================================================
# 1. APP CONFIGURATION & STYLE
# ==============================================================================
st.set_page_config(page_title="CFA Economics Ultimate", layout="wide")

st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; font-weight: bold; background-color: #0052cc; color: white; border: none;}
    .stButton>button:active {background-color: #003d99;}
    div[data-testid="stExpander"] {background-color: #f8f9fa; border-radius: 10px; border: 1px solid #e0e0e0;}
    .stProgress > div > div > div > div {background-color: #0052cc;}
    h1, h2, h3 {font-family: 'Helvetica Neue', sans-serif;}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. THE CHART ENGINE
# ==============================================================================
def get_chart(chart_type):
    fig = go.Figure()
    layout_args = dict(height=300, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='#ffffff')
    
    if chart_type == "elastic":
        x = np.linspace(0, 10, 100); y = 10 - 0.5 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#0052cc', width=4), name='Demand'))
        fig.update_layout(title="Elastic Demand", xaxis_title="Q", yaxis_title="P", **layout_args)
    elif chart_type == "inelastic":
        x = np.linspace(0, 5, 100); y = 10 - 2 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#d93025', width=4), name='Demand'))
        fig.update_layout(title="Inelastic Demand", xaxis_title="Q", yaxis_title="P", **layout_args)
    return fig

# ==============================================================================
# 3. THE MASTER DATABASE (FULL SYLLABUS STRUCTURE)
# ==============================================================================
library = {
    "Economics": {
        "LOS 1: Topics in Demand and Supply Analysis": {
            "Hard (15 Qs)": [
                {"q": "Cross-price elasticity is negative. The goods are:", "opt": ["Substitutes", "Complements", "Inferior"], "ans": "Complements", "why": "Price of A up -> Demand for B down."},
                {"q": "Income elasticity is 1.5. The good is:", "opt": ["Necessity", "Luxury", "Inferior"], "ans": "Luxury", "why": "Income elasticity > 1."},
                {"q": "Price ceiling below equilibrium causes:", "opt": ["Surplus", "Shortage", "No Effect"], "ans": "Shortage", "why": "Qd > Qs."},
                {"q": "Substitution effect is always:", "opt": ["Positive", "Negative", "Ambiguous"], "ans": "Negative", "why": "Higher price leads to substitution away."},
                {"q": "In elastic region, Price Decrease leads to:", "opt": ["Higher Revenue", "Lower Revenue", "Same Revenue"], "ans": "Higher Revenue", "why": "%Q increase > %P decrease.", "chart": "elastic"},
                {"q": "Unit Elastic Demand means MR is:", "opt": ["Positive", "Negative", "Zero"], "ans": "Zero", "why": "Revenue is maximized."},
                {"q": "Consumer Surplus is area:", "opt": ["Below Demand Above Price", "Above Supply Below Price", "Below Supply"], "ans": "Below Demand Above Price", "why": "Willingness to pay minus price."},
                {"q": "Giffen Good demand curve slopes:", "opt": ["Upward", "Downward", "Vertical"], "ans": "Upward", "why": "Income effect > Substitution effect."},
                {"q": "Deadweight loss occurs when:", "opt": ["Allocative Efficiency", "Market Distortion", "Perfect Comp"], "ans": "Market Distortion", "why": "Loss of total surplus."},
                {"q": "Arc Elasticity uses:", "opt": ["Initial Price", "Final Price", "Average Price"], "ans": "Average Price", "why": "Midpoint method."},
                {"q": "Veblen Good appeal is based on:", "opt": ["Price", "Status", "Quality"], "ans": "Status", "why": "Higher price = higher utility."},
                {"q": "Tax burden falls on consumer if Demand is:", "opt": ["Elastic", "Inelastic", "Perfectly Elastic"], "ans": "Inelastic", "why": "They cannot switch away.", "chart": "inelastic"},
                {"q": "Minimum Wage is a:", "opt": ["Price Ceiling", "Price Floor", "Quota"], "ans": "Price Floor", "why": "Minimum price for labor."},
                {"q": "If Supply shifts right and Demand stays, P and Q?", "opt": ["P down Q up", "P up Q down", "P up Q up"], "ans": "P down Q up", "why": "Surplus drives price down."},
                {"q": "Normal Profit includes:", "opt": ["Accounting Profit", "Opportunity Cost", "Economic Rent"], "ans": "Opportunity Cost", "why": "Zero economic profit."}
            ],
            "Brutal (15 Qs)": [
                {"q": "For a Giffen Good, the Income Effect is:", "opt": ["Negative and smaller than Sub Effect", "Negative and larger than Sub Effect", "Positive"], "ans": "Negative and larger than Sub Effect", "why": "Strong negative income effect dominates."},
                {"q": "Stable Cobweb model requires:", "opt": ["Supply steeper than Demand", "Demand steeper than Supply", "Equal slopes"], "ans": "Demand steeper than Supply", "why": "Demand less elastic than supply."},
                {"q": "If Demand is P = 100 - 2Q, what is MR?", "opt": ["100 - 2Q", "100 - 4Q", "100 - Q"], "ans": "100 - 4Q", "why": "MR has twice the slope of Demand."},
                {"q": "Utility Maximization condition:", "opt": ["MUx = MUy", "MUx/Px = MUy/Py", "Px = Py"], "ans": "MUx/Px = MUy/Py", "why": "Marginal utility per dollar."},
                {"q": "Slope of Indifference Curve is:", "opt": ["MRS", "MRT", "MPL"], "ans": "MRS", "why": "Marginal Rate of Substitution."},
                {"q": "Income Elasticity -0.5 and Price Elasticity -0.4. 10% Price Up, 10% Income Up. Q change?", "opt": ["-9%", "-1%", "1%"], "ans": "-9%", "why": "-4% (Price) + -5% (Income) = -9%."},
                {"q": "Quota Rent goes to:", "opt": ["Government", "License Holder", "Consumer"], "ans": "License Holder", "why": "Importer captures price gap."},
                {"q": "Subsidy benefit goes to producer if Demand is:", "opt": ["Perfectly Elastic", "Perfectly Inelastic", "Unit Elastic"], "ans": "Perfectly Elastic", "why": "Price doesn't fall for consumers."},
                {"q": "Production function Q = K^0.6 L^0.5. Returns to Scale?", "opt": ["Constant", "Decreasing", "Increasing"], "ans": "Increasing", "why": "0.6 + 0.5 = 1.1 (>1)."},
                {"q": "Linear Demand intercept elasticity is:", "opt": ["0", "1", "Infinity"], "ans": "Infinity", "why": "Q is zero."},
                {"q": "Effective Price Ceiling causes:", "opt": ["Excess Supply", "Excess Demand", "Equilibrium"], "ans": "Excess Demand", "why": "Shortage."},
                {"q": "Long Run Supply elasticity is usually:", "opt": ["Higher than Short Run", "Lower", "Same"], "ans": "Higher than Short Run", "why": "More factors variable."},
                {"q": "Negative production externality implies:", "opt": ["MSC > MPC", "MPC > MSC", "MPB > MSB"], "ans": "MSC > MPC", "why": "Social cost > Private cost."},
                {"q": "Coase Theorem requires:", "opt": ["Low Transaction Costs", "Government Intervention", "High Taxes"], "ans": "Low Transaction Costs", "why": "Efficient bargaining."},
                {"q": "Inferior Good Substitution Effect is:", "opt": ["Positive", "Negative", "Zero"], "ans": "Negative", "why": "Sub effect is always negative."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Elasticity Formula", "ans": "%ΔQ / %ΔP", "why": "Responsiveness"}, {"q": "Giffen Good", "ans": "Inferior + Upward Sloping", "why": "Income > Sub Effect"},
                {"q": "Consumer Surplus", "ans": "Area below D above P", "why": "Net Benefit"}, {"q": "Deadweight Loss", "ans": "Lost Total Surplus", "why": "Inefficiency"},
                {"q": "Cross Elasticity (+)", "ans": "Substitutes", "why": "Move together"}, {"q": "Cross Elasticity (-)", "ans": "Complements", "why": "Move opposite"},
                {"q": "Normal Good", "ans": "Income Elasticity > 0", "why": "Buy more as rich"}, {"q": "Inferior Good", "ans": "Income Elasticity < 0", "why": "Buy less as rich"},
                {"q": "Price Floor", "ans": "Min Price (Surplus)", "why": "Above Eq"}, {"q": "Price Ceiling", "ans": "Max Price (Shortage)", "why": "Below Eq"}
            ]
        },
        "LOS 2: The Firm and Market Structures": {
            "Hard (15 Qs)": [
                {"q": "Perfect Comp Demand Curve is:", "opt": ["Vertical", "Horizontal", "Downward"], "ans": "Horizontal", "why": "Price Taker."},
                {"q": "Profit Max Rule:", "opt": ["MR=MC", "P=ATC", "TR=TC"], "ans": "MR=MC", "why": "Marginal Revenue = Marginal Cost."},
                {"q": "Monopolistic Comp Product:", "opt": ["Identical", "Differentiated", "Unique"], "ans": "Differentiated", "why": "Brand power."},
                {"q": "Kinked Demand Curve Model:", "opt": ["Oligopoly", "Monopoly", "Perfect Comp"], "ans": "Oligopoly", "why": "Sticky prices."},
                {"q": "Natural Monopoly cause:", "opt": ["Economies of Scale", "Patents", "Collusion"], "ans": "Economies of Scale", "why": "Falling ATC."},
                {"q": "Nash Equilibrium:", "opt": ["Optimal joint outcome", "Best response to rival", "Cheating"], "ans": "Best response to rival", "why": "No incentive to deviate."},
                {"q": "HHI Measures:", "opt": ["Elasticity", "Concentration", "Inflation"], "ans": "Concentration", "why": "Sum squared shares."},
                {"q": "Cartels fail because:", "opt": ["Incentive to cheat", "Legal barriers", "Low profits"], "ans": "Incentive to cheat", "why": "Individual gain > Group gain."},
                {"q": "Shutdown Point (SR):", "opt": ["P < AVC", "P < ATC", "P < MC"], "ans": "P < AVC", "why": "Can't cover variable costs."},
                {"q": "Breakeven Point:", "opt": ["P = ATC", "P = AVC", "MR = MC"], "ans": "P = ATC", "why": "Zero economic profit."},
                {"q": "1st Degree Price Discrim:", "opt": ["No Consumer Surplus", "High Consumer Surplus", "DWL"], "ans": "No Consumer Surplus", "why": "Perfect discrimination."},
                {"q": "Long Run Monopolistic Comp Profit:", "opt": ["Positive", "Zero", "Negative"], "ans": "Zero", "why": "Entry erodes profit."},
                {"q": "Concentration Ratio:", "opt": ["Sum of top N shares", "Sum of squared shares", "Gini coeff"], "ans": "Sum of top N shares", "why": "Market power metric."},
                {"q": "Oligopoly Interdependence:", "opt": ["High", "Low", "None"], "ans": "High", "why": "Strategic behavior."},
                {"q": "Monopoly Supply Curve:", "opt": ["MC curve", "Upward sloping", "Undefined"], "ans": "Undefined", "why": "Depends on Demand shift."}
            ],
            "Brutal (15 Qs)": [
                {"q": "Cournot Model variable:", "opt": ["Price", "Quantity", "Capacity"], "ans": "Quantity", "why": "Simultaneous Q choice."},
                {"q": "Bertrand Model variable:", "opt": ["Price", "Quantity", "Entry"], "ans": "Price", "why": "Price war to MC."},
                {"q": "Stackelberg Model:", "opt": ["Leader/Follower", "Simultaneous", "Collusive"], "ans": "Leader/Follower", "why": "First mover advantage."},
                {"q": "Dominant Firm Model price:", "opt": ["Market Demand", "Residual Demand", "Marginal Cost"], "ans": "Residual Demand", "why": "Given fringe supply."},
                {"q": "Monopoly HHI (1 firm):", "opt": ["100", "1000", "10000"], "ans": "10000", "why": "100^2."},
                {"q": "Allocative Efficiency:", "opt": ["P=MC", "P=ATC", "MR=MC"], "ans": "P=MC", "why": "Value = Cost."},
                {"q": "X-Inefficiency:", "opt": ["Tech progress", "Waste/Sloth", "Allocative loss"], "ans": "Waste/Sloth", "why": "Lack of competition."},
                {"q": "Lerner Index:", "opt": ["(P-MC)/P", "P/MC", "MC/P"], "ans": "(P-MC)/P", "why": "Market power."},
                {"q": "2nd Degree Price Discrim:", "opt": ["Quantity", "Identity", "Time"], "ans": "Quantity", "why": "Bulk discounts."},
                {"q": "Collusion instability condition:", "opt": ["Cheater MR > MC", "Cheater P < ATC", "High penalty"], "ans": "Cheater MR > MC", "why": "Profit in cheating."},
                {"q": "Kinked Demand Gap in:", "opt": ["MR Curve", "MC Curve", "ATC Curve"], "ans": "MR Curve", "why": "Discontinuous MR."},
                {"q": "Productive Efficiency:", "opt": ["Min ATC", "Min AVC", "P=MC"], "ans": "Min ATC", "why": "Lowest cost production."},
                {"q": "Dual Curve Monopoly transforms:", "opt": ["CS to PS", "PS to CS", "DWL to Tax"], "ans": "CS to PS", "why": "Extracts surplus."},
                {"q": "Contestable Market Theory:", "opt": ["Threat of entry disciplines", "Regulation needed", "High barriers"], "ans": "Threat of entry disciplines", "why": "Hit and run entry."},
                {"q": "Porter's 5 Forces - High Switch Cost:", "opt": ["Low Buyer Power", "High Buyer Power", "High Rivalry"], "ans": "Low Buyer Power", "why": "Lock-in."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Perfect Comp", "ans": "Many firms, Price Taker", "why": "Horizontal D"}, {"q": "Monopoly", "ans": "One firm, Price Maker", "why": "High Barriers"},
                {"q": "Oligopoly", "ans": "Few firms, Interdependent", "why": "Strategic"}, {"q": "Monopolistic Comp", "ans": "Diff Products, Low Barriers", "why": "Zero LR Profit"},
                {"q": "HHI", "ans": "Sum Sq Shares", "why": "Concentration"}, {"q": "Nash Eq", "ans": "Best Response", "why": "Game Theory"},
                {"q": "Natural Monopoly", "ans": "Falling ATC", "why": "Economies of Scale"}, {"q": "Profit Max", "ans": "MR = MC", "why": "Always"},
                {"q": "Shutdown SR", "ans": "P < AVC", "why": "Cash flow neg"}, {"q": "Breakeven", "ans": "P = ATC", "why": "Zero Econ Profit"}
            ]
        },
        "LOS 3: Aggregate Output, Prices, and Growth": {"Hard (15 Qs)": [], "Brutal (15 Qs)": [], "Flashcards (10 Cards)": []},
        "LOS 4: Understanding Business Cycles": {"Hard (15 Qs)": [], "Brutal (15 Qs)": [], "Flashcards (10 Cards)": []},
        "LOS 5: Monetary and Fiscal Policy": {"Hard (15 Qs)": [], "Brutal (15 Qs)": [], "Flashcards (10 Cards)": []},
        "LOS 6: International Trade and Capital Flows": {"Hard (15 Qs)": [], "Brutal (15 Qs)": [], "Flashcards (10 Cards)": []},
        "LOS 7: Currency Exchange Rates": {"Hard (15 Qs)": [], "Brutal (15 Qs)": [], "Flashcards (10 Cards)": []},
        "MOCK EXAM": {
            "Brutal (Sample 50 Qs)": [
                {"q": "Nominal GDP grows 5%, Velocity constant. Money Supply growth?", "opt": ["5%", "0%", "10%"], "ans": "5%", "why": "MV=PY."},
                {"q": "Fisher Effect: Nominal Rate =", "opt": ["Real + Exp Infl", "Real - Infl", "Infl / Real"], "ans": "Real + Exp Infl", "why": "Approx."},
                {"q": "Ricardian Equivalence:", "opt": ["Deficit has no demand effect", "Deficit stimulates", "Surplus hurts"], "ans": "Deficit has no demand effect", "why": "Future tax exp."},
                {"q": "J-Curve Effect:", "opt": ["Trade balance worsens then improves", "Improves then worsens", "Stay same"], "ans": "Trade balance worsens then improves", "why": "Price vs Vol adj."},
                {"q": "Crowding Out:", "opt": ["Govt borrow raises rates", "Inv increases", "Tax cuts work"], "ans": "Govt borrow raises rates", "why": "Less pvt invest."},
                {"q": "Liquidity Trap:", "opt": ["Monetary policy ineffective", "Fiscal ineffective", "High rates"], "ans": "Monetary policy ineffective", "why": "Rates at zero."},
                {"q": "Stagflation:", "opt": ["High Infl + High Unemp", "Low Infl + Low Unemp", "High Growth"], "ans": "High Infl + High Unemp", "why": "Supply shock."},
                {"q": "Cost-Push Inflation:", "opt": ["Agg Supply shift left", "Agg Demand shift right", "Money supply"], "ans": "Agg Supply shift left", "why": "Higher input costs."},
                {"q": "Demand-Pull Inflation:", "opt": ["AD shift right", "AS shift left", "Tech shock"], "ans": "AD shift right", "why": "Excess demand."},
                {"q": "Okun's Law:", "opt": ["GDP and Unemployment", "Inflation and Unemp", "Tax and Rev"], "ans": "GDP and Unemployment", "why": "Inverse relationship."},
                {"q": "Phillips Curve (SR):", "opt": ["Inflation vs Unemp", "Tax vs Rev", "Growth vs Int Rate"], "ans": "Inflation vs Unemp", "why": "Tradeoff."},
                {"q": "Money Multiplier:", "opt": ["1/Reserve Ratio", "1/Tax Rate", "1/MPS"], "ans": "1/Reserve Ratio", "why": "Max credit creation."},
                {"q": "Fractional Reserve Banking:", "opt": ["Banks lend fraction of deposits", "Keep 100%", "No lending"], "ans": "Banks lend fraction of deposits", "why": "Creates money."},
                {"q": "Central Bank buys bonds:", "opt": ["Money Supply Up", "Rates Up", "Reserves Down"], "ans": "Money Supply Up", "why": "Injection."},
                {"q": "Fiscal Multiplier:", "opt": ["1/(1-MPC)", "1/MPC", "1/Tax"], "ans": "1/(1-MPC)", "why": "Spending cycle."},
                {"q": "Structural Unemployment:", "opt": ["Mismatch skills", "Business cycle", "Job search"], "ans": "Mismatch skills", "why": "Long term."},
                {"q": "Frictional Unemployment:", "opt": ["Job search gap", "Recession", "Skills gap"], "ans": "Job search gap", "why": "Short term."},
                {"q": "Cyclical Unemployment:", "opt": ["Recession related", "Skills gap", "Voluntary"], "ans": "Recession related", "why": "Low AD."},
                {"q": "Real GDP measures:", "opt": ["Output at base prices", "Output at current prices", "Happiness"], "ans": "Output at base prices", "why": "Adjusted for infl."},
                {"q": "GDP Deflator:", "opt": ["Nominal/Real", "Real/Nominal", "CPI/PPI"], "ans": "Nominal/Real", "why": "Price index."},
                {"q": "Current Account Deficit implies:", "opt": ["Capital Account Surplus", "Trade Surplus", "Govt Surplus"], "ans": "Capital Account Surplus", "why": "BoP must balance."},
                {"q": "Purchasing Power Parity:", "opt": ["Law of One Price", "Interest Rates equal", "Growth equal"], "ans": "Law of One Price", "why": "Exch rate adj."},
                {"q": "Interest Rate Parity:", "opt": ["Forward/Spot diff = Int Rate diff", "Inflation diff", "Growth diff"], "ans": "Forward/Spot diff = Int Rate diff", "why": "No arbitrage."},
                {"q": "Marshall-Lerner Condition:", "opt": ["Elast Exp + Elast Imp > 1", "Sum < 1", "Sum = 0"], "ans": "Elast Exp + Elast Imp > 1", "why": "Depreciation improves TB."},
                {"q": "Comparative Advantage:", "opt": ["Lower Opp Cost", "Absolute Cost", "Tech"], "ans": "Lower Opp Cost", "why": "Trade basis."},
                {"q": "Heckscher-Ohlin Theory:", "opt": ["Factor endowments", "Tech diff", "Taste diff"], "ans": "Factor endowments", "why": "Labor vs Capital rich."},
                {"q": "Laspeyres Index:", "opt": ["Base year weights", "Current year weights", "Fisher"], "ans": "Base year weights", "why": "CPI method."},
                {"q": "Paasche Index:", "opt": ["Current year weights", "Base weights", "Geo mean"], "ans": "Current year weights", "why": "GDP Deflator."},
                {"q": "Diminishing Marginal Returns:", "opt": ["MPL falls as L rises", "MPL rises", "APL constant"], "ans": "MPL falls as L rises", "why": "Fixed capital."},
                {"q": "Solow Growth Model long run:", "opt": ["Tech progress", "Capital accumulation", "Pop growth"], "ans": "Tech progress", "why": "Steady state."},
                {"q": "Sustainable Growth Rate:", "opt": ["ROE * b", "ROA * b", "NI/Equity"], "ans": "ROE * b", "why": "Retention ratio."},
                {"q": "Automatic Stabilizers:", "opt": ["Tax/Welfare", "Fed Rates", "Infra spend"], "ans": "Tax/Welfare", "why": "No legislation needed."},
                {"q": "Discretionary Fiscal Policy:", "opt": ["New laws/spending", "Unemployment ben", "Taxes"], "ans": "New laws/spending", "why": "Active choice."},
                {"q": "Expansionary Gap:", "opt": ["Actual > Potential GDP", "Actual < Potential", "Zero"], "ans": "Actual > Potential GDP", "why": "Inflation risk."},
                {"q": "Recessionary Gap:", "opt": ["Actual < Potential GDP", "Actual > Potential", "Zero"], "ans": "Actual < Potential GDP", "why": "Unemployment."},
                {"q": "Quantity Theory of Money:", "opt": ["MV = PY", "MP = VY", "M/P = Y"], "ans": "MV = PY", "why": "Monetarist base."},
                {"q": "Neutrality of Money:", "opt": ["Money affects prices not output (LR)", "Affects output", "Affects nothing"], "ans": "Money affects prices not output (LR)", "why": "Real variables unchanged."},
                {"q": "Say's Law:", "opt": ["Supply creates Demand", "Demand creates Supply", "Prices rigid"], "ans": "Supply creates Demand", "why": "Classical view."},
                {"q": "Keynesian View:", "opt": ["Demand drives output", "Supply drives output", "Money neutral"], "ans": "Demand drives output", "why": "Sticky prices."},
                {"q": "Laffer Curve:", "opt": ["Tax Rate vs Revenue", "Inf vs Unemp", "Equality vs Growth"], "ans": "Tax Rate vs Revenue", "why": "Optimal tax rate."},
                {"q": "Lorenz Curve:", "opt": ["Inequality", "Tax", "Growth"], "ans": "Inequality", "why": "Wealth dist."},
                {"q": "Gini Coefficient:", "opt": ["0=Perfect Equality", "1=Equality", "0=Inequality"], "ans": "0=Perfect Equality", "why": "Area under Lorenz."},
                {"q": "Spot Rate:", "opt": ["Immediate delivery", "Future", "Option"], "ans": "Immediate delivery", "why": "T+2."},
                {"q": "Forward Rate:", "opt": ["Future delivery", "Spot", "Swap"], "ans": "Future delivery", "why": "Hedging."},
                {"q": "Real Exchange Rate:", "opt": ["Nominal x (CPI_for / CPI_dom)", "Nominal x (CPI_dom / CPI_for)", "Nominal"], "ans": "Nominal x (CPI_for / CPI_dom)", "why": "Purchasing power."},
                {"q": "Balance of Payments:", "opt": ["Always Balances (Sum=0)", "Surplus", "Deficit"], "ans": "Always Balances (Sum=0)", "why": "Accounting identity."},
                {"q": "Autarky:", "opt": ["No Trade", "Free Trade", "Tariffs"], "ans": "No Trade", "why": "Closed economy."},
                {"q": "Protective Tariff:", "opt": ["Protect domestic Ind", "Revenue", "Punish"], "ans": "Protect domestic Ind", "why": "Import sub."},
                {"q": "Infant Industry Argument:", "opt": ["Protect new ind", "Protect old", "Free trade"], "ans": "Protect new ind", "why": "Until scale reached."},
                {"q": "Dumping:", "opt": ["Selling below cost abroad", "Polluting", "Subsidizing"], "ans": "Selling below cost abroad", "why": "Predatory."}
            ]
        }
    }
}

# ==============================================================================
# 4. STATE MANAGEMENT & UI
# ==============================================================================
if 'history' not in st.session_state: st.session_state.history = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'checked' not in st.session_state: st.session_state.checked = False
if 'fc_flipped' not in st.session_state: st.session_state.fc_flipped = False

# SIDEBAR
st.sidebar.title("🧭 CFA Navigator")
module_key = "Economics" # Hardcoded for this app
los_list = list(library[module_key].keys())
# Remove Mock from LOS list for the dropdown
los_list_clean = [x for x in los_list if "MOCK" not in x]
los_key = st.sidebar.selectbox("Learning Outcome (LOS)", los_list_clean)

if st.sidebar.button("🔄 Reset"):
    st.session_state.q_idx = 0; st.session_state.score = 0; st.session_state.checked = False; st.session_state.fc_flipped = False; st.rerun()

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice", "🃏 Flashcards", "💀 Mock Exam", "📊 History"])

# TAB 1: PRACTICE
with tab1:
    types = [k for k in library[module_key][los_key].keys() if "Flashcard" not in k]
    if types:
        diff = st.radio("Level", types, horizontal=True)
        q_list = library[module_key][los_key][diff]
        if q_list:
            q_idx = st.session_state.q_idx
            if q_idx < len(q_list):
                q = q_list[q_idx]
                st.progress((q_idx)/len(q_list))
                st.caption(f"Q {q_idx+1}/{len(q_list)} | Score: {st.session_state.score}")
                if "chart" in q: st.plotly_chart(get_chart(q['chart']), use_container_width=True)
                st.subheader(q['q'])
                choice = st.radio("Select:", q['opt'], key=f"q_{q_idx}")
                
                c1, c2 = st.columns(2)
                if c1.button("Check"): st.session_state.checked = True
                
                if st.session_state.checked:
                    if choice == q['ans']:
                        st.success(f"✅ Correct! \n\n{q['why']}")
                        if f"done_{q_idx}" not in st.session_state: st.session_state.score += 1; st.session_state[f"done_{q_idx}"] = True
                    else:
                        st.error(f"❌ Wrong. Answer: {q['ans']}. \n\nReason: {q['why']}")
                    
                    if c2.button("Next"): st.session_state.q_idx += 1; st.session_state.checked = False; st.rerun()
            else:
                st.balloons()
                st.success(f"Done! Score: {st.session_state.score}")
        else:
            st.info("Questions coming for this LOS.")
    else:
        st.info("No questions loaded.")

# TAB 2: FLASHCARDS
with tab2:
    if "Flashcards (10 Cards)" in library[module_key][los_key]:
        fc_list = library[module_key][los_key]["Flashcards (10 Cards)"]
        if fc_list:
            fc_idx = st.session_state.get("fc_idx", 0)
            if fc_idx < len(fc_list):
                card = fc_list[fc_idx]
                with st.container(border=True):
                    st.caption(f"Card {fc_idx+1}/{len(fc_list)}")
                    if not st.session_state.fc_flipped:
                        st.markdown(f"## {card['q']}")
                        if st.button("Flip"): st.session_state.fc_flipped = True; st.rerun()
                    else:
                        st.markdown(f"## {card['ans']}")
                        st.info(card['why'])
                        if st.button("Next Card"): st.session_state.fc_idx = fc_idx + 1; st.session_state.fc_flipped = False; st.rerun()
            else:
                st.success("Deck Done!")
                if st.button("Restart Deck"): st.session_state.fc_idx = 0; st.rerun()
        else: st.info("Flashcards coming.")

# TAB 3: MOCK
with tab3:
    st.header("💀 The Mock")
    mock_list = library[module_key]["MOCK EXAM"]["Brutal (Sample 50 Qs)"]
    m_idx = st.session_state.get("m_idx", 0)
    if m_idx < len(mock_list):
        mq = mock_list[m_idx]
        st.markdown(f"**Mock Q{m_idx+1}**")
        st.write(mq['q'])
        m_opt = st.radio("Select:", mq['opt'], key=f"m_{m_idx}")
        if st.button("Submit Mock Answer"):
            if m_opt == mq['ans']: st.success("Correct")
            else: st.error(f"Wrong. {mq['ans']}")
            if st.button("Next Mock"): st.session_state.m_idx = m_idx + 1; st.rerun()
    else: st.success("Mock Complete")

# TAB 4: HISTORY
with tab4:
    if st.session_state.history: st.dataframe(pd.DataFrame(st.session_state.history))
    else: st.write("No history.")
