import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# ==============================================================================
# 1. APP CONFIGURATION
# ==============================================================================
st.set_page_config(page_title="CFA Economics Master", layout="wide")

# CSS for "App-Like" Feel on iPad
st.markdown("""
<style>
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; font-weight: bold; background-color: #0052cc; color: white; border: none;}
    .stButton>button:active {background-color: #003d99;}
    div[data-testid="stExpander"] {background-color: #f8f9fa; border-radius: 10px; border: 1px solid #e0e0e0;}
    .stProgress > div > div > div > div {background-color: #0052cc;}
    .stTabs [data-baseweb="tab-list"] {gap: 10px;}
    .stTabs [data-baseweb="tab"] {height: 50px; white-space: pre-wrap; background-color: #f0f2f6; border-radius: 10px 10px 0 0;}
    .stTabs [aria-selected="true"] {background-color: #0052cc; color: white;}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. THE CHART ENGINE (Dynamic Graph Generation)
# ==============================================================================
def get_chart(chart_type):
    fig = go.Figure()
    layout_args = dict(height=300, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='#f8f9fa')
    
    if chart_type == "elastic":
        x = np.linspace(0, 10, 100); y = 10 - 0.5 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#0052cc', width=4), name='Demand'))
        fig.update_layout(title="Elastic Demand (Flatter)", xaxis_title="Quantity", yaxis_title="Price", **layout_args)
        
    elif chart_type == "inelastic":
        x = np.linspace(0, 5, 100); y = 10 - 2 * x
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#d93025', width=4), name='Demand'))
        fig.update_layout(title="Inelastic Demand (Steep)", xaxis_title="Quantity", yaxis_title="Price", **layout_args)
        
    elif chart_type == "shift_right":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=10-x, mode='lines', line=dict(color='grey', dash='dot'), name='Demand'))
        fig.add_trace(go.Scatter(x=x, y=x, mode='lines', line=dict(color='black'), name='Supply 1'))
        fig.add_trace(go.Scatter(x=x, y=x-2, mode='lines', line=dict(color='#188038', width=3), name='Supply 2 (Shift)'))
        fig.update_layout(title="Supply Shift Right", xaxis_title="Q", yaxis_title="P", **layout_args)

    elif chart_type == "perfect_competition":
        x = np.linspace(0, 10, 100)
        fig.add_trace(go.Scatter(x=x, y=[5]*100, mode='lines', line=dict(color='#0052cc', width=4), name='MR = P'))
        fig.update_layout(title="Perfect Competition (Price Taker)", xaxis_title="Q", yaxis_title="P", **layout_args)

    return fig

# ==============================================================================
# 3. THE DATABASE (300+ Questions Architecture)
# ==============================================================================
# Structure: Module -> LOS -> Type (Hard/Brutal/Flashcard) -> List
library = {
    "Economics": {
        "LOS 1: Topics in Demand and Supply Analysis": {
            "Hard (15 Qs)": [
                {"q": "If the cross-price elasticity between two goods is negative, the goods are:", "opt": ["Substitutes", "Complements", "Inferior"], "ans": "Complements", "why": "Negative Cross-Price Elasticity means as Price of A goes up, Demand for B goes down."},
                {"q": "Refer to 'Elastic Demand' Chart. If price decreases in the elastic region, Total Revenue will:", "opt": ["Increase", "Decrease", "Stay Same"], "ans": "Increase", "why": "In elastic region, %ΔQ > %ΔP, so TR rises.", "chart": "elastic"},
                {"q": "Income elasticity of demand is +1.5. This good is:", "opt": ["Inferior", "Normal (Necessity)", "Normal (Luxury)"], "ans": "Normal (Luxury)", "why": "Income Elasticity > 1 indicates a luxury good."},
                {"q": "A price ceiling set BELOW the equilibrium price results in:", "opt": ["Surplus", "Shortage", "Equilibrium"], "ans": "Shortage", "why": "Price is forced low, Demand > Supply."},
                {"q": "Refer to 'Inelastic Demand' Chart. The tax burden falls mostly on:", "opt": ["Consumer", "Producer", "Shared Equally"], "ans": "Consumer", "why": "When Demand is inelastic, consumers bear more tax burden.", "chart": "inelastic"},
                {"q": "If the price of a substitute increases, the demand curve for the original good shifts:", "opt": ["Left", "Right", "No Shift"], "ans": "Right", "why": "Consumers switch to the cheaper original good."},
                {"q": "Consumer Surplus is defined as the area:", "opt": ["Below Demand, Above Price", "Above Supply, Below Price", "Below Demand, Above Supply"], "ans": "Below Demand, Above Price", "why": "Difference between willingness to pay and actual price."},
                {"q": "Refer to 'Supply Shift Right'. This shift could be caused by:", "opt": ["Higher Input Costs", "Better Technology", "Fewer Sellers"], "ans": "Better Technology", "why": "Tech improvements lower costs, increasing supply (shift right).", "chart": "shift_right"},
                {"q": "Ideally, a tax should be levied on goods with:", "opt": ["High Elasticity", "Low Elasticity", "Unit Elasticity"], "ans": "Low Elasticity", "why": "Minimizes Deadweight Loss (Ramsey Rule)."},
                {"q": "Minimum Wage is an example of a:", "opt": ["Price Ceiling", "Price Floor", "Quota"], "ans": "Price Floor", "why": "Legally mandated minimum price for labor."},
                {"q": "The Veblen Good violates the Law of Demand because:", "opt": ["It is an inferior good", "Higher price increases utility", "It is a Giffen good"], "ans": "Higher price increases utility", "why": "Status goods; demand rises as price rises."},
                {"q": "If demand is Unit Elastic, Marginal Revenue is:", "opt": ["Positive", "Negative", "Zero"], "ans": "Zero", "why": "TR is maximized when MR = 0 (Unit Elastic point)."},
                {"q": "Deadweight Loss represents:", "opt": ["Lost Tax Revenue", "Reduction in Total Surplus", "Producer Loss"], "ans": "Reduction in Total Surplus", "why": "Allocative inefficiency caused by distortions."},
                {"q": "In the long run, supply elasticity generally:", "opt": ["Increases", "Decreases", "Stays Constant"], "ans": "Increases", "why": "Firms have more time to adjust inputs/capacity."},
                {"q": "A Giffen Good must be:", "opt": ["A Luxury Good", "An Inferior Good", "A Normal Good"], "ans": "An Inferior Good", "why": "Income effect dominates substitution effect for inferior goods."}
            ],
            "Brutal (15 Qs)": [
                {"q": "If Demand is Perfectly Elastic, the incidence of a subsidy benefits:", "opt": ["Producer only", "Consumer only", "Both"], "ans": "Producer only", "why": "If consumers are perfectly price sensitive, they pay the same price; producers keep the subsidy."},
                {"q": "A firm has a production function Q = K^0.5 L^0.5. Returns to scale are:", "opt": ["Increasing", "Decreasing", "Constant"], "ans": "Constant", "why": "0.5 + 0.5 = 1. Constant Returns to Scale."},
                {"q": "Calculating elasticity using the Arc Method avoids:", "opt": ["Starting point bias", "Slope calculation", "Price limits"], "ans": "Starting point bias", "why": "Arc method uses the midpoint/average."},
                {"q": "If Total Revenue = 100Q - 2Q^2, at what Quantity is Revenue maximized?", "opt": ["25", "50", "100"], "ans": "25", "why": "MR = 100 - 4Q. Set MR=0 -> 100=4Q -> Q=25."},
                {"q": "Consumer chooses Bundle A over B. Prices change. Consumer chooses B. This violates:", "opt": ["Transitivity", "Completeness", "WARP (Weak Axiom of Revealed Preference)"], "ans": "WARP (Weak Axiom of Revealed Preference)", "why": "If A was revealed preferred to B, choosing B later when A is affordable violates WARP."},
                {"q": "In a linear demand curve P = a - bQ, slope is -b. Elasticity at intercept is:", "opt": ["Zero", "One", "Infinity"], "ans": "Infinity", "why": "At the Y-intercept, Q approaches 0, so P/Q approaches infinity."},
                {"q": "An effective Price Ceiling causes Deadweight Loss by:", "opt": ["Reducing Quantity Traded", "Increasing Quantity Traded", "Transferring Surplus"], "ans": "Reducing Quantity Traded", "why": "Market quantity is limited to Quantity Supplied (Qs), which is < Equilibrium Q."},
                {"q": "If the income elasticity of demand is -0.5 and the price elasticity is -0.4, a 10% price hike and 10% income hike result in Q change of:", "opt": ["-9%", "-1%", "+1%"], "ans": "-9%", "why": "(-0.4*10%) + (-0.5*10%) = -4% - 5% = -9%."},
                {"q": "Stable Cobweb Model requires:", "opt": ["Supply slope > Demand slope", "Demand slope > Supply slope", "Slopes equal"], "ans": "Demand slope > Supply slope", "why": "Demand must be less elastic (steeper) than supply for convergence."},
                {"q": "Quota Rent accrues to:", "opt": ["Government", "License Holders", "Consumers"], "ans": "License Holders", "why": "The gap between domestic price and world price goes to the importer/licensee."},
                {"q": "Slope of the Indifference Curve is known as:", "opt": ["MRT", "MRS", "MPL"], "ans": "MRS", "why": "Marginal Rate of Substitution."},
                {"q": "For a Giffen Good, the Demand Curve slopes:", "opt": ["Downward", "Upward", "Vertical"], "ans": "Upward", "why": "Price Up -> Quantity Up (Income effect > Substitution effect)."},
                {"q": "Substitution Effect is always:", "opt": ["Positive", "Negative", "Ambiguous"], "ans": "Negative", "why": "Higher price always encourages substitution away, holding utility constant."},
                {"q": "Utility Maximization rule:", "opt": ["MUx = MUy", "MUx/Px = MUy/Py", "Px = Py"], "ans": "MUx/Px = MUy/Py", "why": "Marginal Utility per dollar must be equal across goods."},
                {"q": "Demand function Qd = 120 - 4P. Supply Qs = 2P - 30. Equilibrium Price?", "opt": ["20", "25", "30"], "ans": "25", "why": "120-4P = 2P-30 -> 150=6P -> P=25."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Formula for Price Elasticity of Demand", "ans": "% Change in Q / % Change in P", "why": "Measure of responsiveness."},
                {"q": "Giffen Good Definition", "ans": "Inferior good where Income Effect > Substitution Effect", "why": "Demand curve slopes upward."},
                {"q": "Veblen Good", "ans": "High-status good where Price Up = Utility Up", "why": "Violates law of demand due to status signaling."},
                {"q": "Consumer Surplus (Visual)", "ans": "Area Below Demand and Above Market Price", "why": "Value received vs. price paid."},
                {"q": "Deadweight Loss", "ans": "Loss of total surplus due to market inefficiency", "why": "Occurs with taxes, ceilings, floors, monopolies."},
                {"q": "Cross-Price Elasticity (Complements)", "ans": "Negative", "why": "Price of A up -> Demand for B down."},
                {"q": "Cross-Price Elasticity (Substitutes)", "ans": "Positive", "why": "Price of A up -> Demand for B up."},
                {"q": "Income Elasticity > 1", "ans": "Luxury Good", "why": "Demand rises faster than income."},
                {"q": "Income Elasticity < 0", "ans": "Inferior Good", "why": "Demand falls as income rises."},
                {"q": "Shutdown Point (Short Run)", "ans": "Price < Average Variable Cost (AVC)", "why": "Revenue doesn't cover variable costs."}
            ]
        },
        "LOS 2: The Firm and Market Structures": {
            "Hard (15 Qs)": [
                {"q": "Refer to 'Perfect Comp' Chart. The demand curve facing a single firm is:", "opt": ["Horizontal", "Vertical", "Downward Sloping"], "ans": "Horizontal", "why": "Firm is a price taker; MR = P.", "chart": "perfect_competition"},
                {"q": "In Monopolistic Competition, products are:", "opt": ["Identical", "Differentiated", "Unique"], "ans": "Differentiated", "why": "Brand loyalty allows some price-setting power."},
                {"q": "The Kinked Demand Curve model describes:", "opt": ["Monopoly", "Oligopoly", "Perfect Competition"], "ans": "Oligopoly", "why": "Competitors follow price cuts but ignore price hikes."},
                {"q": "Herfindahl-Hirschman Index (HHI) measures:", "opt": ["Inflation", "Market Concentration", "Elasticity"], "ans": "Market Concentration", "why": "Sum of squared market shares."},
                {"q": "Nash Equilibrium occurs when:", "opt": ["All firms cheat", "No firm can improve by changing strategy alone", "Joint profits are maximized"], "ans": "No firm can improve by changing strategy alone", "why": "Optimal strategy given the rival's response."},
                {"q": "Natural Monopoly arises due to:", "opt": ["High Economies of Scale", "Legal Barriers", "Control of Resources"], "ans": "High Economies of Scale", "why": "One firm can supply the market at lower AC than two firms."},
                {"q": "Profit Maximization condition for ALL firms:", "opt": ["P = MC", "MR = MC", "TR = TC"], "ans": "MR = MC", "why": "Marginal Revenue equals Marginal Cost."},
                {"q": "In the Long Run, Monopolistic Competitors earn:", "opt": ["Economic Profit", "Zero Economic Profit", "Losses"], "ans": "Zero Economic Profit", "why": "Low barriers to entry erode profits."},
                {"q": "Cartels are most likely to succeed when:", "opt": ["Products are differentiated", "Number of firms is small", "Cost structures differ"], "ans": "Number of firms is small", "why": "Easier to monitor cheating."},
                {"q": "Price Discrimination (1st Degree) results in:", "opt": ["Zero Consumer Surplus", "High Consumer Surplus", "Deadweight Loss"], "ans": "Zero Consumer Surplus", "why": "Monopolist captures entire surplus."},
                {"q": "Concentration Ratio (CR4) considers:", "opt": ["All firms", "Top 4 firms", "Squared shares"], "ans": "Top 4 firms", "why": "Sum of market shares of top 4."},
                {"q": "Average Total Cost (ATC) is minimized when:", "opt": ["MC = ATC", "MC = AVC", "MR = MC"], "ans": "MC = ATC", "why": "MC curve intersects ATC at its minimum."},
                {"q": "Breakeven point is where:", "opt": ["TR = TVC", "AR = ATC", "MR = MC"], "ans": "AR = ATC", "why": "Price (Average Revenue) covers Total Average Cost."},
                {"q": "Game Theory: The Prisoner's Dilemma usually leads to:", "opt": ["Cooperation", "Sub-optimal Outcome", "Pareto Efficiency"], "ans": "Sub-optimal Outcome", "why": "Rational self-interest hurts the group."},
                {"q": "A single seller with no close substitutes:", "opt": ["Monopoly", "Oligopoly", "Monopsony"], "ans": "Monopoly", "why": "High barriers to entry, price maker."}
            ],
            "Brutal (15 Qs)": [
                {"q": "Cournot Model assumes competitors compete on:", "opt": ["Price", "Quantity", "Quality"], "ans": "Quantity", "why": "Firms choose Q assuming rival Q is fixed."},
                {"q": "Bertrand Model assumes competitors compete on:", "opt": ["Price", "Quantity", "Capacity"], "ans": "Price", "why": "Price wars lead to P = MC."},
                {"q": "Stackelberg Model features:", "opt": ["Simultaneous moves", "Leader and Follower", "Collusion"], "ans": "Leader and Follower", "why": "Sequential game; First Mover advantage."},
                {"q": "HHI of a monopoly is:", "opt": ["100", "1,000", "10,000"], "ans": "10,000", "why": "100 squared = 10,000."},
                {"q": "Collusion is unstable because:", "opt": ["MR > MC for the cheater", "P < ATC for the cheater", "Legal penalties are low"], "ans": "MR > MC for the cheater", "why": "Individual incentive to increase Q exceeds group incentive."},
                {"q": "In a Kinked Demand Curve, the MR curve has a:", "opt": ["Vertical Gap", "Horizontal Gap", "Constant Slope"], "ans": "Vertical Gap", "why": "Discontinuity due to asymmetric elasticity."},
                {"q": "Allocative Efficiency is achieved when:", "opt": ["P = MC", "P = ATC", "MR = MC"], "ans": "P = MC", "why": "Value to consumer equals cost of production. Only in Perfect Comp."},
                {"q": "X-Inefficiency refers to:", "opt": ["Deadweight Loss", "Waste due to lack of competition", "Allocative loss"], "ans": "Waste due to lack of competition", "why": "Monopolies get lazy/bloated costs."},
                {"q": "Lerner Index measures:", "opt": ["Market Power (P-MC)/P", "Concentration", "Elasticity"], "ans": "Market Power (P-MC)/P", "why": "Higher index = more markup power."},
                {"q": "Dominant Firm Model: The dominant firm sets price based on:", "opt": ["Market Demand", "Residual Demand", "Supply of Fringe"], "ans": "Residual Demand", "why": "Market Demand minus Fringe Supply."},
                {"q": "Second Degree Price Discrimination is based on:", "opt": ["Identity", "Quantity/Volume", "Location"], "ans": "Quantity/Volume", "why": "Bulk discounts."},
                {"q": "Shutdown Point (Long Run):", "opt": ["P < AVC", "P < ATC", "TR < TFC"], "ans": "P < ATC", "why": "Firm exits if it cannot cover all costs indefinitely."},
                {"q": "Dual-curve monopoly (Price Discrimination) converts:", "opt": ["DWL to Consumer Surplus", "Consumer Surplus to Producer Surplus", "Producer Surplus to Tax"], "ans": "Consumer Surplus to Producer Surplus", "why": "Extracts willingness to pay."},
                {"q": "Porter's 5 Forces: High switching costs:", "opt": ["Increase rivalry", "Decrease Buyer Power", "Increase Threat of Entry"], "ans": "Decrease Buyer Power", "why": "Lock-in effect reduces customer leverage."},
                {"q": "Supply Curve for a Monopoly:", "opt": ["MC curve above AVC", "Upward sloping", "Does Not Exist"], "ans": "Does Not Exist", "why": "No unique P-Q relationship; depends on Demand shift."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Perfect Competition Characteristics", "ans": "Many firms, Identical product, No barriers, P=MR", "why": "Price Takers."},
                {"q": "Monopolistic Competition", "ans": "Many firms, Differentiated products, Low barriers", "why": "Marketing/Brand matters."},
                {"q": "Oligopoly", "ans": "Few firms, High barriers, Interdependence", "why": "Strategic gaming (Game Theory)."},
                {"q": "Monopoly", "ans": "One firm, Unique product, Very high barriers", "why": "Price Maker."},
                {"q": "Profit Max Rule", "ans": "MR = MC", "why": "Universal rule for all structures."},
                {"q": "Nash Equilibrium", "ans": "Optimal strategy given opponent's strategy", "why": "No incentive to deviate."},
                {"q": "Concentration Ratio (N)", "ans": "Sum of market shares of top N firms", "why": "Simple measure of control."},
                {"q": "HHI Calculation", "ans": "Sum of squared market shares (s1^2 + s2^2...)", "why": "More sensitive to mergers."},
                {"q": "Natural Monopoly", "ans": "Declining ATC over entire relevant range of Q", "why": "High fixed costs (Utilities)."},
                {"q": "Kinked Demand Curve", "ans": "Matches price cuts, ignores price hikes", "why": "Sticky prices in Oligopoly."}
            ]
        },
        "MOCK EXAM": {
            "Brutal (Sample Set)": [
                 {"q": "Mock Q1: If nominal GDP grows 5% and velocity is constant, money supply growth must be:", "opt": ["5%", "0%", "10%"], "ans": "5%", "why": "MV = PY. If V is constant, M must match PY."},
                 {"q": "Mock Q2: A central bank targeting 2% inflation in a deflationary spiral should:", "opt": ["Buy Bonds", "Sell Bonds", "Raise Rates"], "ans": "Buy Bonds", "why": "Expansionary policy: Inject liquidity."},
                 {"q": "Mock Q3: Ricardian Equivalence suggests that deficit spending:", "opt": ["Stimulates economy", "Has no effect on Demand", "Causes hyperinflation"], "ans": "Has no effect on Demand", "why": "Public saves more to pay future taxes, offsetting spending."},
                 {"q": "Mock Q4: J-Curve effect: Currency depreciation initially causes Trade Balance to:", "opt": ["Improve", "Worsen", "Stay Flat"], "ans": "Worsen", "why": "Contracts are fixed; import costs rise before volume adjusts."},
                 {"q": "Mock Q5: Fisher Effect: Nominal Rate =", "opt": ["Real + Expected Inflation", "Real - Inflation", "Inflation / Real"], "ans": "Real + Expected Inflation", "why": "Approximation of nominal rate."}
            ]
        }
    }
}

# ==============================================================================
# 4. APP LOGIC & STATE MANAGEMENT
# ==============================================================================
if 'history' not in st.session_state: st.session_state.history = []
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'checked' not in st.session_state: st.session_state.checked = False
if 'fc_flipped' not in st.session_state: st.session_state.fc_flipped = False
if 'active_tab' not in st.session_state: st.session_state.active_tab = "Practice"

# --- SIDEBAR NAV ---
st.sidebar.title("🧭 CFA Navigator")

# 1. Module Selector
module_key = st.sidebar.selectbox("Subject", list(library.keys()))
los_key = st.sidebar.selectbox("Learning Outcome (LOS)", list(library[module_key].keys()))

# 2. Reset Button
if st.sidebar.button("🔄 Reset Session"):
    st.session_state.q_idx = 0
    st.session_state.score = 0
    st.session_state.checked = False
    st.session_state.fc_flipped = False
    st.rerun()

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice Questions", "🃏 Flashcards", "💀 Mock Exam", "📊 Performance"])

# -----------------------------------------------------------------------------
# TAB 1: PRACTICE QUESTIONS (Hard/Brutal)
# -----------------------------------------------------------------------------
with tab1:
    available_sets = [k for k in library[module_key][los_key].keys() if "Flashcard" not in k]
    if not available_sets:
        st.info("No practice questions for this section.")
    else:
        difficulty = st.radio("Difficulty Level", available_sets, horizontal=True)
        q_list = library[module_key][los_key][difficulty]
        total_q = len(q_list)
        
        # Progress
        idx = st.session_state.q_idx
        if idx < total_q:
            q = q_list[idx]
            
            # Header
            c1, c2, c3 = st.columns([1, 6, 1])
            c1.markdown(f"**Q {idx+1}/{total_q}**")
            c2.progress((idx)/total_q)
            c3.markdown(f"**Score: {st.session_state.score}**")
            
            # Chart?
            if "chart" in q:
                st.plotly_chart(get_chart(q['chart']), use_container_width=True)
            
            # Question
            st.markdown(f"### {q['q']}")
            
            # Options
            choice = st.radio("Select Answer:", q['opt'], key=f"p_{idx}")
            
            # Actions
            b1, b2 = st.columns(2)
            if b1.button("Check Answer", key="btn_check"):
                st.session_state.checked = True
            
            if st.session_state.checked:
                if choice == q['ans']:
                    st.success(f"✅ Correct! \n\n{q['why']}")
                    if f"done_{idx}" not in st.session_state:
                        st.session_state.score += 1
                        st.session_state[f"done_{idx}"] = True
                else:
                    st.error(f"❌ Incorrect. \n\n**Correct:** {q['ans']} \n\n**Why:** {q['why']}")
                
                if b2.button("Next Question ➡️", key="btn_next"):
                    st.session_state.q_idx += 1
                    st.session_state.checked = False
                    st.rerun()
        else:
            st.balloons()
            st.success(f"Module Complete! Score: {st.session_state.score}/{total_q}")
            st.session_state.history.append({"Date": datetime.now().strftime("%H:%M"), "Module": los_key, "Score": f"{st.session_state.score}/{total_q}"})

# -----------------------------------------------------------------------------
# TAB 2: FLASHCARDS
# -----------------------------------------------------------------------------
with tab2:
    fc_sets = [k for k in library[module_key][los_key].keys() if "Flashcard" in k]
    if not fc_sets:
        st.warning("No flashcards available for this LOS.")
    else:
        fc_list = library[module_key][los_key][fc_sets[0]]
        fc_idx = st.session_state.get("fc_idx", 0)
        
        if fc_idx < len(fc_list):
            card = fc_list[fc_idx]
            
            # Card Container
            with st.container(border=True):
                st.caption(f"Card {fc_idx+1} of {len(fc_list)}")
                
                if not st.session_state.fc_flipped:
                    st.markdown(f"## {card['q']}")
                    if st.button("🔄 Flip"):
                        st.session_state.fc_flipped = True
                        st.rerun()
                else:
                    st.markdown(f"## {card['ans']}")
                    st.info(card['why'])
                    
                    c1, c2 = st.columns(2)
                    if c1.button("⬅️ Back"):
                        st.session_state.fc_flipped = False
                        st.rerun()
                    if c2.button("Next Card ➡️"):
                        st.session_state.fc_idx = fc_idx + 1
                        st.session_state.fc_flipped = False
                        st.rerun()
        else:
            st.success("Deck Complete!")
            if st.button("Restart Deck"):
                st.session_state.fc_idx = 0
                st.rerun()

# -----------------------------------------------------------------------------
# TAB 3: MOCK EXAM
# -----------------------------------------------------------------------------
with tab3:
    st.header("💀 The Brutal Mock")
    if "MOCK EXAM" in library["Economics"]:
        mock_qs = library["Economics"]["MOCK EXAM"]["Brutal (Sample Set)"]
        # Simple mock logic (reuse Practice logic simplified)
        m_idx = st.session_state.get("m_idx", 0)
        if m_idx < len(mock_qs):
            mq = mock_qs[m_idx]
            st.markdown(f"**Mock Q{m_idx+1}**")
            st.write(mq['q'])
            m_choice = st.radio("Select:", mq['opt'], key=f"m_{m_idx}")
            
            if st.button("Submit Mock Answer"):
                if m_choice == mq['ans']: st.success("Correct")
                else: st.error(f"Wrong. {mq['ans']}")
                
                if st.button("Next Mock Q"):
                    st.session_state.m_idx = m_idx + 1
                    st.rerun()
        else:
            st.success("Mock Complete.")
    else:
        st.write("Mock Data Loading...")

# -----------------------------------------------------------------------------
# TAB 4: PERFORMANCE
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("📊 Session History")
    if st.session_state.history:
        st.dataframe(pd.DataFrame(st.session_state.history))
    else:
        st.write("No sessions recorded yet.")
