import streamlit as st
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
if "folder_options" not in st.session_state:
    st.session_state.folder_options = st.session_state.tasks_df["folder_name"].unique(maintain_order=True).to_list()

scheduler = st.session_state.scheduler_client

home_page = st.Page("views/home.py", title="Home page", icon=":material/home:")
# create_task_page = st.Page("views/create_task.py", title="Create task", icon=":material/schedule:")
# manage_task_page = st.Page("views/manage_task.py", title="Manage task", icon=":material/more_time:")
# manage_folder_page = st.Page("views/manage_folder.py", title="Manage folder", icon=":material/folder_open:")

nav = st.navigation(
    {
        "Home": [home_page],
        # "Folder Actions": [manage_folder_page],
        # "Task Actions": [create_task_page, manage_task_page]
    }
)

nav.run()