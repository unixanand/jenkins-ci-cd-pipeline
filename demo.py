import streamlit as st
st.set_page_config(page_title="My EC2 Demo", layout="wide")
st.title("Streamlit on Ubuntu")
st.success("Running behind Nginx on port 8080")
st.sidebar.selectbox("Menu", ["Home", "Dashboard", "About"])
st.balloons()
