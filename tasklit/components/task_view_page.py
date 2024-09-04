import streamlit as st
from pytask_scheduler import get_task_scheduler_history

def view_task_component():
    pass

def task_history():
    if "task_history" not in st.session_state:
        st.session_state.task_history = get_task_scheduler_history()
