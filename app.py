import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from auth import create_users_table, register_user, login_user

from scoring_engine import (
    calculate_growth_potential,
    calculate_saturation_risk,
    calculate_consistency_score,
    calculate_monetization_readiness
)

from projection_engine import project_growth
from lever_detection import detect_growth_levers
from experiment_engine import generate_experiment_plan
from llm_engine import generate_ai_strategy
from report_generator import generate_pdf_report


# -----------------------------
# INIT DATABASE
# -----------------------------

create_users_table()


# -----------------------------
# SESSION STATES
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "login"


# -----------------------------
# LOGIN / SIGNUP PAGE
# -----------------------------

if not st.session_state.logged_in:

    st.title("🚀 Creator's Lab")
    st.markdown("### AI Growth Intelligence for Creators")

    if st.session_state.auth_mode == "login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if login_user(username, password):

                st.session_state.logged_in = True
                st.success("Login successful")
                st.rerun()

            else:
                st.error("Invalid username or password")

        st.write("Don't have an account?")

        if st.button("Create Account"):
            st.session_state.auth_mode = "signup"
            st.rerun()

    else:

        st.subheader("Create Account")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type="password")

        if st.button("Sign Up"):

            if register_user(new_user, new_password):

                st.success("Account created. Please login.")
                st.session_state.auth_mode = "login"
                st.rerun()

            else:
                st.error("Username already exists")

        st.write("Already have an account?")

        if st.button("Back to Login"):
            st.session_state.auth_mode = "login"
            st.rerun()

    st.stop()


# -----------------------------
# DASHBOARD
# -----------------------------

st.set_page_config(
    page_title="Creator's Lab",
    page_icon="🚀",
    layout="wide"
)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


st.title("🚀 Creator's Lab Dashboard")
st.caption("Engineer Your Growth")

st.divider()


# -----------------------------
# INPUT FORM
# -----------------------------

st.header("Creator Analysis Input")

with st.form("creator_input_form"):

    col1, col2 = st.columns(2)

    with col1:

        followers = st.number_input("Current Followers", min_value=0, step=100)

        engagement_rate = st.number_input(
            "Engagement Rate (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1
        )

        posts_per_week = st.slider(
            "Posts per Week",
            min_value=0,
            max_value=14,
            value=3
        )

    with col2:

        niche = st.selectbox(
            "Content Niche",
            ["Fitness", "Tech", "Travel", "Education", "Finance", "Lifestyle"]
        )

        content_format = st.selectbox(
            "Primary Content Format",
            ["Reels", "Carousel", "Photos", "Mixed"]
        )

    analyze_button = st.form_submit_button("Analyze Growth")


# -----------------------------
# ANALYSIS
# -----------------------------

if analyze_button:

    st.divider()

    growth_index = calculate_growth_potential(
        followers, engagement_rate, posts_per_week
    )

    saturation_score = calculate_saturation_risk(niche)

    consistency_score = calculate_consistency_score(posts_per_week)

    monetization_score = calculate_monetization_readiness(
        followers, engagement_rate
    )

    projection = project_growth(
        followers, engagement_rate, posts_per_week
    )

    primary_lever, secondary_lever = detect_growth_levers(
        followers, engagement_rate, posts_per_week
    )

    strategy_type, experiment_plan = generate_experiment_plan(
        engagement_rate, posts_per_week, content_format
    )

    st.header("Growth Intelligence")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Growth Potential", growth_index)
    col2.metric("Saturation Risk", saturation_score)
    col3.metric("Consistency Score", consistency_score)
    col4.metric("Monetization Readiness", monetization_score)

    st.divider()

    st.header("Growth Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=growth_index,
            title={'text': "Growth Potential Index"},
            gauge={'axis': {'range': [0, 100]}}
        ))

        st.plotly_chart(gauge, use_container_width=True)

    with col2:

        radar_data = pd.DataFrame({
            "Metric": [
                "Growth Potential",
                "Saturation",
                "Consistency",
                "Monetization"
            ],
            "Score": [
                growth_index,
                saturation_score,
                consistency_score,
                monetization_score
            ]
        })

        radar = px.line_polar(
            radar_data,
            r="Score",
            theta="Metric",
            line_close=True
        )

        radar.update_traces(fill='toself')

        st.plotly_chart(radar, use_container_width=True)

    st.divider()

    st.header("Growth Projection")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("3 Month Conservative", projection["3m_low"])
        st.metric("3 Month Expected", projection["3m_mid"])
        st.metric("3 Month Aggressive", projection["3m_high"])

    with col2:
        st.metric("6 Month Projection", projection["6m"])

    projection_data = pd.DataFrame({
        "Month": ["Now", "3 Months", "6 Months"],
        "Followers": [
            followers,
            projection["3m_mid"],
            projection["6m"]
        ]
    })

    fig = px.line(
        projection_data,
        x="Month",
        y="Followers",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.header("Strategic Insights")

    col1, col2 = st.columns(2)

    col1.info(f"Primary Lever: {primary_lever}")
    col2.info(f"Secondary Opportunity: {secondary_lever}")

    st.divider()

    st.header("4 Week Content Plan")

    st.write(f"Strategy Mode: **{strategy_type}**")

    for week, posts in experiment_plan.items():

        st.subheader(week)

        for post in posts:
            st.write(f"- {post}")

    st.divider()

    st.header("AI Growth Strategy")

    ai_strategy = generate_ai_strategy(
        followers,
        engagement_rate,
        posts_per_week,
        niche,
        content_format,
        growth_index,
        primary_lever,
        projection["3m_mid"]
    )

    st.write(ai_strategy)

    report_path = generate_pdf_report(
        followers,
        engagement_rate,
        posts_per_week,
        growth_index,
        saturation_score,
        consistency_score,
        monetization_score,
        primary_lever,
        secondary_lever,
        ai_strategy
    )

    with open(report_path, "rb") as file:
        st.download_button(
            label="Download Growth Report (PDF)",
            data=file,
            file_name="creator_growth_report.pdf",
            mime="application/pdf"
        )