import os
import streamlit as st
import polars as pl
from tasklit.functions.functions import connect_to_task_scheduler
from tasklit.frames import get_tasks
from tasklit.classes.definition import TaskDefinition
from tasklit.classes.task_settings import TaskSettings
from tasklit.classes.task import ExistingTask
from tasklit.constants import TASK_INSTANCES_POLICY, TASK_RESTART_INTERVALS, TASK_EXECUTION_LIMIT

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

task_df = st.session_state.tasks_df.filter_author_and_task_name(
    author=author_filter,
    folder_name=folder_select
)

task_select = (task_df.tasklit_taskframe()).get("selection").get("rows")

st.divider()


if task_select:
    task_name_selected = task_df["name"].unique(maintain_order=True).to_list()[task_select[0]]
    taskdef = TaskDefinition(st.session_state.scheduler_client).get_task_definition(folder_select, task_name_selected)
    task_settings = TaskSettings(taskdef).get_task_settings()

    allow_demand_start_setting = task_settings.get("AllowDemandStart")
    start_when_available_setting = task_settings.get("StartWhenAvailable")
    enabled_setting = task_settings.get("Enabled")
    hidden_setting = task_settings.get("Hidden")
    restart_interval_setting = task_settings.get("RestartInterval")
    restart_count_setting = task_settings.get("RestartCount")
    execution_time_limit_setting = task_settings.get("ExecutionTimeLimit")
    multiple_instances_setting = task_settings.get("MultipleInstances")

    with st.container(border=True):
        general_tab, settings_tab = st.tabs(["General","Settings"])
        with settings_tab:
            st.write("_Specify additional settings that affect the behavior of the task._")
            settings_col1, settings_col2, settings_col3, settings_col4 = st.columns([0.3,0.1,0.3,0.4])

            with settings_col1:
                allow_demand_start = st.checkbox("Allow task to be run on demand.", value=allow_demand_start_setting)
                start_when_available = st.checkbox("Run task as soon as possible after a scheduled start is missed.", value=start_when_available_setting)
                st.write("If the task is already running, then the following rule applies when running another instance of the task:")
                multiple_instances = st.selectbox("Multiple Instances Setting", options=TASK_INSTANCES_POLICY.keys(), label_visibility="collapsed")

            with settings_col3:
                st.write("If the task fails, restart every:")
                restart_interval = st.selectbox("Restart Interval Setting", options=TASK_RESTART_INTERVALS.keys(), label_visibility="collapsed")
                st.write("Number of attempts to restart:")
                restart_count = st.number_input("Restart Count Setting", min_value=0, max_value=5, value=restart_count_setting, label_visibility="collapsed")
                st.write("Stop the task if it runs longer than:")
                execution_time_limit = st.selectbox("Execution Time Limit", options=TASK_EXECUTION_LIMIT.keys(), label_visibility="collapsed")


# else:
#     st.write("No task selected")



        

