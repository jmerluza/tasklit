import streamlit as st
import polars as pl
from tasklit.functions.functions import connect_to_task_scheduler, get_tasks_by_folder
from tasklit.components.folders_pane import get_folders_pane
from tasklit.components.actions_pane import get_folder_actions, get_task_actions

st.set_page_config(page_title="TaskLit", layout="wide")
st.title(":clock2: TaskLit")

if "scheduler_client" not in st.session_state:
    st.session_state.scheduler_client = connect_to_task_scheduler()

scheduler = st.session_state.scheduler_client
folders_pane_df = get_folders_pane()

folder_pane, tasks_pane, actions_pane = st.columns([0.15,0.65,0.10])
with folder_pane:
    st.header("Select Folder", divider="green")
    folder_select = st.dataframe(
        folders_pane_df,
        hide_index=True,
        use_container_width=True,
        selection_mode="single-row",
        on_select="rerun"
    )

    try:
        folder_name = folders_pane_df.item(
            row=folder_select.get("selection").get("rows")[0],
            column=0
        )
    except IndexError:
        folder_name = "\\"

with tasks_pane:
    st.header(f":file_folder: {folder_name}", divider="blue")
    task_pane_df = get_tasks_by_folder(folder_name)
    task_select = st.dataframe(
        task_pane_df, hide_index=True,
        use_container_width=True,
        selection_mode="single-row",
        on_select="rerun"
    )

with actions_pane:
    st.header("Actions", divider="grey")
    st.write(f"_{folder_name} actions_")
    get_folder_actions()

    st.write(f"_Selected task actions_")
    get_task_actions()

    

# st.subheader("Folder statistics", divider="red")
# with st.container(border=True):
#     stat_col1, stat_col2, stat_col3, stat_col4= st.columns([0.2,0.2,0.2,0.4])
#     with stat_col1:
#         st.write(f"Total number of tasks: {task_pane_df.total_task_count()}")
#         st.write(f"Total number of missed runs: {task_pane_df.total_missed_runs()}")
#     with stat_col2:
#         st.dataframe(task_pane_df.task_results(), hide_index=True, use_container_width=True)
#     with stat_col3:
#         st.dataframe(task_pane_df.task_states(), hide_index=True, use_container_width=True)
#     with stat_col4:
#         st.dataframe(task_pane_df.task_by_author(), hide_index=True, use_container_width=True)

