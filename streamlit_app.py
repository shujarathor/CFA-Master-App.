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
        # --- LOS 4: FULLY LOADED ---
        "LOS 4: Understanding Business Cycles": {
            "Hard (Exam Level)": [
                {"q": "A Recession is technically defined as:", "opt": ["2 consecutive quarters of declining Real GDP", "High Unemployment", "Market Crash"], "ans": "2 consecutive quarters of declining Real GDP", "why": "Standard technical definition."},
                {"q": "Inventory-to-Sales ratio typically rises when:", "opt": ["Economy hits a Peak", "Economy is in Trough", "Early Expansion"], "ans": "Economy hits a Peak", "why": "Sales slow down but production hasn't adjusted, causing involuntary inventory buildup."},
                {"q": "Leading Economic Indicator example:", "opt": ["S&P 500 Index", "Unemployment Rate", "Industrial Production"], "ans": "S&P 500 Index", "why": "Stock market anticipates future earnings."},
                {"q": "Lagging Economic Indicator example:", "opt": ["Duration of Unemployment", "Building Permits", "Money Supply"], "ans": "Duration of Unemployment", "why": "Firms delay firing/hiring until trend is confirmed."},
                {"q": "Coincident Economic Indicator example:", "opt": ["Personal Income", "Interest Rate Spread", "Orders for Capital Goods"], "ans": "Personal Income", "why": "Happens simultaneously with economic activity."},
                {"q": "Neoclassical School believes business cycles are caused by:", "opt": ["Temporary deviations from long-run equilibrium", "Animal Spirits", "Money Supply"], "ans": "Temporary deviations from long-run equilibrium", "why": "Markets are self-correcting; cycles are short-term blips."},
                {"q": "Keynesian School believes business cycles are driven by:", "opt": ["Aggregate Demand fluctuations", "Technology Shocks", "Central Bank errors"], "ans": "Aggregate Demand fluctuations", "why": "'Animal spirits' and business confidence drive Investment and AD."},
                {"q": "Monetarist School believes recessions are caused by:", "opt": ["Inappropriate Money Supply growth", "Fiscal Deficits", "Market Failure"], "ans": "Inappropriate Money Supply growth", "why": "Central Bank error is the root cause."},
                {"q": "Real Business Cycle (RBC) Theory focuses on:", "opt": ["External Shocks (Tech/Resources)", "Money Supply", "Demand"], "ans": "External Shocks (Tech/Resources)", "why": "Cycles are efficient responses to real external changes."},
                {"q": "During an Expansion, the Output Gap is typically:", "opt": ["Positive (Inflationary)", "Negative (Recessionary)", "Zero"], "ans": "Positive (Inflationary)", "why": "Actual GDP > Potential GDP."},
                {"q": "Discouraged Workers effect on Unemployment Rate:", "opt": ["Lowers it artificialy", "Raises it", "No effect"], "ans": "Lowers it artificialy", "why": "They leave the Labor Force, so they aren't counted as unemployed."},
                {"q": "Underemployed workers are:", "opt": ["Employed part-time but want full-time", "Not working", "Discouraged"], "ans": "Employed part-time but want full-time", "why": "Counted as employed, masking slack in labor market."},
                {"q": "Inflation usually peaks:", "opt": ["Lagging the cycle peak", "Leading the cycle", "Coincident"], "ans": "Lagging the cycle peak", "why": "Prices are sticky; they keep rising even after demand slows."},
                {"q": "The 'Agency Worker' indicator is:", "opt": ["Leading", "Lagging", "Coincident"], "ans": "Leading", "why": "Firms hire temps before committing to full-time staff."},
                {"q": "Capital Spending typically peaks:", "opt": ["Late Expansion", "Early Recession", "Trough"], "ans": "Late Expansion", "why": "Firms finally run out of capacity and invest right before the crash."}
            ],
            "Brutal (Above Exam)": [
                {"q": "Austrian Business Cycle Theory blames:", "opt": ["Artificially low interest rates", "Lack of demand", "Tech shocks"], "ans": "Artificially low interest rates", "why": "Causes 'Malinvestment' in long-term projects that aren't viable."},
                {"q": "In RBC Theory, government intervention is:", "opt": ["Counter-productive", "Necessary", "Neutral"], "ans": "Counter-productive", "why": "Markets are already optimal/efficient; intervention distorts."},
                {"q": "The 'Yield Curve Inversion' (10y - 2y) is the most reliable predictor of:", "opt": ["Recession in 12 months", "Inflation", "Stock Rally"], "ans": "Recession in 12 months", "why": "Short rates > Long rates implies tight money/future slowdown."},
                {"q": "Okun's Law coefficient (approx) suggests 1% excess unemployment equals:", "opt": ["2% Output Gap", "1% Output Gap", "0.5% Output Gap"], "ans": "2% Output Gap", "why": "GDP falls by 2% for every 1% rise in unemployment."},
                {"q": "Labor Participation Rate typically:", "opt": ["Falls during recession (Lagging)", "Rises during recession", "Is constant"], "ans": "Falls during recession (Lagging)", "why": "Cyclical effect: people give up looking."},
                {"q": "Deflation is dangerous because it increases:", "opt": ["Real value of Debt", "Nominal Interest Rates", "Tax Revenue"], "ans": "Real value of Debt", "why": "Fisher Effect: Real Liability rises, crushing borrowers (Debt Deflation)."},
                {"q": "During early expansion, productivity usually:", "opt": ["Rises rapidly", "Falls", "Stays flat"], "ans": "Rises rapidly", "why": "Firms produce more with same staff (hoarding labor pays off)."},
                {"q": "Unit Labor Costs are:", "opt": ["Lagging Indicator", "Leading Indicator", "Coincident"], "ans": "Lagging Indicator", "why": "Wages are sticky and last to adjust."},
                {"q": "Building Permits vs Housing Starts:", "opt": ["Permits lead Starts", "Starts lead Permits", "Coincident"], "ans": "Permits lead Starts", "why": "Paperwork comes before the shovel hits dirt."},
                {"q": "Change in Credit/Debt usage is:", "opt": ["Leading Indicator", "Lagging", "Irrelevant"], "ans": "Leading Indicator", "why": "Credit impulse drives spending changes."},
                {"q": "New Keynesian theory adds what to standard Keynesianism?", "opt": ["Microfoundations & Sticky Prices", "Rational Expectations", "Real Shocks"], "ans": "Microfoundations & Sticky Prices", "why": "Explains WHY prices/wages are sticky using Menu Costs."},
                {"q": "The 'Wealth Effect' connects:", "opt": ["Asset Prices to Consumption", "Income to Savings", "Rates to Investment"], "ans": "Asset Prices to Consumption", "why": "Stocks/Homes up -> People feel rich -> Spend more."},
                {"q": "Hysteresis in Unemployment means:", "opt": ["Cyclical becomes Structural", "Unemployment bounces back", "Wages fall"], "ans": "Cyclical becomes Structural", "why": "Long-term unemployed lose skills and become unemployable."},
                {"q": "Inventory-to-Sales ratio is lowest at:", "opt": ["Late Expansion/Peak", "Trough", "Early Expansion"], "ans": "Late Expansion/Peak", "why": "Sales are maxed out, inventory is flying off shelves (until the turn)."},
                {"q": "Central Bank 'Taylor Rule' guides rates based on:", "opt": ["Inflation Gap + Output Gap", "Gold Price", "Exchange Rate"], "ans": "Inflation Gap + Output Gap", "why": "Balances price stability and growth."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Recession Definition", "ans": "2 Quarters Declining Real GDP", "why": "Technical rule."},
                {"q": "Leading Indicator", "ans": "Predicts future (e.g., Stock Market)", "why": "Changes before economy."},
                {"q": "Lagging Indicator", "ans": "Confirms past (e.g., Unemployment Duration)", "why": "Changes after economy."},
                {"q": "Coincident Indicator", "ans": "Current state (e.g., Industrial Prod)", "why": "Happens now."},
                {"q": "Neoclassical View", "ans": "Cycles are temp deviations", "why": "Self-correcting markets."},
                {"q": "Keynesian View", "ans": "Cycles driven by AD / Animal Spirits", "why": "Govt intervention needed."},
                {"q": "Monetarist View", "ans": "Cycles driven by Money Supply errors", "why": "Keep money growth stable."},
                {"q": "RBC Theory", "ans": "Cycles driven by Real External Shocks", "why": "No policy needed."},
                {"q": "Austrian Theory", "ans": "Low rates cause Malinvestment", "why": "Boom-Bust cycle."},
                {"q": "Output Gap", "ans": "Actual GDP - Potential GDP", "why": "Measure of slack."}
            ]
        },

        # --- LOS 5: FULLY LOADED ---
        "LOS 5: Monetary and Fiscal Policy": {
            "Hard (Exam Level)": [
                {"q": "Money Neutrality implies that in the long run, money supply changes affect:", "opt": ["Prices only", "Real Output", "Velocity"], "ans": "Prices only", "why": "Real variables (Output/Employment) are unaffected by nominal money."},
                {"q": "Fisher Effect: Nominal Interest Rate equals:", "opt": ["Real Rate + Expected Inflation", "Real Rate - Inflation", "Inflation / Real Rate"], "ans": "Real Rate + Expected Inflation", "why": "Approximation of the cost of money."},
                {"q": "A Central Bank's 'Policy Rate' is typically:", "opt": ["The rate at which banks lend to each other overnight", "The 10-Year Bond yield", "The Mortgage Rate"], "ans": "The rate at which banks lend to each other overnight", "why": "It anchors the short end of the yield curve."},
                {"q": "Open Market Operations (Buying Bonds):", "opt": ["Increases Reserves & Lowers Rates", "Decreases Reserves & Raises Rates", "No effect"], "ans": "Increases Reserves & Lowers Rates", "why": "Injects liquidity into the banking system."},
                {"q": "Fractional Reserve Banking means:", "opt": ["Banks hold only a fraction of deposits as reserves", "Banks hold 100% reserves", "Banks cannot lend"], "ans": "Banks hold only a fraction of deposits as reserves", "why": "Allows for credit creation (Money Multiplier)."},
                {"q": "The Money Multiplier (simple) is:", "opt": ["1 / Reserve Requirement", "1 / Tax Rate", "1 / MPS"], "ans": "1 / Reserve Requirement", "why": "Maximum potential credit creation from new reserves."},
                {"q": "Demand for Money (Liquidity Preference) rises if:", "opt": ["Nominal GDP rises", "Interest Rates rise", "Bond prices fall"], "ans": "Nominal GDP rises", "why": "Transaction demand increases with higher income/spending."},
                {"q": "Crowding Out Effect:", "opt": ["Govt borrowing raises rates, lowering Private Investment", "Govt spending lowers rates", "Tax cuts increase Investment"], "ans": "Govt borrowing raises rates, lowering Private Investment", "why": "Public sector absorbs available loanable funds."},
                {"q": "Ricardian Equivalence:", "opt": ["Deficits have no effect on Demand", "Deficits stimulate Demand", "Surpluses hurt Demand"], "ans": "Deficits have no effect on Demand", "why": "Private sector saves more today to pay for expected future taxes."},
                {"q": "Automatic Stabilizers:", "opt": ["Unemployment Insurance / Progressive Taxes", "New Infrastructure Bills", "Rate Cuts"], "ans": "Unemployment Insurance / Progressive Taxes", "why": "Kick in without new legislation during a cycle."},
                {"q": "Discretionary Fiscal Policy:", "opt": ["New Spending Laws", "Tax Receipts falling due to recession", "Welfare"], "ans": "New Spending Laws", "why": "Requires active legislative action."},
                {"q": "Inflation Targeting is a mandate of:", "opt": ["Monetary Policy", "Fiscal Policy", "Trade Policy"], "ans": "Monetary Policy", "why": "Central Bank goal (usually 2%)."},
                {"q": "Liquidity Trap occurs when:", "opt": ["Demand for Money is perfectly elastic", "Rates are high", "Inflation is high"], "ans": "Demand for Money is perfectly elastic", "why": "People hoard cash; lowering rates further is ineffective."},
                {"q": "Expansionary Fiscal Policy + Tight Monetary Policy results in:", "opt": ["Higher Rates", "Lower Rates", "Lower Output"], "ans": "Higher Rates", "why": "Govt borrowing pushes rates up, Fed pushes rates up."},
                {"q": "Quantitative Easing (QE):", "opt": ["Central Bank buys Long-term assets", "CB buys Short-term bills", "CB raises rates"], "ans": "Central Bank buys Long-term assets", "why": "Targets long-end rates when short rates are zero."}
            ],
            "Brutal (Above Exam)": [
                {"q": "Taylor Rule: If Inflation > Target and Output > Potential, the CB should:", "opt": ["Raise Rates aggressively", "Lower Rates", "Do nothing"], "ans": "Raise Rates aggressively", "why": "To cool down the overheating economy."},
                {"q": "Transmission Mechanism: 'Balance Sheet Channel' implies:", "opt": ["Lower rates boost asset prices, improving collateral", "Lower rates boost exports", "Lower rates increase cash"], "ans": "Lower rates boost asset prices, improving collateral", "why": "Better collateral allows more borrowing/lending."},
                {"q": "Structural Deficit:", "opt": ["Deficit that exists at Full Employment", "Cyclical Deficit", "Trade Deficit"], "ans": "Deficit that exists at Full Employment", "why": "Fundamental imbalance, not caused by recession."},
                {"q": "Repo Rate (Repurchase Agreement):", "opt": ["Rate to borrow cash against collateral", "Unsecured lending rate", "Mortgage rate"], "ans": "Rate to borrow cash against collateral", "why": "Secured short-term funding rate."},
                {"q": "Equation of Exchange (Monetarist):", "opt": ["MV = PY", "MP = VY", "M/P = Y"], "ans": "MV = PY", "why": "Money * Velocity = Price * Real Output."},
                {"q": "Negative Interest Rates aim to:", "opt": ["Force banks to lend reserves", "Reward savers", "Reduce inflation"], "ans": "Force banks to lend reserves", "why": "Penalizes holding excess reserves at the CB."},
                {"q": "Fiscal Multiplier is highest when:", "opt": ["MPC is high", "MPS is high", "Tax rate is high"], "ans": "MPC is high", "why": "More spending leads to more rounds of income generation."},
                {"q": "Balanced Budget Multiplier:", "opt": ["Equal to 1", "Equal to 0", "Negative"], "ans": "Equal to 1", "why": "Taxing $1 and spending $1 still boosts GDP by $1 (net)."},
                {"q": "Supply-Side Fiscal Policy focuses on:", "opt": ["Lowering Marginal Tax Rates", "Increasing Transfer Payments", "Lowering Rates"], "ans": "Lowering Marginal Tax Rates", "why": "Incentivizes labor and capital investment (LRAS shift)."},
                {"q": "Lag Time: Monetary Policy has:", "opt": ["Short Implementation, Long Impact Lag", "Long Implementation Lag", "No Lag"], "ans": "Short Implementation, Long Impact Lag", "why": "Fast to decide, slow to affect economy (12-18 months)."},
                {"q": "Lag Time: Fiscal Policy has:", "opt": ["Long Implementation, Short Impact Lag", "Short Implementation", "No Lag"], "ans": "Long Implementation, Short Impact Lag", "why": "Slow to pass laws, fast to affect demand once checks go out."},
                {"q": "Sterilized Intervention:", "opt": ["Forex Op offset by Open Market Op", "Forex Op only", "Capital Control"], "ans": "Forex Op offset by Open Market Op", "why": "Keeps domestic money supply unchanged while managing currency."},
                {"q": "Pay-As-You-Go (PAYGO) rule:", "opt": ["New spending must be offset by revenue/cuts", "Deficits allowed", "Gold standard"], "ans": "New spending must be offset by revenue/cuts", "why": "Fiscal discipline rule."},
                {"q": "Indirect Taxes (VAT/Sales Tax) are:", "opt": ["Regressive", "Progressive", "Neutral"], "ans": "Regressive", "why": "Take a higher % of income from low earners."},
                {"q": "Debt Monetization:", "opt": ["CB buys Govt Debt directly", "Private sector buys Debt", "Paying off debt"], "ans": "CB buys Govt Debt directly", "why": "Printing money to pay bills (Hyperinflation risk)."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Money Neutrality", "ans": "Money affects P, not Y (Long Run)", "why": "Real variables are independent."},
                {"q": "Fisher Effect", "ans": "Nominal R = Real r + Exp Infl", "why": "Interest rate decomp."},
                {"q": "Money Multiplier", "ans": "1 / Reserve Ratio", "why": "Credit creation potential."},
                {"q": "Crowding Out", "ans": "Govt Borrowing -> Rates Up -> Inv Down", "why": "Public replaces Private."},
                {"q": "Ricardian Equiv", "ans": "Deficits don't change Demand", "why": "Future tax expectation."},
                {"q": "Liquidity Trap", "ans": "Monetary Policy ineffective", "why": "Rates at zero/demand flat."},
                {"q": "Stagflation Policy", "ans": "Hard choice (Fight Infl vs Growth)", "why": "Supply shock dilemma."},
                {"q": "Fiscal Multiplier", "ans": "1 / (1 - MPC)", "why": "Spending ripple effect."},
                {"q": "Automatic Stabilizers", "ans": "Taxes & Welfare", "why": "Counter-cyclical without laws."},
                {"q": "Taylor Rule", "ans": "Target Rate formula", "why": "Response to Infl & Output gaps."}
            ]
        },

        # --- LOS 6: FULLY LOADED ---
        "LOS 6: International Trade and Capital Flows": {
            "Hard (Exam Level)": [
                {"q": "Comparative Advantage is based on:", "opt": ["Lower Opportunity Cost", "Lower Absolute Cost", "Higher Quality"], "ans": "Lower Opportunity Cost", "why": "The ability to produce at a lower relative cost than a trading partner."},
                {"q": "The Ricardian Model assumes labor is:", "opt": ["The only factor of production", "One of many factors", "Mobile across countries"], "ans": "The only factor of production", "why": "Focuses on labor productivity differences."},
                {"q": "Heckscher-Ohlin Theory attributes trade to:", "opt": ["Differences in Factor Endowments", "Technology", "Taste"], "ans": "Differences in Factor Endowments", "why": "Capital-rich countries export capital-intensive goods."},
                {"q": "A Tariff imposed by a small country results in:", "opt": ["Deadweight Loss", "Terms of Trade Gain", "Global Efficiency"], "ans": "Deadweight Loss", "why": "Distorts production and consumption without affecting world prices."},
                {"q": "Quota Rent typically accrues to:", "opt": ["The License Holder (Importer)", "The Government", "The Consumer"], "ans": "The License Holder (Importer)", "why": "The price gap between world and domestic price goes to whoever holds the right to import."},
                {"q": "Voluntary Export Restraint (VER):", "opt": ["Country voluntarily limits exports", "Country limits imports", "Tax on exports"], "ans": "Country voluntarily limits exports", "why": "Usually done to avoid a tariff/trade war."},
                {"q": "Current Account includes:", "opt": ["Merchandise, Services, Income, Transfers", "FDI and Portfolio Inv", "Gold Reserves"], "ans": "Merchandise, Services, Income, Transfers", "why": "Tracks flow of goods/services/income."},
                {"q": "Foreign Direct Investment (FDI) is part of the:", "opt": ["Financial/Capital Account", "Current Account", "Reserves"], "ans": "Financial/Capital Account", "why": "Investment in physical assets or control of firms."},
                {"q": "A Free Trade Area (FTA):", "opt": ["Removes barriers between members only", "Adopts common external tariff", "Common Currency"], "ans": "Removes barriers between members only", "why": "Members keep their own tariffs against non-members (e.g., USMCA)."},
                {"q": "A Customs Union adds what to an FTA?", "opt": ["Common External Tariff", "Free movement of labor", "Common Currency"], "ans": "Common External Tariff", "why": "Members treat non-members identically."},
                {"q": "The World Bank's primary mission is:", "opt": ["Reduce Poverty/Development", "Exchange Rate Stability", "Trade Disputes"], "ans": "Reduce Poverty/Development", "why": "Provides loans/grants for development projects."},
                {"q": "The IMF's primary mission is:", "opt": ["Global Monetary Stability", "Infrastructure loans", "Negotiating Tariffs"], "ans": "Global Monetary Stability", "why": "Acts as lender of last resort for BOP crises."},
                {"q": "Dumping is defined as:", "opt": ["Selling below production cost or home price", "Selling low quality goods", "Tax evasion"], "ans": "Selling below production cost or home price", "why": "Predatory pricing behavior."},
                {"q": "Autarky Price:", "opt": ["Price in a closed economy (No Trade)", "World Price", "Tariff Price"], "ans": "Price in a closed economy (No Trade)", "why": "Equilibrium where domestic Supply = Domestic Demand."},
                {"q": "Terms of Trade formula:", "opt": ["Index of Export Prices / Index of Import Prices", "Import P / Export P", "Vol Exp / Vol Imp"], "ans": "Index of Export Prices / Index of Import Prices", "why": "Ratio of export prices to import prices (Px/Pm)."}
            ],
            "Brutal (Above Exam)": [
                {"q": "Leontief Paradox found that the U.S. (Capital rich) exported:", "opt": ["Labor-intensive goods", "Capital-intensive goods", "Land-intensive goods"], "ans": "Labor-intensive goods", "why": "Contradicted Heckscher-Ohlin; explained by human capital (skilled labor)."},
                {"q": "Trade Diversion occurs when:", "opt": ["Regional pact shifts trade from low-cost global to high-cost member", "Trade moves to low-cost member", "Volume decreases"], "ans": "Regional pact shifts trade from low-cost global to high-cost member", "why": "Efficiency loss from preferential trade agreements."},
                {"q": "Marshall-Lerner Condition (Sum of elasticities > 1) ensures:", "opt": ["Depreciation improves Trade Balance", "Appreciation improves Trade Balance", "Stable prices"], "ans": "Depreciation improves Trade Balance", "why": "Volume effect dominates Price effect."},
                {"q": "The J-Curve Effect describes:", "opt": ["Initial worsening of Trade Balance after depreciation", "Immediate improvement", "Steady decline"], "ans": "Initial worsening of Trade Balance after depreciation", "why": "Contracts are fixed in SR; import costs rise before volume adjusts."},
                {"q": "Absorption Approach: Trade Balance (X-M) equals:", "opt": ["National Income (Y) - Domestic Expenditure (E)", "S - I", "T - G"], "ans": "National Income (Y) - Domestic Expenditure (E)", "why": "If we spend more than we earn, we must have a deficit."},
                {"q": "In a Large Country, a Tariff can:", "opt": ["Improve Terms of Trade", "Hurt Terms of Trade", "No effect"], "ans": "Improve Terms of Trade", "why": "Monopsony power forces exporters to lower prices."},
                {"q": "Infant Industry Argument relies on:", "opt": ["Temporary protection to achieve economies of scale", "Permanent protection", "National security"], "ans": "Temporary protection to achieve economies of scale", "why": "Valid only if industry eventually becomes competitive."},
                {"q": "An Export Subsidy by a Large Country:", "opt": ["Worsens its Terms of Trade", "Improves Terms of Trade", "Increases Global Welfare"], "ans": "Worsens its Terms of Trade", "why": "Lowers world price of its export, hurting the subsidizer."},
                {"q": "Economic Union adds what to a Common Market?", "opt": ["Common Economic Institutions/Policy", "Common Tariff", "Free Movement"], "ans": "Common Economic Institutions/Policy", "why": "High integration (e.g., EU)."},
                {"q": "Balance of Payments Identity:", "opt": ["Current Acct + Capital Acct + Official Res = 0", "CA = KA", "X = M"], "ans": "Current Acct + Capital Acct + Official Res = 0", "why": "Every transaction has a debit and credit."},
                {"q": "IMF Conditionality:", "opt": ["Borrowers must adopt austerity/reforms", "Borrowers must join WTO", "None"], "ans": "Borrowers must adopt austerity/reforms", "why": "Requirement for bailout loans."},
                {"q": "Impact of Capital Restrictions:", "opt": ["Prevents Interest Rate Parity from holding", "Ensures PPP", "Increases Efficiency"], "ans": "Prevents Interest Rate Parity from holding", "why": "Disconnects domestic rates from global rates."},
                {"q": "Twin Deficits Hypothesis links:", "opt": ["Fiscal Deficit and Trade Deficit", "Inflation and Unemployment", "Savings and Investment"], "ans": "Fiscal Deficit and Trade Deficit", "why": "Govt borrowing sucks in foreign capital, appreciating currency, hurting exports."},
                {"q": "Effective Rate of Protection:", "opt": ["Considers tariffs on inputs vs outputs", "Just nominal tariff", "Quota equivalent"], "ans": "Considers tariffs on inputs vs outputs", "why": "True protection for value-added."},
                {"q": "Gravity Model of Trade predicts trade based on:", "opt": ["Economic Size and Distance", "Tariffs", "Culture"], "ans": "Economic Size and Distance", "why": "Trade is proportional to GDPs and inversely proportional to distance."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Comparative Advantage", "ans": "Lower Opportunity Cost", "why": "Basis for trade."},
                {"q": "Absolute Advantage", "ans": "Lower Input Cost/Higher Productivity", "why": "Adam Smith."},
                {"q": "Tariff", "ans": "Tax on Imports", "why": "Protects domestic producers."},
                {"q": "Quota", "ans": "Limit on Quantity", "why": "Generates rents."},
                {"q": "Customs Union", "ans": "FTA + Common External Tariff", "why": "Blocks non-members."},
                {"q": "Current Account", "ans": "Goods/Services/Income/Transfers", "why": "Real economy flows."},
                {"q": "Capital Account", "ans": "Asset Transfers/Investments", "why": "Financial flows."},
                {"q": "Balance of Payments", "ans": "Must Sum to Zero", "why": "Accounting Identity."},
                {"q": "J-Curve", "ans": "Depreciation hurts TB at first", "why": "Short run vs Long run."},
                {"q": "Terms of Trade", "ans": "Px / Pm", "why": "Ratio of export/import prices."}
            ]
        },

        # --- LOS 7: FULLY LOADED ---
        "LOS 7: Currency Exchange Rates": {
            "Hard (Exam Level)": [
                {"q": "Spot Exchange Rate definition:", "opt": ["Rate for immediate delivery (T+2)", "Rate for future delivery", "Average rate"], "ans": "Rate for immediate delivery (T+2)", "why": "Standard settlement is 2 days."},
                {"q": "Forward Exchange Rate definition:", "opt": ["Rate for future delivery", "Rate for immediate delivery", "Central Bank rate"], "ans": "Rate for future delivery", "why": "Used for hedging or speculation."},
                {"q": "If EUR/USD moves from 1.10 to 1.15, the USD has:", "opt": ["Depreciated", "Appreciated", "Stayed constant"], "ans": "Depreciated", "why": "It takes MORE dollars to buy 1 Euro, so Dollar is weaker."},
                {"q": "Real Exchange Rate formula:", "opt": ["Nominal Rate x (CPI Foreign / CPI Domestic)", "Nominal x (CPI Dom / CPI For)", "Nominal - Inflation"], "ans": "Nominal Rate x (CPI Foreign / CPI Domestic)", "why": "Adjusts for relative purchasing power."},
                {"q": "Purchasing Power Parity (PPP) implies:", "opt": ["Law of One Price holds globally", "Interest rates are equal", "Inflation is zero"], "ans": "Law of One Price holds globally", "why": "Identical goods should cost the same everywhere when adjusted for FX."},
                {"q": "If a country has higher inflation than its trading partners, its currency should:", "opt": ["Depreciate", "Appreciate", "Stay stable"], "ans": "Depreciate", "why": "To maintain PPP, the currency loses value to offset inflation."},
                {"q": "A 'Direct Quote' in the US is:", "opt": ["DC/FC (e.g., 1.2 USD/EUR)", "FC/DC (e.g., 0.8 EUR/USD)", "Cross rate"], "ans": "DC/FC (e.g., 1.2 USD/EUR)", "why": "Price of one unit of foreign currency in domestic terms."},
                {"q": "The 'Bid' price in a quote is:", "opt": ["Price dealer pays to buy", "Price dealer sells at", "Midpoint"], "ans": "Price dealer pays to buy", "why": "Dealer Bids low, Asks high."},
                {"q": "The 'Ask' (Offer) price is:", "opt": ["Price dealer sells at", "Price dealer buys at", "Zero"], "ans": "Price dealer sells at", "why": "You buy from the dealer at the Ask."},
                {"q": "Spread calculation:", "opt": ["Ask - Bid", "Bid - Ask", "Ask / Bid"], "ans": "Ask - Bid", "why": "Dealer's profit margin."},
                {"q": "Cross Rate calculation (e.g., EUR/GBP) usually involves:", "opt": ["Using USD as a bridge", "Using Gold", "Guessing"], "ans": "Using USD as a bridge", "why": "Most currencies quote against USD."},
                {"q": "Forward Premium means:", "opt": ["Forward Rate > Spot Rate", "Forward Rate < Spot Rate", "Forward = Spot"], "ans": "Forward Rate > Spot Rate", "why": "Currency is stronger in the forward market."},
                {"q": "Forward Discount means:", "opt": ["Forward Rate < Spot Rate", "Forward > Spot", "Volatile"], "ans": "Forward Rate < Spot Rate", "why": "Currency is weaker in the future."},
                {"q": "Exchange Rate Regimes: 'Floating' means:", "opt": ["Market determines rate", "Government sets rate", "Fixed to Gold"], "ans": "Market determines rate", "why": "Supply and Demand drive price."},
                {"q": "Exchange Rate Regimes: 'Pegged' means:", "opt": ["Fixed to another currency", "Floating", "No currency"], "ans": "Fixed to another currency", "why": "Central Bank intervenes to maintain rate."}
            ],
            "Brutal (Above Exam)": [
                {"q": "Interest Rate Parity (IRP) prevents:", "opt": ["Riskless Arbitrage", "Inflation", "Trade Deficits"], "ans": "Riskless Arbitrage", "why": "Forward premium/discount must offset interest rate differential."},
                {"q": "If Country A Interest Rate > Country B Interest Rate, Country A currency should trade at a:", "opt": ["Forward Discount", "Forward Premium", "Spot Premium"], "ans": "Forward Discount", "why": "High rate currency depreciates in forward market to offset yield advantage."},
                {"q": "Carry Trade involves:", "opt": ["Borrowing Low Yield, Investing High Yield", "Borrowing High Yield", "Hedging"], "ans": "Borrowing Low Yield, Investing High Yield", "why": "Profits from rate spread (risks currency crash)."},
                {"q": "Marshall-Lerner Condition (Elasticities):", "opt": ["wX + wM > 1", "wX + wM < 1", "wX = wM"], "ans": "wX + wM > 1", "why": "Depreciation only improves Trade Balance if demand is elastic enough."},
                {"q": "Absorption Approach: To improve Trade Balance, a country must:", "opt": ["Reduce Domestic Expenditure relative to Income", "Increase Spending", "Lower Taxes"], "ans": "Reduce Domestic Expenditure relative to Income", "why": "X - M = Y - E."},
                {"q": "The J-Curve Effect is caused by:", "opt": ["Short-term contract rigidity", "Long-term elasticity", "Speculation"], "ans": "Short-term contract rigidity", "why": "Import prices rise immediately, volume adjusts slowly."},
                {"q": "Mundell-Fleming Model (High Capital Mobility): Expansionary Fiscal Policy leads to:", "opt": ["Appreciation", "Depreciation", "No change"], "ans": "Appreciation", "why": "Higher rates attract foreign capital inflows."},
                {"q": "Mundell-Fleming Model (High Capital Mobility): Expansionary Monetary Policy leads to:", "opt": ["Depreciation", "Appreciation", "Stable rates"], "ans": "Depreciation", "why": "Lower rates cause capital flight."},
                {"q": "Currency Board:", "opt": ["Legislative commitment to exchange domestic currency for anchor at fixed rate", "Soft peg", "Managed Float"], "ans": "Legislative commitment to exchange domestic currency for anchor at fixed rate", "why": "Requires 100% reserve backing; imports inflation."},
                {"q": "Impossible Trinity (Trilemma): You cannot have all three:", "opt": ["Fixed Rate, Free Capital Flow, Independent Monetary Policy", "Low Inf, High Growth, Low Tax", "Fixed Rate, Tariffs, Growth"], "ans": "Fixed Rate, Free Capital Flow, Independent Monetary Policy", "why": "Must choose two."},
                {"q": "Calculating Forward Points: If Bid is 1.2000 and points are -10:", "opt": ["1.1990", "1.2010", "1.2100"], "ans": "1.1990", "why": "Points are added/subtracted (divide by 10,000 for standard pairs)."},
                {"q": "Relative PPP states % change in Spot Rate equals:", "opt": ["Inflation Differential", "Interest Rate Differential", "Growth Differential"], "ans": "Inflation Differential", "why": "S1/S0 = (1+Inf_A)/(1+Inf_B)."},
                {"q": "Uncovered Interest Parity (UIP) assumes:", "opt": ["Risk Neutral investors", "Risk Averse investors", "Capital Controls"], "ans": "Risk Neutral investors", "why": "Expected spot change equals interest differential (often fails in reality)."},
                {"q": "Terms of Trade Improvement usually leads to:", "opt": ["Real Income Increase", "Real Income Decrease", "Inflation"], "ans": "Real Income Increase", "why": "Your exports buy more imports."},
                {"q": "Dornbusch Overshooting Model:", "opt": ["Exchange rates overreact to monetary shocks in SR", "Rates are stable", "PPP holds always"], "ans": "Exchange rates overreact to monetary shocks in SR", "why": "Prices are sticky, so FX moves efficiently (too much) to compensate."}
            ],
            "Flashcards (10 Cards)": [
                {"q": "Spot Rate", "ans": "Immediate Delivery (T+2)", "why": "Cash market."},
                {"q": "Forward Rate", "ans": "Future Delivery", "why": "Locked in today."},
                {"q": "Direct Quote", "ans": "Domestic / Foreign", "why": "Cost of 1 unit of foreign."},
                {"q": "Indirect Quote", "ans": "Foreign / Domestic", "why": "Buying power of 1 unit domestic."},
                {"q": "Real Exchange Rate", "ans": "Nominal adjusted for Price Levels", "why": "Purchasing Power."},
                {"q": "PPP", "ans": "Law of One Price", "why": "Long run equilibrium."},
                {"q": "Interest Rate Parity", "ans": "F/S = (1+r_d)/(1+r_f)", "why": "No Arbitrage condition."},
                {"q": "Carry Trade", "ans": "Borrow Low, Invest High", "why": "Profits from yield spread."},
                {"q": "J-Curve", "ans": "Depreciation worsens TB first", "why": "Price effect > Volume effect (SR)."},
                {"q": "Impossible Trinity", "ans": "Fixed Rate, Capital Flow, Indep Policy", "why": "Pick Two."}
            ]
        },

        "MOCK EXAM": {
            "Full Mock": [
                # --- BATCH 1 (Questions 1-50) ---
                {"q": "1. In Hicksian demand analysis, for a Giffen Good, the Substitution Effect (SE) and Income Effect (IE) interact how?", "opt": ["SE is negative, IE is positive and larger than SE", "SE is positive, IE is negative", "SE is negative, IE is negative"], "ans": "SE is negative, IE is positive and larger than SE", "why": "SE is always negative (opposite to price). For Giffen, IE is positive (inferior) and overwhelms the SE."},
                {"q": "2. If the Indifference Curve is convex to the origin, the Marginal Rate of Substitution (MRS) must be:", "opt": ["Constant", "Diminishing", "Increasing"], "ans": "Diminishing", "why": "As you consume more X, you are willing to give up less Y to get another X."},
                {"q": "3. A firm operating in Perfect Competition faces a price of $20. Its ATC is $25 and AVC is $15. In the short run, it should:", "opt": ["Shut down immediately", "Continue operating at a loss", "Raise prices"], "ans": "Continue operating at a loss", "why": "P > AVC ($20 > $15). It covers variable costs and contributes $5 to fixed costs. Shutting down loses more."},
                {"q": "4. The 'Engel Curve' for a Luxury Good is:", "opt": ["Downward sloping", "Upward sloping and concave", "Upward sloping and convex"], "ans": "Upward sloping and convex", "why": "Demand increases more than proportionately as income rises (Elasticity > 1)."},
                {"q": "5. In the Cournot Duopoly model, if one firm increases output, the reaction function of the rival firm predicts:", "opt": ["Rival will increase output", "Rival will decrease output", "Rival will hold output constant"], "ans": "Rival will decrease output", "why": "Quantities are strategic substitutes in Cournot."},
                {"q": "6. A monopolist has a linear demand curve P = 100 - 2Q. At what price is Total Revenue maximized?", "opt": ["$50", "$25", "$75"], "ans": "$50", "why": "TR is max when MR = 0. MR = 100 - 4Q. Q=25. P = 100 - 2(25) = 50. (Midpoint of linear demand)."},
                {"q": "7. The 'Liquidity Preference' theory implies that the yield curve is upward sloping because:", "opt": ["Short rates are expected to rise", "Investors demand a premium for interest rate risk in long bonds", "Inflation is rising"], "ans": "Investors demand a premium for interest rate risk in long bonds", "why": "Liquidity premium increases with maturity."},
                {"q": "8. If the Paasche Index is 110 and the Laspeyres Index is 115, the Fisher Index is closest to:", "opt": ["112.5", "112.0", "113.1"], "ans": "112.5", "why": "Geometric mean of 1.10 and 115. Sqrt(1.265) ≈ 112.47."},
                {"q": "9. Assuming high capital mobility, under a Fixed Exchange Rate regime, Expansionary Fiscal Policy leads to:", "opt": ["Crowding out of private investment", "A massive increase in Money Supply", "Ineffectiveness"], "ans": "A massive increase in Money Supply", "why": "Fiscal exp raises rates -> Capital inflow -> CB must sell currency (buy Forex) to maintain peg -> Money Supply expands."},
                {"q": "10. The 'Accelerator Principle' in investment theory states that net investment depends on:", "opt": ["The level of interest rates", "The rate of change of national income", "Corporate profits"], "ans": "The rate of change of national income", "why": "Investment is derived from the *change* in demand (GDP growth)."},
                {"q": "11. If the Nominal GDP target is growing at 5%, and Velocity is trending down by 1% per year, Money Supply must grow at:", "opt": ["4%", "5%", "6%"], "ans": "6%", "why": "%M + %V = %NomGDP. M - 1% = 5%. M = 6%."},
                {"q": "12. A 'Veblen Good' demand curve slopes upward because of:", "opt": ["Income Effect", "Snob/Status Effect", "Giffen Paradox"], "ans": "Snob/Status Effect", "why": "Utility is derived *from* the high price (conspicuous consumption)."},
                {"q": "13. In a 'Kinked Demand' Oligopoly, if Marginal Cost (MC) increases slightly within the gap, Price (P) and Quantity (Q) will:", "opt": ["P increases, Q decreases", "Remain unchanged", "P stays same, Q decreases"], "ans": "Remain unchanged", "why": "The vertical gap in MR means MR still equals MC at the same Q."},
                {"q": "14. Calculating Cross-Price Elasticity: Price of Y goes from $10 to $12. Demand for X goes from 100 to 110. Exy is:", "opt": ["+0.5 (Substitutes)", "+0.5 (Complements)", "+2.0 (Substitutes)"], "ans": "+0.5 (Substitutes)", "why": "%dQ = 10%. %dP = 20%. 10/20 = 0.5. Positive = Substitute."},
                {"q": "15. The 'Terms of Trade' improve if:", "opt": ["Export prices rise relative to import prices", "Currency depreciates", "Volume of exports rises"], "ans": "Export prices rise relative to import prices", "why": "You get more imports for every unit of export."},
                {"q": "16. Regarding the Stackelberg Model, the 'First Mover Advantage' results in:", "opt": ["Leader producing less than Cournot", "Leader producing more, Follower producing less", "Both producing monopoly output"], "ans": "Leader producing more, Follower producing less", "why": "Leader commits to high output, forcing follower to retreat."},
                {"q": "17. A decrease in the Gini Coefficient indicates:", "opt": ["Higher Inequality", "Lower Inequality", "Higher GDP"], "ans": "Lower Inequality", "why": "0 is perfect equality, 1 is perfect inequality."},
                {"q": "18. The 'Crowding Out' effect is strongest when the demand for money is:", "opt": ["Perfectly Elastic (Liquidity Trap)", "Perfectly Inelastic", "Unit Elastic"], "ans": "Perfectly Inelastic", "why": "If money demand is insensitive to rates, fiscal borrowing spikes rates drastically, crushing investment."},
                {"q": "19. If the USD/CAD spot is 1.30 and the 1-year forward is 1.28, the CAD is trading at a:", "opt": ["Forward Discount", "Forward Premium", "Par"], "ans": "Forward Premium", "why": "1.30 CAD/USD -> 1.28 CAD/USD. CAD is getting stronger (Appreciating). Premium."},
                {"q": "20. According to the Coase Theorem, negative externalities can be solved without government if:", "opt": ["Transaction costs are low and property rights are defined", "Taxes are high", "The market is perfect"], "ans": "Transaction costs are low and property rights are defined", "why": "Parties will bargain to the efficient outcome."},
                {"q": "21. A tariff that maximizes welfare for a large country is called:", "opt": ["Prohibitive Tariff", "Optimum Tariff", "Retaliatory Tariff"], "ans": "Optimum Tariff", "why": "Balances terms-of-trade gain against efficiency loss."},
                {"q": "22. If the Reserve Ratio is 10% and Banks hold 5% Excess Reserves, the actual Money Multiplier is:", "opt": ["10", "20", "6.67"], "ans": "6.67", "why": "Multiplier = 1 / (RR + Excess). 1 / 0.15 = 6.66..."},
                {"q": "23. In the Long Run, a Monopolistic Competitor produces at a point where:", "opt": ["P = Min ATC", "P > Min ATC", "P = MC"], "ans": "P > Min ATC", "why": "Excess Capacity Theorem. Tangency is on the downward slope of ATC."},
                {"q": "24. 'Menu Costs' are a primary explanation for:", "opt": ["Wage Rigidity", "Price Stickiness", "Interest Rate volatility"], "ans": "Price Stickiness", "why": "Cost of changing price lists prevents firms from adjusting P instantly."},
                {"q": "25. Which unemployment type is NOT part of the Natural Rate of Unemployment (NAIRU)?", "opt": ["Frictional", "Structural", "Cyclical"], "ans": "Cyclical", "why": "Natural Rate = Frictional + Structural only."},
                {"q": "26. If a country has a persistent Current Account Deficit, it must have a:", "opt": ["Capital Account Deficit", "Capital Account Surplus", "Budget Surplus"], "ans": "Capital Account Surplus", "why": "It must borrow from abroad (Import capital) to finance the consumption."},
                {"q": "27. The 'Triangle of Welfare Loss' in a monopoly represents:", "opt": ["Transfer from Consumer to Producer", "Deadweight Loss", "Fixed Costs"], "ans": "Deadweight Loss", "why": "Surplus that vanishes because mutually beneficial trades (P > MC) don't happen."},
                {"q": "28. An increase in the Labor Force Participation Rate, ceteris paribus, initially causes the Unemployment Rate to:", "opt": ["Decrease", "Increase", "Stay same"], "ans": "Increase", "why": "New entrants join as 'Unemployed' before finding jobs."},
                {"q": "29. If the Central Bank buys securities, the immediate impact on the Interbank Lending Rate is:", "opt": ["Increase", "Decrease", "Neutral"], "ans": "Decrease", "why": "Adds reserves -> Supply of loanable funds up -> Price (Rate) down."},
                {"q": "30. 'Dutch Disease' refers to currency appreciation causing:", "opt": ["Deindustrialization", "Hyperinflation", "Banking Crisis"], "ans": "Deindustrialization", "why": "Resource exports boost currency, making manufacturing exports uncompetitive."},
                {"q": "31. A 'Quota' is worse than a 'Tariff' for the importing country if:", "opt": ["Quota rents are captured by foreigners", "Demand is inelastic", "Supply is elastic"], "ans": "Quota rents are captured by foreigners", "why": "With a tariff, govt gets revenue. With a quota, foreign exporters often keep the extra profit."},
                {"q": "32. The 'Substitution Bias' in CPI implies that CPI:", "opt": ["Overstates Inflation", "Understates Inflation", "Is accurate"], "ans": "Overstates Inflation", "why": "Consumers switch to cheaper goods, but fixed basket assumes they don't."},
                {"q": "33. In the IS-LM model, a decrease in Money Supply shifts:", "opt": ["IS Left", "LM Left (Up)", "LM Right (Down)"], "ans": "LM Left (Up)", "why": "Less money -> Higher interest rate required to clear money market."},
                {"q": "34. Perfect Price Discrimination results in a Marginal Revenue curve that:", "opt": ["Is below the Demand Curve", "Coincides with the Demand Curve", "Is horizontal"], "ans": "Coincides with the Demand Curve", "why": "The firm captures the exact price for every unit, so P = MR."},
                {"q": "35. If Nominal GDP = 12 Trillion and Money Supply = 2 Trillion, Velocity is:", "opt": ["6", "24", "0.16"], "ans": "6", "why": "V = PY / M = 12 / 2 = 6."},
                {"q": "36. The slope of the Budget Constraint is determined by:", "opt": ["MRS", "Relative Prices (-Px/Py)", "Income"], "ans": "Relative Prices (-Px/Py)", "why": "Market trade-off rate."},
                {"q": "37. 'Moral Hazard' in banking refers to:", "opt": ["Taking excessive risk because of bailouts", "Adverse Selection", "Theft"], "ans": "Taking excessive risk because of bailouts", "why": "Insulation from consequences encourages risk."},
                {"q": "38. If the Real Interest Rate is negative:", "opt": ["Inflation > Nominal Rate", "Nominal Rate > Inflation", "Deflation is occurring"], "ans": "Inflation > Nominal Rate", "why": "Fisher equation: Real = Nom - Inf."},
                {"q": "39. The 'Herfindahl Index' for a duopoly with 50-50 market share is:", "opt": ["2,500", "5,000", "50"], "ans": "5,000", "why": "50^2 + 50^2 = 2500 + 2500 = 5000."},
                {"q": "40. A 'Giffen Good' must have a demand curve that is:", "opt": ["Elastic", "Inelastic", "Positively Sloped"], "ans": "Positively Sloped", "why": "Price up -> Quantity up."},
                {"q": "41. In Game Theory, a 'Dominant Strategy' is:", "opt": ["Best regardless of what the opponent does", "Best given what the opponent does", "Always cheating"], "ans": "Best regardless of what the opponent does", "why": "No strategic dependence."},
                {"q": "42. The 'Paradox of Thrift' suggests that if everyone saves more:", "opt": ["Investment rises", "Aggregate Demand falls, lowering total savings", "Growth accelerates"], "ans": "Aggregate Demand falls, lowering total savings", "why": "Spending stops -> Income falls -> Savings actually drop."},
                {"q": "43. If a currency is overvalued based on PPP, in the long run it should:", "opt": ["Depreciate", "Appreciate", "Stay constant"], "ans": "Depreciate", "why": "Goods are too expensive; demand for currency will fall."},
                {"q": "44. 'Sterilized Intervention' by a Central Bank affects:", "opt": ["Money Supply", "Exchange Rates but not Money Supply", "Interest Rates"], "ans": "Exchange Rates but not Money Supply", "why": "Offsetting bond operation neutralizes the liquidity effect."},
                {"q": "45. The 'J-Curve' trough represents the period where:", "opt": ["Volume effect dominates", "Price effect dominates", "Elasticity is infinite"], "ans": "Price effect dominates", "why": "Import prices are higher, but quantity hasn't dropped yet -> Trade Deficit worsens."},
                {"q": "46. If the elasticity of demand is -2.0, a 10% price cut raises revenue by approx:", "opt": ["10%", "8%", "20%"], "ans": "8%", "why": "Q up 20%. P down 10%. Revenue change = (1-10%)*(1+20%) = 0.9*1.2 = 1.08 -> +8%."},
                {"q": "47. In the Solow Model, steady state occurs when:", "opt": ["Investment = Depreciation", "Savings = Consumption", "MPK = 0"], "ans": "Investment = Depreciation", "why": "Capital stock stops growing."},
                {"q": "48. 'Fiscal Drag' occurs when:", "opt": ["Inflation pushes taxpayers into higher brackets", "Govt spending is too low", "Deficits are high"], "ans": "Inflation pushes taxpayers into higher brackets", "why": "Real tax burden rises without rate changes (Bracket Creep)."},
                {"q": "49. An inverted yield curve usually signals:", "opt": ["Future Recession", "Future Inflation", "Fiscal Surplus"], "ans": "Future Recession", "why": "Short rates high (tight money) + Long rates low (low growth expectation)."},
                {"q": "50. If Cross Elasticity = 0, the goods are:", "opt": ["Unrelated", "Substitutes", "Complements"], "ans": "Unrelated", "why": "Price of one implies nothing about the other."},
                
                # --- BATCH 2 (Questions 51-100) ---
                {"q": "51. If the Bid/Ask for USD/GBP is 1.2500 / 1.2510, what is the cost to BUY GBP?", "opt": ["1.2500 USD", "1.2510 USD", "1.2505 USD"], "ans": "1.2510 USD", "why": "You buy at the Dealer's Ask price."},
                {"q": "52. Calculating the 'Cross-Rate Bid': If A/B Bid is 2.0 and B/C Bid is 3.0, what is A/C Bid?", "opt": ["6.0", "5.0", "1.5"], "ans": "6.0", "why": "Bid * Bid = Bid. (A/B) * (B/C) = A/C. 2.0 * 3.0 = 6.0."},
                {"q": "53. In a 'Monopsony' labor market, the Marginal Resource Cost (MRC) of labor is:", "opt": ["Equal to the Wage Rate", "Higher than the Wage Rate", "Lower than the Wage Rate"], "ans": "Higher than the Wage Rate", "why": "To hire one more worker, you must raise wages for ALL workers."},
                {"q": "54. If Nominal GDP increases by 4% and Population increases by 4%, Real GDP per Capita:", "opt": ["Stays same", "Decreases", "Cannot be determined without Inflation data"], "ans": "Cannot be determined without Inflation data", "why": "Nominal GDP must be deflated to Real GDP first. If Inflation > 0, Real GDP per cap fell."},
                {"q": "55. A 'Pigouvian Tax' is designed to:", "opt": ["Generate maximum revenue", "Correct a negative externality", "Redistribute wealth"], "ans": "Correct a negative externality", "why": "Tax = Marginal Social Cost of pollution."},
                {"q": "56. If Demand is Perfectly Inelastic (Vertical), a tax imposed on producers is paid by:", "opt": ["100% Consumers", "100% Producers", "Split 50/50"], "ans": "100% Consumers", "why": "Producers pass the full tax price increase because consumers will not reduce quantity."},
                {"q": "57. The 'Money Multiplier' with Currency Drain (C/D ratio) is:", "opt": ["(1 + C/D) / (RR + C/D)", "1 / RR", "1 / (1-MPC)"], "ans": "(1 + C/D) / (RR + C/D)", "why": "Cash held by public reduces bank reserves available for lending."},
                {"q": "58. In the Short Run, if Average Variable Cost (AVC) is rising, Marginal Cost (MC) must be:", "opt": ["Below AVC", "Above AVC", "Equal to AVC"], "ans": "Above AVC", "why": "MC pulls the average up only when it is above the average."},
                {"q": "59. Which school of thought advocates for a 'Constant Money Growth Rule'?", "opt": ["Keynesian", "Monetarist", "Austrian"], "ans": "Monetarist", "why": "Friedman: Discretionary policy causes instability; stick to k-percent rule."},
                {"q": "60. If the 'Terms of Trade' improve, but the 'Trade Balance' worsens, this is likely due to:", "opt": ["Inelastic demand for imports", "Elastic demand for exports", "Perfect competition"], "ans": "Inelastic demand for imports", "why": "Imports got cheaper, but we bought SO MANY more that total spend went up."},
                {"q": "61. 'Cost-Push Inflation' is initially characterized by:", "opt": ["Falling GDP and Rising Prices", "Rising GDP and Rising Prices", "Rising GDP and Falling Prices"], "ans": "Falling GDP and Rising Prices", "why": "SRAS shifts left (Stagflation)."},
                {"q": "62. In a 'Liquidity Trap', the Fiscal Multiplier is:", "opt": ["Zero", "Small", "Large"], "ans": "Large", "why": "No crowding out occurs because interest rates don't rise (LM curve is flat)."},
                {"q": "63. The 'Substitution Effect' for a wage increase leads a worker to:", "opt": ["Work more", "Work less", "Retire"], "ans": "Work more", "why": "Leisure is more expensive (opportunity cost), so you substitute leisure for labor."},
                {"q": "64. The 'Income Effect' for a wage increase (at high incomes) leads a worker to:", "opt": ["Work more", "Work less", "Save less"], "ans": "Work less", "why": "You feel richer and 'buy' more leisure."},
                {"q": "65. If a country imposes a Capital Control tax on outflows, domestic interest rates should:", "opt": ["Rise", "Fall", "Stay same"], "ans": "Fall", "why": "Capital is trapped inside the country, increasing the supply of loanable funds."},
                {"q": "66. A 'Single Price Monopolist' creates Deadweight Loss because:", "opt": ["It produces where MR < P", "It produces where MR = MC", "It produces where P = MC"], "ans": "It produces where MR < P", "why": "Willingness to pay (P) > Cost (MC), but units are not produced."},
                {"q": "67. If the Central Bank wants to sterilize the inflationary effect of buying Foreign Currency, it should:", "opt": ["Buy Domestic Bonds", "Sell Domestic Bonds", "Lower Rates"], "ans": "Sell Domestic Bonds", "why": "Buying FX injects cash. Selling Bonds drains cash to neutralize it."},
                {"q": "68. The 'Laffer Curve' suggests that at very high tax rates, cutting taxes will:", "opt": ["Decrease Revenue", "Increase Revenue", "Have no effect"], "ans": "Increase Revenue", "why": "Disincentive effects of high taxes are removed, boosting the tax base."},
                {"q": "69. 'Rational Expectations' theory implies that anticipated policy changes have:", "opt": ["Short-run effects only", "Long-run effects only", "No effect on real output"], "ans": "No effect on real output", "why": "Agents adjust prices/wages immediately, preventing any real stimulus."},
                {"q": "70. If the Output Gap is -2% (Recessionary) and the Central Bank targets 2% Inflation, but current inflation is 1%, the Taylor Rule suggests:", "opt": ["Rate Hike", "Aggressive Rate Cut", "Rate Pause"], "ans": "Aggressive Rate Cut", "why": "Both gaps (Output and Inflation) dictate easing."},
                {"q": "71. 'Concentration Ratios' (CR4) fail to account for:", "opt": ["Market Power", "Mergers between top firms", "Mergers between small firms"], "ans": "Mergers between small firms", "why": "CR4 only looks at the top 4. HHI captures the full distribution."},
                {"q": "72. A 'Forward Rate Agreement' (FRA) is essentially a bet on:", "opt": ["Future Exchange Rates", "Future Interest Rates (LIBOR/SOFR)", "Stock Prices"], "ans": "Future Interest Rates (LIBOR/SOFR)", "why": "Used to hedge interest rate risk."},
                {"q": "73. In the Mundell-Fleming model with flexible exchange rates, Fiscal Policy is ineffective because:", "opt": ["Crowding out via Currency Appreciation", "Crowding out via Interest Rates", "Ricardian Equivalence"], "ans": "Crowding out via Currency Appreciation", "why": "Fiscal Exp -> Rates Up -> Currency Up -> Net Exports Down (cancels stimulus)."},
                {"q": "74. If the Elasticity of Supply is > Elasticity of Demand, the tax burden falls mostly on:", "opt": ["Producers", "Consumers", "Government"], "ans": "Consumers", "why": "He who is less elastic (cannot run away) pays the tax."},
                {"q": "75. 'Minimum Efficient Scale' (MES) is the output level where:", "opt": ["LRATC is minimized", "MC is minimized", "Profit is maximized"], "ans": "LRATC is minimized", "why": "Smallest size to compete effectively."},
                {"q": "76. 'Diminishing Marginal Returns' applies to:", "opt": ["Short Run only", "Long Run only", "Both"], "ans": "Short Run only", "why": "Requires at least one fixed input (Capital). In LR, all inputs are variable (Scale)."},
                {"q": "77. If the Price of X rises and the Demand for Y shifts Left, X and Y are:", "opt": ["Substitutes", "Complements", "Inferior"], "ans": "Complements", "why": "X is more expensive, so you use less X... and therefore need less Y (e.g., Gin and Tonic)."},
                {"q": "78. 'Core Inflation' excludes:", "opt": ["Services", "Food and Energy", "Housing"], "ans": "Food and Energy", "why": "They are too volatile to show the long-term trend."},
                {"q": "79. A 'Negative Supply Shock' (e.g., Oil Embargo) shifts:", "opt": ["SRAS Left", "SRAS Right", "AD Left"], "ans": "SRAS Left", "why": "Input costs rise, reducing supply at every price level."},
                {"q": "80. In Perfect Competition, the Demand Curve facing the *Firm* is:", "opt": ["Perfectly Inelastic", "Perfectly Elastic", "Downward Sloping"], "ans": "Perfectly Elastic", "why": "The firm is a price taker (Horizontal D). The *Market* D is downward sloping."},
                {"q": "81. 'Rent Seeking' refers to:", "opt": ["Landlords raising rents", "Expending resources to gain government privilege/protection", "Looking for an apartment"], "ans": "Expending resources to gain government privilege/protection", "why": "Lobbying for tariffs/subsidies. It is a social waste."},
                {"q": "82. If Real GDP = Potential GDP, Unemployment equals:", "opt": ["Zero", "The Natural Rate", "Structural Rate"], "ans": "The Natural Rate", "why": "Cyclical unemployment is zero."},
                {"q": "83. The 'Fisher Index' is known as 'Ideal' because it corrects for:", "opt": ["Substitution Bias", "Quality Bias", "New Product Bias"], "ans": "Substitution Bias", "why": "It handles the geometric mean of Paasche (under) and Laspeyres (over)."},
                {"q": "84. If the Nominal Exchange Rate is constant, but Domestic Inflation > Foreign Inflation, the Real Exchange Rate:", "opt": ["Appreciates", "Depreciates", "Stays constant"], "ans": "Appreciates", "why": "Our goods are becoming relatively more expensive. Competitiveness falls."},
                {"q": "85. 'Frictional Unemployment' is beneficial because:", "opt": ["It keeps wages low", "It represents better job matching", "It reduces inflation"], "ans": "It represents better job matching", "why": "Time spent finding the *right* job improves productivity."},
                {"q": "86. An increase in the Reserve Requirement causes the Money Multiplier to:", "opt": ["Increase", "Decrease", "Stay same"], "ans": "Decrease", "why": "Banks can lend out a smaller fraction of deposits."},
                {"q": "87. 'Indifference Curves' cannot cross because it violates:", "opt": ["Transitivity", "Completeness", "Non-satiation"], "ans": "Transitivity", "why": "If A=B and A=C, then B must equal C. Crossing curves implies B > C and C > B simultaneously."},
                {"q": "88. The 'Current Account' deficit is fundamentally an imbalance between:", "opt": ["Imports and Exports", "Savings and Investment", "Tax and Spend"], "ans": "Savings and Investment", "why": "(S - I) + (T - G) = CA. If Investment > Savings, you must import capital (CA deficit)."},
                {"q": "89. 'Predatory Pricing' is:", "opt": ["Pricing below MC to drive out rivals", "Pricing high to gauge willingness", "Price discrimination"], "ans": "Pricing below MC to drive out rivals", "why": "Illegal antitrust violation (if proven)."},
                {"q": "90. If the 'Velocity of Money' is unstable, which policy is difficult to implement?", "opt": ["Monetary Targeting (Money Supply)", "Inflation Targeting", "Fiscal Policy"], "ans": "Monetary Targeting (Money Supply)", "why": "If V fluctuates, controlling M doesn't reliably control PY (Nominal GDP)."},
                {"q": "91. A 'Credit Default Swap' (CDS) price rising indicates:", "opt": ["Improving credit quality", "Deteriorating credit quality", "Lower interest rates"], "ans": "Deteriorating credit quality", "why": "Cost of insurance against default is going up."},
                {"q": "92. 'Collusive Oligopoly' behaves most like:", "opt": ["Monopoly", "Perfect Competition", "Monopolistic Competition"], "ans": "Monopoly", "why": "They act as a single firm to maximize joint profits."},
                {"q": "93. 'Transfer Payments' (Social Security) are excluded from GDP because:", "opt": ["They are not production", "They are too small", "They are taxed"], "ans": "They are not production", "why": "It is just moving money from A to B, not creating new goods/services."},
                {"q": "94. If the Marginal Propensity to Consume (MPC) is 0.8, the Tax Multiplier is:", "opt": ["-4", "-5", "-1"], "ans": "-4", "why": "-MPC / (1 - MPC) = -0.8 / 0.2 = -4."},
                {"q": "95. 'Implicit Costs' are:", "opt": ["Out of pocket expenses", "Opportunity costs of owned resources", "Accounting costs"], "ans": "Opportunity costs of owned resources", "why": "e.g., the salary the owner *could* have earned working elsewhere."},
                {"q": "96. Economic Profit equals:", "opt": ["Accounting Profit - Implicit Costs", "Revenue - Explicit Costs", "Accounting Profit + Implicit Costs"], "ans": "Accounting Profit - Implicit Costs", "why": "Total Revenue - (Explicit + Implicit Costs)."},
                {"q": "97. 'Monetary Neutrality' suggests that doubling the money supply will eventually:", "opt": ["Double Real GDP", "Double Price Levels", "Halve Interest Rates"], "ans": "Double Price Levels", "why": "Real variables are unaffected in the long run."},
                {"q": "98. 'Okun's Law' describes the relationship between:", "opt": ["Inflation and Unemployment", "GDP Gap and Unemployment Gap", "Tax rates and Revenue"], "ans": "GDP Gap and Unemployment Gap", "why": "High unemployment correlates with output below potential."},
                {"q": "99. 'Gresham's Law' states:", "opt": ["Bad money drives out good", "Good money drives out bad", "Money is neutral"], "ans": "Bad money drives out good", "why": "People hoard the valuable currency (Good) and spend the debased one (Bad)."},
                {"q": "100. If the Central Bank pegs the currency ABOVE the equilibrium value (Overvalued):", "opt": ["It gains reserves", "It loses reserves", "It has no effect"], "ans": "It loses reserves", "why": "It must buy its own currency (sell foreign reserves) to prop up the price."}
                               ,
                # --- BATCH 3 (Questions 101-150) ---
                {"q": "101. A 'Corner Solution' in consumer choice theory typically occurs when:", "opt": ["Goods are Perfect Substitutes", "Goods are Perfect Complements", "MRS is diminishing"], "ans": "Goods are Perfect Substitutes", "why": "Consumer buys ONLY the cheaper good (all X or all Y)."},
                {"q": "102. The 'Bandwagon Effect' implies that the market demand curve is:", "opt": ["More elastic than individual curves sum", "Less elastic", "Vertical"], "ans": "More elastic than individual curves sum", "why": "People buy because others are buying, amplifying price drops."},
                {"q": "103. In the 'Stage II' of Production (Law of Variable Proportions):", "opt": ["Average Product is falling, Marginal Product is positive", "Marginal Product is negative", "Average Product is rising"], "ans": "Average Product is falling, Marginal Product is positive", "why": "The rational zone of production."},
                {"q": "104. 'Economies of Scope' differ from 'Economies of Scale' because they relate to:", "opt": ["Variety of products", "Volume of one product", "Fixed costs"], "ans": "Variety of products", "why": "Cheaper to produce Product A and B together than separately."},
                {"q": "105. A 'Contestable Market' theory suggests that monopolies behave competitively if:", "opt": ["Barriers to entry/exit are low", "There are many firms", "Regulation is strict"], "ans": "Barriers to entry/exit are low", "why": "Threat of 'hit-and-run' entry disciplines the incumbent."},
                {"q": "106. In 'First-Degree Price Discrimination', Consumer Surplus is:", "opt": ["Zero", "Maximized", "Shared with producer"], "ans": "Zero", "why": "Monopolist charges the maximum willingness to pay for every single unit."},
                {"q": "107. The 'Sweezy Model' of Oligopoly assumes rivals will:", "opt": ["Match price cuts but ignore price hikes", "Match price hikes", "Ignore all price changes"], "ans": "Match price cuts but ignore price hikes", "why": "Creates the Kinked Demand Curve."},
                {"q": "108. In a 'Dominant Firm' model, the fringe firms act as:", "opt": ["Price Takers", "Price Leaders", "Cartel members"], "ans": "Price Takers", "why": "They accept the price set by the dominant firm and supply what they can."},
                {"q": "109. 'Imputed Rent' is included in GDP to account for:", "opt": ["Value of owner-occupied housing", "Rent controls", "Commercial leases"], "ans": "Value of owner-occupied housing", "why": "Treats homeowners as if they pay rent to themselves (keeps GDP consistent vs renting)."},
                {"q": "110. 'Green GDP' adjusts standard GDP for:", "opt": ["Environmental degradation and resource depletion", "Inflation", "Renewable energy output"], "ans": "Environmental degradation and resource depletion", "why": "Subtracts the cost of pollution/damage."},
                {"q": "111. A 'Cost of Living Adjustment' (COLA) usually links wages to:", "opt": ["CPI", "GDP Deflator", "PPI"], "ans": "CPI", "why": "Protects purchasing power of consumers."},
                {"q": "112. The 'U-6' Unemployment Rate is higher than the standard rate because it includes:", "opt": ["Discouraged workers and Underemployed", "Long-term unemployed only", "Foreign workers"], "ans": "Discouraged workers and Underemployed", "why": "Broadest measure of labor slack."},
                {"q": "113. Friedman's 'Permanent Income Hypothesis' suggests consumption depends on:", "opt": ["Long-run expected income", "Current disposable income", "Interest rates"], "ans": "Long-run expected income", "why": "Temporary tax cuts have little effect on spending if viewed as transient."},
                {"q": "114. 'Tobin's Q' predicts investment will rise if:", "opt": ["Market Value of Assets > Replacement Cost", "Market Value < Replacement Cost", "Interest rates are high"], "ans": "Market Value of Assets > Replacement Cost", "why": "Firms buy capital (invest) because the stock market values it highly (Q > 1)."},
                {"q": "115. The 'Structural Budget Deficit' is the deficit that would exist if:", "opt": ["The economy were at Full Employment", "There were no taxes", "Inflation were zero"], "ans": "The economy were at Full Employment", "why": "Removes the cyclical component (automatic stabilizers)."},
                {"q": "116. Money functions as a 'Unit of Account' when:", "opt": ["Prices are quoted in it", "It is saved", "It is used for trade"], "ans": "Prices are quoted in it", "why": "It measures value (like a ruler)."},
                {"q": "117. 'Operational Independence' for a Central Bank means:", "opt": ["It can choose *how* to achieve targets", "It can set its own inflation target", "It is not audited"], "ans": "It can choose *how* to achieve targets", "why": "Govt sets the goal (e.g., 2%), Bank chooses the tools (Rates/QE)."},
                {"q": "118. The 'Neutral Rate of Interest' (r*) is the rate where:", "opt": ["Economy grows at trend with stable inflation", "Inflation is zero", "GDP growth is maxed"], "ans": "Economy grows at trend with stable inflation", "why": "Neither expansionary nor contractionary."},
                {"q": "119. 'Intra-Industry Trade' (e.g., Germany exports cars to France, imports cars from France) is driven by:", "opt": ["Product Differentiation & Economies of Scale", "Comparative Advantage", "Resource endowments"], "ans": "Product Differentiation & Economies of Scale", "why": "Consumers want variety (BMWs AND Peugeots)."},
                {"q": "120. In a 'Voluntary Export Restraint' (VER), the 'Quota Rents' go to:", "opt": ["The Foreign Exporter", "The Domestic Govt", "The Domestic Consumer"], "ans": "The Foreign Exporter", "why": "Foreigners raise prices to limit quantity, keeping the extra profit."},
                {"q": "121. 'Capital Flight' typically causes:", "opt": ["Currency Depreciation and Higher Rates", "Appreciation and Lower Rates", "Stable markets"], "ans": "Currency Depreciation and Higher Rates", "why": "Selling currency to leave crashes the rate; liquidity dries up spiking interest."},
                {"q": "122. 'Triangular Arbitrage' is possible if:", "opt": ["Implied Cross Rate != Quoted Cross Rate", "Forward Rate > Spot", "Rates are equal"], "ans": "Implied Cross Rate != Quoted Cross Rate", "why": "Profit from mispricing between three currency pairs."},
                {"q": "123. 'Real Interest Rate Parity' suggests that real rates across countries will:", "opt": ["Converge", "Diverge", "Follow inflation"], "ans": "Converge", "why": "Capital flows to the highest real yield until it is equalized."},
                {"q": "124. The 'Portfolio Balance Approach' to FX rates focuses on:", "opt": ["Supply/Demand of Financial Assets", "Trade flows", "PPP"], "ans": "Supply/Demand of Financial Assets", "why": "Investors rebalancing bond/stock portfolios drives currency flows."},
                {"q": "125. Which factor is critical for 'Endogenous Growth Theory'?", "opt": ["R&D and Human Capital Spillover", "Capital Accumulation", "Population Growth"], "ans": "R&D and Human Capital Spillover", "why": "Knowledge doesn't suffer diminishing returns."},
                {"q": "126. Strong 'Property Rights' are essential for growth because they:", "opt": ["Encourage Investment and Innovation", "Increase Taxes", "Reduce Inequality"], "ans": "Encourage Investment and Innovation", "why": "Nobody builds a factory if it can be seized arbitrarily."},
                {"q": "127. The 'Averch-Johnson Effect' (Gold Plating) occurs in regulation when:", "opt": ["Rate of Return is regulated", "Price Cap is used", "Entry is free"], "ans": "Rate of Return is regulated", "why": "Utilities over-invest in capital base to increase the absolute dollar profit allowed."},
                {"q": "128. 'Loss Aversion' (Prospect Theory) implies losses hurt:", "opt": ["More than equivalent gains feel good", "Less than gains", "The same as gains"], "ans": "More than equivalent gains feel good", "why": "Roughly 2x magnitude impact."},
                {"q": "129. The 'Framing Effect' means decisions are influenced by:", "opt": ["How information is presented", "Rational calculation", "Utility max"], "ans": "How information is presented", "why": "80% fat-free sounds better than 20% fat."},
                {"q": "130. 'Arc Elasticity' is used when:", "opt": ["Calculating elasticity over a range of prices", "At a specific point", "For linear demand"], "ans": "Calculating elasticity over a range of prices", "why": "Uses the midpoint formula."},
                {"q": "131. A 'Tax Wedge' creates a gap between:", "opt": ["Cost to employer and Wage received by worker", "Price and Cost", "Import and Export"], "ans": "Cost to employer and Wage received by worker", "why": "Labor tax + Income tax reduces employment."},
                {"q": "132. The 'Backward Bending Supply Curve' of Labor occurs when:", "opt": ["Income Effect > Substitution Effect", "Subst > Income", "Wages are low"], "ans": "Income Effect > Substitution Effect", "why": "At very high wages, you buy more leisure."},
                {"q": "133. The 'Rental Price of Capital' must equal:", "opt": ["Marginal Product of Capital (MPK)", "Interest Rate", "Depreciation"], "ans": "Marginal Product of Capital (MPK)", "why": "Equilibrium condition for firm input."},
                {"q": "134. 'Loanable Funds Theory' determines interest rates via:", "opt": ["Supply of Savings vs Demand for Investment", "Supply of Money vs Demand for Money", "Central Bank"], "ans": "Supply of Savings vs Demand for Investment", "why": "Real sector determination of rates."},
                {"q": "135. The 'Great Depression' was worsened by (Monetarist view):", "opt": ["Contraction of Money Supply by Fed", "Stock Crash", "Fiscal austerity"], "ans": "Contraction of Money Supply by Fed", "why": "Allowed banking panic to destroy liquidity."},
                {"q": "136. 'Shadow Banking' played a role in 2008 because:", "opt": ["It was unregulated and highly leveraged", "It was too small", "It held only cash"], "ans": "It was unregulated and highly leveraged", "why": "Bank-like maturity transformation without deposit insurance."},
                {"q": "137. 'Helicopter Money' differs from QE because:", "opt": ["It is a permanent transfer to citizens", "It buys assets", "It is reversible"], "ans": "It is a permanent transfer to citizens", "why": "Fiscal stimulus financed by money printing (never paid back)."},
                {"q": "138. A 'Diffusion Index' < 50% usually signals:", "opt": ["Contraction/Slowdown", "Expansion", "Peak"], "ans": "Contraction/Slowdown", "why": "More components are falling than rising."},
                {"q": "139. 'LIFO' inventory accounting during inflation results in:", "opt": ["Lower reported profits, Lower taxes", "Higher profits, Higher taxes", "Higher Inventory value"], "ans": "Lower reported profits, Lower taxes", "why": "High cost current items are 'sold' first, increasing COGS."},
                {"q": "140. 'Type I Error' in policy is:", "opt": ["False Positive (Taking action when none needed)", "False Negative", "Accuracy"], "ans": "False Positive (Taking action when none needed)", "why": "e.g., Raising rates to fight inflation that wasn't there."},
                {"q": "141. 'Efficient Market Hypothesis' (Weak Form) says you cannot profit from:", "opt": ["Past price/volume data (Technical Analysis)", "Public info", "Insider info"], "ans": "Past price/volume data (Technical Analysis)", "why": "Past trends are already priced in."},
                {"q": "142. A 'Random Walk' implies future stock prices are:", "opt": ["Unpredictable", "Mean reverting", "Trending"], "ans": "Unpredictable", "why": "New information arrives randomly."},
                {"q": "143. 'Dollarization' (giving up national currency) eliminates:", "opt": ["Exchange Rate Risk and Monetary Autonomy", "Fiscal Policy", "Trade"], "ans": "Exchange Rate Risk and Monetary Autonomy", "why": "You import the US Fed's policy completely."},
                {"q": "144. 'Seigniorage' is profit made by:", "opt": ["Printing money", "Minting coins only", "Taxing imports"], "ans": "Printing money", "why": "Difference between face value of money and cost to produce it."},
                {"q": "145. The WTO's 'Most Favored Nation' (MFN) clause requires:", "opt": ["Treating all members equally", "Favoring developing nations", "Zero tariffs"], "ans": "Treating all members equally", "why": "You cannot give a special deal to one partner (unless FTA)."},
                {"q": "146. 'Tax Incidence' depends on:", "opt": ["Relative Elasticities of Supply and Demand", "Who writes the check", "Govt law"], "ans": "Relative Elasticities of Supply and Demand", "why": "Statutory incidence is irrelevant."},
                {"q": "147. A 'Price Floor' (Minimum Wage) causes a surplus if set:", "opt": ["Above Equilibrium", "Below Equilibrium", "At Equilibrium"], "ans": "Above Equilibrium", "why": "Supply of labor > Demand for labor = Unemployment."},
                {"q": "148. The 'Deadweight Loss' of a tax increases with:", "opt": ["The square of the tax rate", "Linearly with tax rate", "It decreases"], "ans": "The square of the tax rate", "why": "Doubling the tax quadruples the distortion."},
                {"q": "149. In 'Oligopoly', the Demand Curve is often assumed to be:", "opt": ["Kinked", "Horizontal", "Vertical"], "ans": "Kinked", "why": "Due to asymmetric reaction to price changes."},
                {"q": "150. 'Utility' is best defined as:", "opt": ["Satisfaction/Benefit derived from consumption", "Usefulness", "Price"], "ans": "Satisfaction/Benefit derived from consumption", "why": "Ordinal measure of preference."}
 
            ]
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
# ==============================================================================
# ==============================================================================
# 5. THE INTERFACE (FINAL UI UPGRADE)
# ==============================================================================
st.title("CFA Master System")

# MODULE SELECTOR
if not library["Economics"]:
    st.error("⚠️ Database Empty. Please Paste Data.")
    st.stop()

los_keys = list(library["Economics"].keys())
practice_keys = [k for k in los_keys if "MOCK" not in k]

# --- TOP BAR ---
selected_los = st.selectbox("📂 Select Learning Outcome (LOS):", practice_keys)

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["📝 Practice", "🃏 Flashcards", "💀 Brutal Mock", "📊 Stats"])

# --- TAB 1: PRACTICE ---
with tab1:
    if selected_los:
        if not library["Economics"][selected_los]["Hard (Exam Level)"]:
            st.info("🚧 Questions coming soon.")
        else:
            available_levels = [k for k in library["Economics"][selected_los].keys() if "Flashcard" not in k]
            level = st.radio("Difficulty:", available_levels, horizontal=True)
            
            q_list = library["Economics"][selected_los][level]
            total = len(q_list)
            idx = st.session_state.q_idx
            
            # Boundary Check
            if idx >= total: idx = total - 1
            if idx < 0: idx = 0
            
            q = q_list[idx]
            
            # Header with Specific Reset
            c_head1, c_head2 = st.columns([3, 1])
            c_head1.caption(f"Question {idx+1} of {total}")
            if c_head2.button("🔄 Reset Module"):
                st.session_state.q_idx = 0
                st.session_state.score = 0
                st.session_state.checked = False
                st.rerun()

            st.progress((idx+1)/total)
            
            # Content
            if "chart" in q: st.plotly_chart(get_chart(q['chart']), use_container_width=True)
            st.markdown(f"### {q['q']}")
            choice = st.radio("Select Answer:", q['opt'], key=f"q_{idx}")
            
            # Nav Buttons
            c1, c2, c3 = st.columns([1, 2, 1])
            
            if idx > 0:
                if c1.button("⬅️ Prev"):
                    st.session_state.q_idx -= 1
                    st.session_state.checked = False
                    st.rerun()
            
            if c2.button("Check Answer", use_container_width=True):
                st.session_state.checked = True
            
            if idx < total - 1:
                if c3.button("Next ➡️"):
                    st.session_state.q_idx += 1
                    st.session_state.checked = False
                    st.rerun()
            else:
                if c3.button("Finish"):
                    st.balloons()
                    st.success(f"Score: {st.session_state.score}/{total}")
                    # Save to History
                    st.session_state.history.append({
                        "Time": datetime.now().strftime("%H:%M"),
                        "Module": selected_los,
                        "Score": f"{st.session_state.score}/{total}"
                    })

            if st.session_state.checked:
                if choice == q['ans']:
                    st.success(f"✅ Correct! \n\n{q['why']}")
                    if f"done_{selected_los}_{idx}" not in st.session_state:
                        st.session_state.score += 1
                        st.session_state[f"done_{selected_los}_{idx}"] = True
                else:
                    st.error(f"❌ Wrong. \n\n**Answer:** {q['ans']} \n\n**Reason:** {q['why']}")

# --- TAB 2: FLASHCARDS ---
with tab2:
    if selected_los and "Flashcards (10 Cards)" in library["Economics"][selected_los]:
        fc_deck = library["Economics"][selected_los]["Flashcards (10 Cards)"]
        if fc_deck:
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
                        f1, f2 = st.columns(2)
                        if fc_idx > 0:
                             if f1.button("⬅️ Back"): st.session_state.fc_idx -= 1; st.session_state.fc_flipped = False; st.rerun()
                        if f2.button("Next ➡️"): st.session_state.fc_idx += 1; st.session_state.fc_flipped = False; st.rerun()
            else:
                if st.button("Restart Deck"): st.session_state.fc_idx = 0; st.rerun()

# --- TAB 3: MOCK EXAM ---
with tab3:
    st.header("💀 The 300-Question Mock")
    
    # Mock Reset Button
    if st.button("🔄 Restart Mock Exam"):
        st.session_state.m_idx = 0
        st.session_state.m_score = 0
        st.rerun()

    if "MOCK EXAM" in library["Economics"]:
        mock_qs = library["Economics"]["MOCK EXAM"]["Full Mock"]
        if not mock_qs:
            st.info("🚧 Mock Exam loading...")
        else:
            m_idx = st.session_state.m_idx
            
            # Boundary Check
            if m_idx >= len(mock_qs): m_idx = len(mock_qs) - 1
            if m_idx < 0: m_idx = 0

            mq = mock_qs[m_idx]
            st.progress((m_idx+1)/len(mock_qs))
            st.write(f"**Mock Q{m_idx+1}**")
            st.markdown(f"### {mq['q']}")
            m_choice = st.radio("Select:", mq['opt'], key=f"m_{m_idx}")
            
            # Mock Nav
            mc1, mc2, mc3 = st.columns([1, 2, 1])
            
            # PREV
            if m_idx > 0:
                if mc1.button("⬅️ Prev", key="m_prev"):
                    st.session_state.m_idx -= 1
                    st.rerun()
            
            # SUBMIT
            if mc2.button("Submit Answer", key="m_sub"):
                if m_choice == mq['ans']: 
                    st.success("Correct")
                    st.session_state.m_score += 1
                else: 
                    st.error(f"Wrong. Answer: {mq['ans']}")
            
            # NEXT
            if m_idx < len(mock_qs) - 1:
                if mc3.button("Next ➡️", key="m_next"):
                    st.session_state.m_idx += 1
                    st.rerun()
            else:
                st.success(f"Mock Complete! Final Score: {st.session_state.m_score}/{len(mock_qs)}")

# --- TAB 4: HISTORY ---
with tab4:
    if st.session_state.history: st.dataframe(st.session_state.history)
    else: st.info("No history yet.")
