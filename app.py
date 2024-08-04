import streamlit as st
import pythoncom
import win32com.client
import pandas as pd
import polars as pl
from tasklit.components.create_task import create_task
from tasklit.functions.functions import get_tasks_by_folder

# =================================================================================================
# Streamlit application
st.title(":clock2: TaskLit")
# =================================================================================================

# =================================================================================================
# Button Components
button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)

with button_col1:
    st.button(label="Create Task", use_container_width=True, on_click=create_task)
# =================================================================================================


# =================================================================================================
# Task Statistics
st.header("_Statistics_", divider=True)
tasks = get_tasks_by_folder()
number_of_tasks = tasks.total_task_count()
number_of_missed_runs = tasks.total_missed_runs()
task_by_state = tasks.task_states()

stats_col1, stats_col2 = st.columns([0.4,0.6])
with stats_col1:
    st.write(f"Total number of tasks: {number_of_tasks}")
    st.write(f"Total number of missed runs: {number_of_missed_runs}")
with stats_col2:
    st.dataframe(task_by_state, hide_index=True, use_container_width=True)
# task_df = pl.DataFrame(tasks).to_pandas()
# st.dataframe(task_df, hide_index=True, use_container_width=True)
# =================================================================================================