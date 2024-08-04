import streamlit as st
import pythoncom
import win32com.client
import pandas as pd
import polars as pl
from tasklit.components.create_task import create_task
from tasklit.functions.functions import get_tasks_by_folder, check_folder_exists

# =================================================================================================
# Streamlit application
st.set_page_config(layout="wide")
st.title(":clock2: TaskLit")
# =================================================================================================

# =================================================================================================
# Button Components
button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)

with button_col1:
    st.button(label="Create Task", use_container_width=True, on_click=create_task)
with button_col2:
    st.button(label="Manage Folders", use_container_width=True)
# =================================================================================================

# =================================================================================================
# Task Statistics
st.header("_Statistics_", divider=True)

a_stats_col1, a_stats_col2 = st.columns([0.1,0.9])
with a_stats_col1:
    folder = st.text_input("Search Folder", value="\\")

if check_folder_exists(folder):
    tasks = get_tasks_by_folder(folder)
    number_of_tasks = tasks.total_task_count()
    number_of_missed_runs = tasks.total_missed_runs()
    task_by_state = tasks.task_states()
    task_by_author = tasks.task_by_author()
    task_by_result = tasks.task_results()

    st.write(f"Total number of tasks: {number_of_tasks}")
    st.write(f"Total number of missed runs: {number_of_missed_runs}")

    b_stats_col1, b_stats_col2, b_stats_col3 = st.columns([0.3,0.3,0.4])
    with b_stats_col1:
        st.subheader("_Tasks by state_",divider="green")
        st.dataframe(task_by_state, hide_index=True, use_container_width=True)  
    with b_stats_col2:
        st.subheader("_Tasks by result_",divider="green")
        st.dataframe(task_by_result, hide_index=True, use_container_width=True)
    with b_stats_col3:
        st.subheader("_Tasks by author_",divider="green")
        st.dataframe(task_by_author, hide_index=True, use_container_width=True)

    # =================================================================================================
else:
    st.error(f"{folder} folder does not exist!")