import streamlit as st

st.header("Create New Task")

folder = st.selectbox("Select folder", ["\\"] + st.session_state.folders)