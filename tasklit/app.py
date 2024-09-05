import streamlit as st
from pytask_scheduler import TaskScheduler, get_task_scheduler_history
from frames.frames import TasksDataFrame

st.set_page_config(page_title="TaskLit", layout="centered", initial_sidebar_state="expanded")
st.title(":orange[:material/local_fire_department:] :red[TaskLit]")
# =================================================================================================
# Initializations
# =================================================================================================
# initialize task scheduler object.
if "ts_object" not in st.session_state:
    st.session_state.ts_object = TaskScheduler()
# initialize task data frame.
if "task_data" not in st.session_state:
    st.session_state.task_data = TasksDataFrame(st.session_state.ts_object.get_all_tasks()).preprocess()
# initialize lists
if "folders" not in st.session_state:
    st.session_state.folders = st.session_state.ts_object.folders
# initialize task data frame for todays tasks.
if "today_tasks" not in st.session_state:
    st.session_state.today_tasks = st.session_state.task_data.get_tasks_scheduled_by_date()

if "task_history" not in st.session_state:
        st.session_state.task_history = get_task_scheduler_history()

# ===================================================
# New Task
# ===================================================
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

home_page = st.Page("home.py", title="Home", icon=":material/home:")
create_page = st.Page("create.py", title="Create New Task", icon=":material/add_circle:")
view_task_page = st.Page("task_view.py", title="View Task", icon=":material/view_day:")

pg = st.navigation([home_page, create_page, view_task_page])
pg.run()