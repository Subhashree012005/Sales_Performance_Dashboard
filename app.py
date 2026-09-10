import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from queries import (
    get_kpi_summary,
    get_revenue_by_salesperson,
    get_monthly_trend,
    get_region_performance,
    get_product_performance,
    get_top_orders,
    get_ranked_by_region,
)

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS — background + custom styling ──────────────────
st.markdown("""
<style>
/* ---------- BACKGROUND ---------- */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    background-attachment: fixed;
}

/* ---------- MAIN CONTENT AREA ---------- */
.main .block-container {
    background: rgba(255, 255, 255, 0.04);
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin-top: 1rem;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
}

/* ---------- HERO HEADER ---------- */
.hero-wrap {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero-title {
    font-size: 80px !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    letter-spacing: -0.5px;
    margin: 0;
    line-height: 1.15;
}

.hero-title span {
    background: linear-gradient(90deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    color: rgba(255,255,255,0.5);
    font-size: 0.95rem;
    margin-top: 0.5rem;
}

/* ---------- SECTION LABELS ---------- */
.section-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: #a78bfa;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
    margin-top: 2rem;
}
.section-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 1rem;
}

/* ---------- KPI CARDS ---------- */
.kpi-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    text-align: center;
    transition: border-color 0.2s;
}
.kpi-card:hover { border-color: rgba(167,139,250,0.5); }
.kpi-icon { font-size: 1.6rem; margin-bottom: 0.4rem; }
.kpi-value {
    font-size: 1.75rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.1;
}
.kpi-label {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.45);
    margin-top: 0.3rem;
}

/* ---------- INSIGHT BOX ---------- */
.insight-box {
    background: linear-gradient(135deg, rgba(167,139,250,0.15), rgba(96,165,250,0.1));
    border: 1px solid rgba(167,139,250,0.3);
    border-radius: 12px;
    padding: 1rem 1.4rem;
    margin: 1.2rem 0;
    color: rgba(255,255,255,0.85);
    font-size: 0.9rem;
    line-height: 1.6;
}
.insight-box b { color: #c4b5fd; }

/* ---------- DIVIDER ---------- */
.custom-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 2rem 0;
}

/* ---------- PLOTLY CHART BACKGROUND FIX ---------- */
.js-plotly-plot { border-radius: 14px; overflow: hidden; }

/* ---------- DATAFRAME STYLING ---------- */
.stDataFrame {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: rgba(255,255,255,0.25);
    font-size: 0.78rem;
    padding: 1.5rem 0 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ── Plotly common theme (dark + transparent) ──────────────────
CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,0.03)",
    font=dict(color="rgba(255,255,255,0.75)", size=12),
    margin=dict(l=20, r=20, t=40, b=20),
    xaxis=dict(gridcolor="rgba(255,255,255,0.06)", linecolor="rgba(255,255,255,0.1)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.06)", linecolor="rgba(255,255,255,0.1)"),
    height=380,
)
PURPLE_BLUE = ["#a78bfa", "#818cf8", "#60a5fa", "#34d399", "#f472b6"]

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <p class="hero-title">Sales Performance <span>Dashboard</span></p>
    <p class="hero-sub">2023 Annual Report &nbsp;·&nbsp; 500 Orders &nbsp;·&nbsp; 5 Salespeople &nbsp;·&nbsp; 4 Regions</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# KPI CARDS
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">At a Glance</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Key Metrics for 2023</p>', unsafe_allow_html=True)

kpi = get_kpi_summary().iloc[0]
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">💰</div>
        <div class="kpi-value">₹{kpi['total_revenue']:,.0f}</div>
        <div class="kpi-label">Total Revenue</div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">🛒</div>
        <div class="kpi-value">{kpi['total_orders']:,}</div>
        <div class="kpi-label">Total Orders</div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">📦</div>
        <div class="kpi-value">{kpi['total_units_sold']:,}</div>
        <div class="kpi-label">Units Sold</div>
    </div>""", unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">📈</div>
        <div class="kpi-value">₹{kpi['avg_order_value']:,.0f}</div>
        <div class="kpi-label">Avg Order Value</div>
    </div>""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SALESPERSON PERFORMANCE
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">Who Sold the Most</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Revenue by Salesperson</p>', unsafe_allow_html=True)

sales_df = get_revenue_by_salesperson()
top_name  = sales_df.iloc[0]["salesperson"]
top_rev   = sales_df.iloc[0]["total_revenue"]

fig1 = go.Figure(go.Bar(
    x=sales_df["salesperson"],
    y=sales_df["total_revenue"],
    marker=dict(
        color=sales_df["total_revenue"],
        colorscale=[[0, "#4f46e5"], [0.5, "#7c3aed"], [1, "#a78bfa"]],
        line=dict(color="rgba(255,255,255,0.05)", width=1),
    ),
    text=[f"₹{v:,.0f}" for v in sales_df["total_revenue"]],
    textposition="outside",
    textfont=dict(color="rgba(255,255,255,0.8)", size=11),
    hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>",
))
fig1.update_layout(**CHART_LAYOUT, title="")
fig1.update_yaxes(title_text="Revenue (₹)")
st.plotly_chart(fig1, use_container_width=True)

st.markdown(f"""
<div class="insight-box">
    💡 <b>{top_name}</b> is the top performer with <b>₹{top_rev:,.0f}</b> in revenue —
    leading the team. Managers can use this breakdown to identify coaching
    opportunities for lower-ranked salespeople.
</div>""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# MONTHLY TREND
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">How Did We Perform Over Time</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Monthly Revenue Trend</p>', unsafe_allow_html=True)

monthly_df  = get_monthly_trend()
best_month  = monthly_df.loc[monthly_df["monthly_revenue"].idxmax()]
worst_month = monthly_df.loc[monthly_df["monthly_revenue"].idxmin()]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=monthly_df["month"],
    y=monthly_df["monthly_revenue"],
    mode="lines+markers",
    line=dict(color="#a78bfa", width=2.5),
    marker=dict(color="#ffffff", size=7, line=dict(color="#a78bfa", width=2)),
    fill="tozeroy",
    fillcolor="rgba(167,139,250,0.08)",
    hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>",
))
fig2.update_layout(**CHART_LAYOUT)
fig2.update_yaxes(title_text="Revenue (₹)")
st.plotly_chart(fig2, use_container_width=True)

st.markdown(f"""
<div class="insight-box">
    💡 Best month was <b>{best_month['month']}</b> at <b>₹{best_month['monthly_revenue']:,.0f}</b>.
    Weakest month was <b>{worst_month['month']}</b> at <b>₹{worst_month['monthly_revenue']:,.0f}</b>.
    Seasonal dips like this can guide when to run promotions or push marketing campaigns.
</div>""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# REGION PERFORMANCE
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">Where Did We Sell</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Region Performance</p>', unsafe_allow_html=True)

region_df  = get_region_performance()
best_region = region_df.iloc[0]
weak_region = region_df.iloc[-1]

col_l, col_r = st.columns([1, 1])

with col_l:
    fig3 = go.Figure(go.Pie(
        labels=region_df["region"],
        values=region_df["total_revenue"],
        hole=0.5,
        marker=dict(colors=PURPLE_BLUE, line=dict(color="#1a1a2e", width=2)),
        textinfo="label+percent",
        textfont=dict(color="white", size=12),
        hovertemplate="<b>%{label}</b><br>Revenue: ₹%{value:,.0f}<br>Share: %{percent}<extra></extra>",
    ))
    fig3.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        margin=dict(l=10, r=10, t=10, b=10),
        height=340,
        showlegend=True,
        legend=dict(font=dict(color="rgba(255,255,255,0.6)")),
    )
    st.plotly_chart(fig3, use_container_width=True)

with col_r:
    st.markdown("<br>", unsafe_allow_html=True)
    for _, row in region_df.iterrows():
        pct = row["revenue_share_pct"]
        st.markdown(f"""
        <div style="margin-bottom:0.9rem;">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                <span style="color:rgba(255,255,255,0.8);font-size:0.9rem;">{row['region']}</span>
                <span style="color:#a78bfa;font-size:0.9rem;font-weight:600;">{pct}%</span>
            </div>
            <div style="background:rgba(255,255,255,0.08);border-radius:6px;height:8px;">
                <div style="background:linear-gradient(90deg,#a78bfa,#60a5fa);
                            width:{pct}%;height:100%;border-radius:6px;"></div>
            </div>
            <div style="color:rgba(255,255,255,0.35);font-size:0.75rem;margin-top:3px;">
                ₹{row['total_revenue']:,.0f} &nbsp;·&nbsp; {row['total_orders']} orders
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown(f"""
<div class="insight-box">
    💡 <b>{best_region['region']}</b> leads with {best_region['revenue_share_pct']}% revenue share.
    <b>{weak_region['region']}</b> is the weakest at {weak_region['revenue_share_pct']}% —
    a potential area to increase sales focus or investigate why orders are fewer.
</div>""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# PRODUCT PERFORMANCE
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">What Did We Sell</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Product Performance</p>', unsafe_allow_html=True)

product_df = get_product_performance()

fig4 = go.Figure(go.Bar(
    x=product_df["product"],
    y=product_df["total_revenue"],
    marker=dict(
        color=PURPLE_BLUE[:3],
        line=dict(color="rgba(255,255,255,0.05)", width=1),
    ),
    text=[f"₹{v:,.0f}" for v in product_df["total_revenue"]],
    textposition="outside",
    textfont=dict(color="rgba(255,255,255,0.8)", size=12),
    hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>",
))
fig4.update_layout(**CHART_LAYOUT)
fig4.update_yaxes(title_text="Revenue (₹)")
st.plotly_chart(fig4, use_container_width=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# WINDOW FUNCTION TABLE — Rank by Region
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">SQL Window Function in Action</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Salesperson Rank Within Each Region</p>', unsafe_allow_html=True)

rank_df = get_ranked_by_region()
st.dataframe(
    rank_df.rename(columns={
        "region": "Region",
        "salesperson": "Salesperson",
        "total_revenue": "Revenue (₹)",
        "rank_in_region": "Rank in Region",
    }),
    use_container_width=True,
    hide_index=True,
)

st.markdown("""
<div class="insight-box">
    💡 This table is built using a <b>SQL Window Function — RANK() OVER (PARTITION BY region)</b>.
    It ranks each salesperson independently within their region, so rank 1 in North
    and rank 1 in South are separate — not compared against each other.
    This is an advanced SQL concept that most freshers don't know.
</div>""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# TOP 10 ORDERS TABLE
# ═══════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">Highest Value Deals</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Top 10 Orders by Revenue</p>', unsafe_allow_html=True)

top_df = get_top_orders()
st.dataframe(
    top_df.rename(columns={
        "order_id": "Order ID",
        "date": "Date",
        "salesperson": "Salesperson",
        "region": "Region",
        "product": "Product",
        "revenue": "Revenue (₹)",
    }),
    use_container_width=True,
    hide_index=True,
)

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    Built with SQL · Python · Streamlit &nbsp;|&nbsp;
    github.com/yourusername/sales-dashboard
</div>""", unsafe_allow_html=True)