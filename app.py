import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==============================
# PAGE SETTINGS
# ==============================

# ==============================
# PROFESSIONAL DASHBOARD STYLE
# ==============================
import streamlit as st
import pandas as pd
import numpy as np
# other imports...

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #EDE7F6 0%,
        #F6F2FF 100%
    );
}
@media (max-width: 768px) {

    .block-container {
        padding-top: 1rem;
        padding-left: 4%;
        padding-right: 4%;
    }

    h1 {
        font-size: 1.8rem !important;
        line-height: 1.2 !important;
    }

    h2 {
        font-size: 1.35rem !important;
    }

    h3 {
        font-size: 1.1rem !important;
    }

    div[data-testid="stHorizontalBlock"] {
        flex-wrap: wrap;
    }

    div[data-testid="stMetric"] {
        margin-bottom: 10px;
    }

    .stPlotlyChart {
        width: 100% !important;
    }
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {
    color: #2D2342 !important;
}

[data-testid="stSidebar"] h2 {
    font-weight: 700;
}

[data-testid="stSidebar"] div[data-baseweb="select"] {
    background-color: white;
    border-radius: 10px;
}

.stApp {
    background: #FAFAFC;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #E8E3F0;
    box-shadow: 0 4px 15px rgba(60, 40, 90, 0.08);
}

h1, h2, h3 {
    color: #29263A;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# YOUR EXISTING CODE STARTS HERE
# ==============================

st.set_page_config(
    page_title="India Forecast Confidence System",
    layout="wide"
)

# rest of your app.py...

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    font-size: 2.4rem !important;
    font-weight: 700 !important;
}

h2, h3 {
    font-weight: 650 !important;
}

[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
}

[data-testid="stMetricLabel"] {
    font-size: 0.95rem;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    font-size: 1.8rem;
    font-weight: 700;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #F3EEFF 0%, #E9DEFF 100%);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.stDataFrame {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
# ==============================
# LOAD FINAL DATA
# ==============================

DATA_PATH = "FINAL_FORECAST_RESULTS.csv"

df = pd.read_csv(DATA_PATH)

# ==============================
# TITLE
# ==============================

st.title("🌧️ India Forecast Confidence System")

st.write(
    "AI-based Forecast Bust Detection and Confidence Analysis"
)

st.write(
    "This system combines GFS weather forecasts, historical forecast "
    "errors, machine learning, and a Forecast Stress Score."
)

# ==============================
# SIDEBAR
# ==============================

st.sidebar.header("Forecast Controls")

selected_day = st.sidebar.selectbox(
    "Select Forecast Day",
    sorted(df["lead_day"].unique())
)

selected_state = st.sidebar.selectbox(
    "Select State",
    ["All India"] + sorted(df["state_name"].unique())
)

# ==============================
# FILTER DATA
# ==============================

day_data = df[df["lead_day"] == selected_day].copy()

if selected_state == "All India":
    display_data = day_data.copy()
else:
    display_data = day_data[
        day_data["state_name"] == selected_state
    ].copy()

# ==============================
# KPI SECTION
# ==============================
# ==============================
# PROFESSIONAL KPI CARDS
# ==============================

avg_probability = display_data["bust_probability"].mean() * 100
avg_stress = display_data["stress_score"].mean()
avg_temperature = display_data["temperature_C"].mean()
avg_rainfall = display_data["rfs"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🎯 Bust Probability",
        value=f"{avg_probability:.1f}%",
        help="Average predicted probability of a forecast bust."
    )

with col2:
    st.metric(
        label="⚠️ Forecast Stress",
        value=f"{avg_stress:.1f}/100",
        help="Overall forecast stress score."
    )

with col3:
    st.metric(
        label="🌡️ Temperature",
        value=f"{avg_temperature:.1f} °C",
        help="Average forecast temperature."
    )

with col4:
    st.metric(
        label="🌧️ Rainfall",
        value=f"{avg_rainfall:.2f} mm",
        help="Average forecast rainfall."
    )

# ==============================
# INDIA MAP
# ==============================

st.subheader("🗺️ Forecast Stress Map")

fig = px.scatter_map(
    day_data,
    lat="latitude",
    lon="longitude",
    color="stress_score",
    size="bust_probability",
    hover_name="state_name",
    hover_data=[
        "bust_probability",
        "stress_score",
        "confidence",
        "rfs",
        "temperature_C",
        "r2",
        "wind_speed"
    ],
    zoom=4,
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==============================
# SELECTED STATE DETAILS
# ==============================

if selected_state != "All India":

    row = display_data.iloc[0]

    st.subheader(
        f"📍 {selected_state} — Day {selected_day}"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Bust Probability",
            f"{row['bust_probability'] * 100:.1f}%"
        )

    with c2:
        st.metric(
            "Stress Score",
            f"{row['stress_score']:.1f}/100"
        )

    with c3:
        st.metric(
            "Rainfall",
            f"{row['rfs']:.2f} mm"
        )

    with c4:
        st.metric(
            "Temperature",
            f"{row['temperature_C']:.1f} °C"
        )

    st.info(
        f"Confidence: {row['confidence']}"
    )

    st.warning(
        f"Why? {row['risk_reasons']}"
    )

# ==============================
# DATA TABLE
# ==============================

st.subheader("📊 Forecast Details")

table_columns = [
    "state_name",
    "lead_day",
    "rfs",
    "temperature_C",
    "r2",
    "wind_speed",
    "bust_probability",
    "stress_score",
    "confidence",
    "risk_reasons"
]

st.dataframe(
    display_data[table_columns],
    use_container_width=True,
    hide_index=True
)
# ==============================
# DOWNLOAD FORECAST RESULTS
# ==============================

st.subheader("📥 Download Results")

download_data = display_data[table_columns].copy()

csv = download_data.to_csv(index=False)

st.download_button(
    label="📥 Download Forecast CSV",
    data=csv,
    file_name=f"{selected_state}_day_{selected_day}_forecast.csv",
    mime="text/csv",
    width="stretch"
)

# ==============================
# FORECAST RISK ANALYSIS
# ==============================

import plotly.express as px

st.subheader("📊 Forecast Risk Analysis")

chart_data = display_data[
    ["state_name", "bust_probability", "stress_score"]
].copy()

# Convert bust probability to percentage
chart_data["Bust Probability (%)"] = (
    chart_data["bust_probability"] * 100
)

# Create interactive chart
fig = px.bar(
    chart_data,
    x="state_name",
    y=["Bust Probability (%)", "stress_score"],
    barmode="group",
    title="Forecast Risk by State",
    labels={
        "state_name": "State",
        "value": "Risk Score",
        "variable": "Metric"
    }
)

fig.update_layout(
    height=450,
    xaxis_title="State",
    yaxis_title="Risk / Probability",
    legend_title="Risk Metrics",
    hovermode="x unified",
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# ==============================
# 10-DAY BUST PROBABILITY TREND
# ==============================

st.subheader("📈 10-Day Bust Probability Trend")

trend_data = (
    df.groupby("lead_day")["bust_probability"]
    .mean()
    .reset_index()
)

trend_data["bust_probability"] = (
    trend_data["bust_probability"] * 100
)

fig_trend = go.Figure()

fig_trend.add_trace(
    go.Scatter(
        x=trend_data["lead_day"],
        y=trend_data["bust_probability"],
        mode="lines+markers",
        name="Bust Probability",
        line=dict(width=4),
        marker=dict(size=9),
        hovertemplate="Day %{x}<br>Probability: %{y:.1f}%<extra></extra>"
    )
)

fig_trend.update_layout(
    title="Predicted Forecast-Bust Risk Across Lead Days",
    xaxis_title="Forecast Lead Day",
    yaxis_title="Bust Probability (%)",
    xaxis=dict(
        tickmode="linear",
        dtick=1
    ),
    height=450,
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)


# ==============================
# HIGH-RISK STATES
# ==============================
# ==============================
# HIGH-RISK STATES
# ==============================
# ==============================
# HIGH-RISK STATES
# ==============================

st.subheader("🚨 Highest Risk States")

risk_data = (
    display_data[
        ["state_name", "bust_probability"]
    ]
    .copy()
)

risk_data["Bust Probability (%)"] = (
    risk_data["bust_probability"] * 100
)

risk_data = (
    risk_data
    .sort_values("Bust Probability (%)", ascending=True)
    .tail(10)
)

fig_risk = go.Figure()

fig_risk.add_trace(
    go.Bar(
        y=risk_data["state_name"],
        x=risk_data["Bust Probability (%)"],
        orientation="h",
        text=[
            f"{x:.1f}%"
            for x in risk_data["Bust Probability (%)"]
        ],
        textposition="outside",
        marker=dict(
            line=dict(width=0)
        ),
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Bust Probability: %{x:.1f}%"
            "<extra></extra>"
        )
    )
)

fig_risk.update_layout(
    title=f"Top 10 Highest-Risk States — Day {selected_day}",
    xaxis_title="Bust Probability (%)",
    yaxis_title=None,
    height=480,
    template="plotly_white",
    showlegend=False,
    margin=dict(
        l=20,
        r=70,
        t=70,
        b=40
    )
)

fig_risk.update_xaxes(
    ticksuffix="%",
    showgrid=True
)

st.plotly_chart(
    fig_risk,
    width="stretch"
)
# ==============================
# 10-DAY WEATHER TREND
# ==============================

# ==============================
# 10-DAY WEATHER TREND
# ==============================

# ==============================
# 10-DAY WEATHER TREND
# ==============================

st.subheader("🌦️ 10-Day Weather Trend")

if selected_state == "All India":

    st.info(
        "Select a state from the sidebar to view its 10-day weather trend."
    )

else:

    state_trend = (
        df[df["state_name"] == selected_state]
        .sort_values("lead_day")
        .copy()
    )

    col1, col2 = st.columns(2)

    # ==================================
    # TEMPERATURE FORECAST
    # ==================================

    with col1:

        fig_temp = go.Figure()

        fig_temp.add_trace(
            go.Scatter(
                x=state_trend["lead_day"],
                y=state_trend["temperature_C"],
                mode="lines+markers",
                name="Temperature",
                line=dict(width=3),
                marker=dict(size=8),
                hovertemplate=(
                    "<b>Day %{x}</b><br>"
                    "Temperature: %{y:.1f} °C"
                    "<extra></extra>"
                )
            )
        )

        fig_temp.update_layout(
            title="🌡️ Temperature Forecast",
            xaxis_title="Forecast Day",
            yaxis_title="Temperature (°C)",
            height=400,
            template="plotly_white",
            hovermode="x unified",
            margin=dict(l=20, r=20, t=60, b=40)
        )

        fig_temp.update_xaxes(
            tickmode="linear",
            dtick=1
        )

        st.plotly_chart(
            fig_temp,
            width="stretch"
        )

    # ==================================
    # RAINFALL FORECAST
    # ==================================

    with col2:

        fig_rain = go.Figure()

        fig_rain.add_trace(
            go.Bar(
                x=state_trend["lead_day"],
                y=state_trend["rfs"],
                name="Rainfall",
                text=[
                    f"{x:.1f} mm"
                    for x in state_trend["rfs"]
                ],
                textposition="outside",
                hovertemplate=(
                    "<b>Day %{x}</b><br>"
                    "Rainfall: %{y:.2f} mm"
                    "<extra></extra>"
                )
            )
        )

        fig_rain.update_layout(
            title="🌧️ Rainfall Forecast",
            xaxis_title="Forecast Day",
            yaxis_title="Rainfall (mm)",
            height=400,
            template="plotly_white",
            hovermode="x unified",
            margin=dict(l=20, r=20, t=60, b=40)
        )

        fig_rain.update_xaxes(
            tickmode="linear",
            dtick=1
        )

        st.plotly_chart(
            fig_rain,
            width="stretch"
        )