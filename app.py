import streamlit as st
import pandas as pd
import polars as pl
import pythoncom
import win32com.client

from tasklit.components.components import create_task

# from tasklit.functions.functions import get_tasks_by_folder

# Connect to Task Scheduler
pythoncom.CoInitialize()
scheduler = win32com.client.Dispatch("Schedule.Service")

if "client" not in st.session_state:
    st.session_state["client"] = scheduler

# =================================================================================================
# Streamlit application
# =================================================================================================
st.title(":clock2: TaskLit")

# Buttons
button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)

with button_col1:
    st.button(label="Create Task", use_container_width=True, on_click=create_task)

st.divider()


# tasks = get_tasks_by_folder(scheduler, "ZBI_Tasks")
# task_df = pl.DataFrame(tasks).to_pandas()
# st.dataframe(task_df, hide_index=True, use_container_width=True)
