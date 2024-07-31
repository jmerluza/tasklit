import streamlit as st
import pandas as pd
import polars as pl
import win32com.client

from tasklit.functions.functions import get_tasks_by_folder

# Connect to Task Scheduler
scheduler = win32com.client.Dispatch("Schedule.Service")
scheduler.Connect()

# Streamlit application
with st.sidebar:
    st.title(":clock2: TaskLit")
    st.button(label="Create Task", use_container_width=True)
    st.button(label="Remove Task", use_container_width=True)
    st.button(label="Import Task", use_container_width=True)
    st.button(label="Run Task", use_container_width=True)

st.divider()


tasks = get_tasks_by_folder(scheduler, "ZBI_Tasks")
task_df = pl.DataFrame(tasks).to_pandas()
st.dataframe(task_df, hide_index=True, use_container_width=True)