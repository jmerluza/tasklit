import streamlit as st
from pytask_scheduler import TaskScheduler
from frames.tasks_dataframe import TasksDataFrame

st.set_page_config(page_title="TaskLit", layout="centered", initial_sidebar_state="expanded")
st.title(":orange[:material/local_fire_department:] :red[TaskLit]")
st.divider()

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

home_page = st.Page("home.py", title="Home", icon=":material/home:")
create_page = st.Page("create.py", title="Create New Task", icon=":material/add_circle:")
view_task_page = st.Page("task_view.py", title="View Task", icon=":material/view_day:")

pg = st.navigation([home_page, create_page, view_task_page])
pg.run()