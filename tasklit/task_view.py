import streamlit as st
from components.task_view_page import task_history

st.header(":material/view_day: View Task")
st.write("_View and edit task properties and view task history statistics._")
task_history()

st.dataframe(st.session_state.task_history)
