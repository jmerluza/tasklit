import os
import streamlit as st
import polars as pl
from pytask_scheduler import TaskScheduler
from tasklit.frames.tasks_dataframe import TasksDataFrame
from datetime import datetime

st.set_page_config(page_title="TaskLit", layout="wide", initial_sidebar_state="expanded")
st.title(":orange[:material/local_fire_department:] :red[TaskLit]")
st.divider()

st.header("Tasks Scheduled Today")

st.markdown("""
<style>
.big-font {
    font-size:20px;
}
</style>
""", unsafe_allow_html=True)

# =================================================================================================
# Initializations
# =================================================================================================

# initialize task scheduler object.
if "ts_object" not in st.session_state:
    st.session_state.ts_object = TaskScheduler()

# initialize task data frame.
if "task_data" not in st.session_state:
    st.session_state.task_data = TasksDataFrame(st.session_state.ts_object.get_all_tasks()).preprocess()

if "today_tasks" not in st.session_state:
    st.session_state.today_tasks = st.session_state.task_data.get_tasks_scheduled_by_date()

# =================================================================================================
# Total Metrics
# =================================================================================================

metric_col1, metric_col2, metric_col3, metric_col4, metric_col5, metric_col6 = st.columns([0.10,0.10,0.10,0.10,0.10, 0.5])
with metric_col1:
    with st.container(border=True):
        st.write(":green[:material/check_circle: READY]")
        st.metric(
            "TASKS READY",
            st.session_state.today_tasks.count_task_by_state(3),
            label_visibility="collapsed"
        )

with metric_col2:
    with st.container(border=True):
        st.write(":blue[:material/run_circle: RUNNING]")
        st.metric(
            "TASKS RUNNING",
            st.session_state.today_tasks.count_task_by_state(4),
            label_visibility="collapsed"
        )

with metric_col3:
    with st.container(border=True):
        st.write(":orange[:material/do_not_disturb: DISABLED]")
        st.metric(
            "TASKS DISABLED",
            st.session_state.today_tasks.count_task_by_state(1),
            label_visibility="collapsed"
        )

with metric_col4:
    with st.container(border=True):
        st.write(":orange[:material/playlist_add_check_circle: QUEUED]")
        st.metric(
            "TASKS QUEUED",
            st.session_state.today_tasks.count_task_by_state(2),
            label_visibility="collapsed"
        )

with metric_col5:
    with st.container(border=True):
        st.write(":red[:material/report: MISSED RUNS]")
        st.metric(
            "TASKS MISSED RUNS",
            st.session_state.today_tasks["number_of_missed_runs"].sum(),
            label_visibility="collapsed"
        )
task_results = (st.session_state.today_tasks
    .group_by("last_task_result_definition")
    .agg(pl.col("name").count())
    .rename({
        "name":"NUMBER OF TASKS",
        "last_task_result_definition":"LAST TASK RESULT"
    })      
)

task_list = (st.session_state.today_tasks
    .select(
        "name",
        "task_state_definition",
        "next_run_time",
        "last_run_time",
        "last_task_result_definition"
    )
    .rename({
        "name":"NAME",
        "task_state_definition":"STATE",
        "next_run_time":"NEXT RUN TIME",
        "last_run_time":"LAST RUN TIME",
        "last_task_result_definition":"LAST TASK RESULT"
    })
)
today_col1, today_col2 = st.columns([0.21,0.79])
with today_col1:
    st.dataframe(task_results, hide_index=True)
with today_col2:
    st.dataframe(task_list, hide_index=True)
