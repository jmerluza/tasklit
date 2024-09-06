"""TaskLit app initialization."""

import streamlit as st
from initializations import initialize_app_objects, initialize_new_task_variables
st.set_page_config(page_title="TaskLit", layout="centered", initial_sidebar_state="expanded")
st.title(":orange[:material/local_fire_department:] :red[TaskLit]")
# =================================================================================================
# Initializations
# =================================================================================================
initialize_app_objects()
initialize_new_task_variables()

home_page = st.Page("home.py", title="Home", icon=":material/home:")
create_page = st.Page("create.py", title="Create New Task", icon=":material/add_circle:")
view_task_page = st.Page("task_view.py", title="View Task", icon=":material/view_day:")

pg = st.navigation([home_page, create_page, view_task_page])
pg.run()