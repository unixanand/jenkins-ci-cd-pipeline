# app.py - Modern Streamlit Demo (2025 style)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

# ─────────────────────────────────────────────────────────────
# Page config - must be the very first Streamlit command
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Modern Streamlit Demo",
    page_icon="Chart with upwards trend",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': '# Modern Streamlit Demo\nBuilt in 2025!'
    }
)

# ─────────────────────────────────────────────────────────────
# Custom CSS for a sleek look
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main {background-color: #0e1117; color: #fafafa;}
    .stPlotlyChart {background-color: #1e1e1e !important;}
    .css-1d391kg {padding-top: 2rem;}
    .success-box {padding: 1rem; border-radius: 10px; background: #1f7a1f; color: white;}
    h1, h2, h3 {color: #ff6e6e !important;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
    st.title("Modern Streamlit Demo")
    st.caption(f"Running on EC2 • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    option = st.selectbox(
        "Choose a demo",
        ["Interactive Dashboard", "Data Explorer", "Live Counter", "Chat Simulator", "File Uploader"]
    )
    
    st.markdown("---")
    st.markdown("Made with Streamlit")

# ─────────────────────────────────────────────────────────────
# Main content
# ─────────────────────────────────────────────────────────────
if option == "Interactive Dashboard":
    st.title("Interactive Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Temperature", "24 °C", "2 °C")
    with col2: st.metric("Revenue", "$12,480", "-8%")
    with col3: st.metric("Active Users", "1,234", "12%")
    with col4: st.metric("Latency", "87 ms", "-5 ms")
    
    # Sample data
    df = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=100),
        "sales": np.random.randn(100).cumsum() + 100,
        "visits": np.random.randint(50, 500, 100),
        "conversion": np.random.uniform(2, 8, 100)
    })
    
    tab1, tab2 = st.tabs(["Line Chart", "Scatter Plot"])
    
    with tab1:
        fig = px.line(df, x="date", y=["sales", "visits"], 
                      title="Sales & Visits Over Time")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig2 = px.scatter(df, x="visits", y="sales", size="conversion", color="conversion",
                          hover_data=["date"], title="Visits vs Sales")
        st.plotly_chart(fig2, use_container_width=True)

elif option == "Data Explorer":
    st.title("Data Explorer")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
        st.line_chart(df.select_dtypes(include="number"))
    else:
        st.info("Upload a CSV file to explore")

elif option == "Live Counter":
    st.title("Live Counter + Progress")
    
    placeholder = st.empty()
    progress_bar = st.progress(0)
    
    for i in range(101):
        with placeholder.container():
            st.markdown(f"### Count: **{i}** %")
            st.progress(i)
        time.sleep(0.05)
    
    st.balloons()
    st.success("Live demo completed!")

elif option == "Chat Simulator":
    st.title("Chat Interface")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your EC2-based AI assistant."}]
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        response = f"Echo (from private EC2): {prompt.upper()}"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

elif option == "File Uploader":
    st.title("File Uploader & Preview")
    uploaded = st.file_uploader("Drop any file", type=None)
    if uploaded:
        st.success(f"Received: {uploaded.name} ({uploaded.size:,} bytes)")
        if uploaded.type.startswith("image/"):
            st.image(uploaded)
        elif uploaded.type == "text/csv":
            df = pd.read_csv(uploaded)
            st.dataframe(df)

# Footer
st.markdown("---")
st.caption("Modern Streamlit app running on your private EC2 • Fully headless • No local tunnel needed!")
