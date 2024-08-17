import os
import streamlit as st
import polars as pl
from tasklit.functions.functions import connect_to_task_scheduler
from tasklit.frames import get_tasks

st.set_page_config(page_title="TaskLit", layout="wide", initial_sidebar_state="expanded")
st.title(":orange[:material/fireplace:] :red[TaskLit]")

# =================================================================================================
# Initializations
# =================================================================================================

# initialize task scheduler connection.
if "scheduler_client" not in st.session_state:
    st.session_state.scheduler_client = connect_to_task_scheduler()

# initialize tasks data frame.
if "tasks_df" not in st.session_state:
    st.session_state.tasks_df = get_tasks()

# initialize folder list options.
# if "folder_options" not in st.session_state:
#     st.session_state.folder_options = st.session_state.tasks_df["folder_name"].unique(maintain_order=True).to_list()

scheduler = st.session_state.scheduler_client

number_of_running_tasks = st.session_state.tasks_df.total_number_of_tasks_by_state("RUNNING")
number_of_ready_tasks = st.session_state.tasks_df.total_number_of_tasks_by_state("READY")
number_of_missed_runs = st.session_state.tasks_df.total_number_of_missed_runs()
number_of_disabled_tasks = st.session_state.tasks_df.total_number_of_tasks_by_state("DISABLED")

filter_col1, filter_col2, filter_col3 = st.columns([0.2,0.2,0.6])
with filter_col1:
    author_filter = st.text_input("Task Author", value=os.getlogin())
with filter_col2:
    folder_options = (
        get_tasks()
        .filter(pl.col("author").str.contains(author_filter))
        ["folder_name"]
        .unique(maintain_order=True)
        .to_list()
    )
    folder_select = st.selectbox("Select folder", options=folder_options)

metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = st.columns([0.1,0.1,0.1,0.1,0.6])
with metric_col1:
    with st.container(border=True):
        st.metric(":blue[:material/sprint: RUNNING TASKS]", number_of_running_tasks)
with metric_col2:
    with st.container(border=True):
        st.metric(":green[:material/check_circle: READY TASKS]", number_of_ready_tasks)
with metric_col3:
    with st.container(border=True):
        st.metric(":red[:material/running_with_errors: MISSED RUNS]", number_of_missed_runs)
with metric_col4:
    with st.container(border=True):
        st.metric(":orange[:material/do_not_disturb: DISABLED TASKS]", number_of_disabled_tasks)



(st.session_state.tasks_df
    .tasklit_taskframe(
        author=author_filter,
        folder_name=folder_select
    )
)

st.divider()
