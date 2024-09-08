import streamlit as st
import pythoncom
from pytask_scheduler import TaskScheduler, get_task_scheduler_history

def initialize_app_objects():
    """Initializes the application objects that are used throughout the app.
    
    Definitions:
        `ts_object`: The task scheduler object.
        `task_data`: All tasks in a data frame.
        `folders`: List of subfolders from the root folder.
        `today_tasks`: All tasks scheduled or completed on todays date.
        `task_history`: All task history events.
    """
    pythoncom.CoInitialize()
    if "ts_object" not in st.session_state:
        st.session_state.ts_object = TaskScheduler()
    if "task_data" not in st.session_state:
        st.session_state.task_data = st.session_state.ts_object.get_all_tasks().preprocess()
    if "folders" not in st.session_state:
        st.session_state.folders = st.session_state.ts_object.folders
    if "tasks_completed_today" not in st.session_state:
        st.session_state.tasks_completed_today = st.session_state.task_data.get_tasks_completed_today()
    if "task_history" not in st.session_state:
        st.session_state.task_history = get_task_scheduler_history().get_todays_history()

def initialize_new_task_variables():
    """Initializes the variables for creating a new task."""
    if "ntask_start_date" not in st.session_state:
        st.session_state.ntask_start_date = None
    if "ntask_start_time" not in st.session_state:
        st.session_state.ntask_start_time = None
    if "ntask_days_interval" not in st.session_state:
        st.session_state.ntask_days_interval = None
    if "ntask_weeks_interval" not in st.session_state:
        st.session_state.ntask_weeks_interval = None
    if "ntask_dow" not in st.session_state:
        st.session_state.ntask_dow = None
    if "ntask_dom" not in st.session_state:
        st.session_state.ntask_dom = None
    if "ntask_moy" not in st.session_state:
        st.session_state.ntask_moy = None
    if "ntask_wom" not in st.session_state:
        st.session_state.ntask_wom = None
    if "ntask_action_path" not in st.session_state:
        st.session_state.ntask_action_path = None
    if "ntask_allow_demand_start" not in st.session_state:
        st.session_state.ntask_allow_demand_start = False
    if "ntask_start_when_avail" not in st.session_state:
        st.session_state.start_when_avail = False
    if "ntask_enabled" not in st.session_state:
        st.session_state.ntask_enabled = False
    if "ntask_hidden" not in st.session_state:
        st.session_state.ntask_hidden = False
    if "ntask_restart_interval" not in st.session_state:
        st.session_state.ntask_restart_interval = ""
    if "ntask_restart_count" not in st.session_state:
        st.session_state.ntask_restart_count = None
    if "ntask_exec_time_limit" not in st.session_state:
        st.session_state.ntask_exec_time_limit = ""
    if "ntask_muliple_instances" not in st.session_state:
        st.session_state.ntask_multiple_instances = None
