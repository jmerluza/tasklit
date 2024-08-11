import streamlit as st
import polars as pl
from tasklit.frames import get_folders, get_tasks
from tasklit.functions.functions import connect_to_task_scheduler

st.set_page_config(page_title="TaskLit", layout="wide", initial_sidebar_state="expanded")
st.title(":clock2: TaskLit")

if "scheduler_client" not in st.session_state:
    st.session_state.scheduler_client = connect_to_task_scheduler()

scheduler = st.session_state.scheduler_client
folder_pane, tasks_pane, actions_pane = st.columns([0.15,0.65,0.10])

with folder_pane:
    st.subheader(":file_folder: Select folder", divider="green")
    folder_df = get_folders()
    folder_select = st.selectbox(
        "",
        options=folder_df["Folders"].to_list(),
        label_visibility="collapsed"
    )
    folder_df.tasklit_folderframe()

with tasks_pane:
    st.subheader(":hourglass_flowing_sand: Select task", divider="blue")
    task_df = get_tasks(folder_select)
    folder_select = st.selectbox(
        "",
        options=task_df["name"].to_list(),
        label_visibility="collapsed"
    )
    task_select = task_df.tasklit_taskframe()

with actions_pane:
    st.header("Actions", divider="grey")
    st.write("_Selected folder actions_")
    st.button(":file_folder: Manage Folder", use_container_width=True)
    st.write("_Selected task actions_")
    st.button(":fire: Run", use_container_width=True)
    st.button(":black_square_for_stop: End", use_container_width=True)
    st.button(":small_red_triangle_down: Disable", use_container_width=True)
    st.button(":hourglass_flowing_sand: Manage Task", use_container_width=True)
