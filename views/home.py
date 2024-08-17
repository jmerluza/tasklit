import os
import streamlit as st
import polars as pl

number_of_running_tasks = st.session_state.tasks_df.total_number_of_tasks_by_state("RUNNING")
number_of_ready_tasks = st.session_state.tasks_df.total_number_of_tasks_by_state("READY")
number_of_missed_runs = st.session_state.tasks_df.total_number_of_missed_runs()
number_of_disabled_tasks = st.session_state.tasks_df.total_number_of_tasks_by_state("DISABLED")

filter_col1, filter_col2, filter_col3 = st.columns([0.2,0.2,0.6])
with filter_col1:
    author_filter = st.text_input("Task Author", value=os.getlogin())
with filter_col2:
    folder_select = st.selectbox("Select folder", options=st.session_state.folder_options)


metric_col1, metric_col2, metric_col3 = st.columns([0.1,0.1,0.8])
with metric_col1:
    with st.container(border=True):
        st.metric(":blue[:material/sprint: RUNNING TASKS]", number_of_running_tasks)
    with st.container(border=True):
        st.metric(":green[:material/check_circle: READY TASKS]", number_of_ready_tasks)
    
with metric_col2:
    with st.container(border=True):
        st.metric(":red[:material/running_with_errors: MISSED RUNS]", number_of_missed_runs)
    with st.container(border=True):
        st.metric(":orange[:material/do_not_disturb: DISABLED TASKS]", number_of_disabled_tasks)

with metric_col3:
    st.session_state.tasks_df.tasklit_taskframe(folder_name=folder_select)

st.divider()

# task_options = (st.session_state.tasks_df
#     .filter(pl.col("folder_name")==folder_select)
#     ["name"].unique(maintain_order=True).to_list()
# )
# task_select_col1, task_select_col2 = st.columns([0.3,0.7])
# with task_select_col1:
#     task_select = st.selectbox(
#         "Select task",
#         options=task_options)

# table_col1, table_col2 = st.columns([0.3,0.7])

# with table_col1:
#     folder_select = st.selectbox("Select folder", options=st.session_state.folder_options)
#     # st.session_state.tasks_df.group_by_last_run_results()

# with table_col2:
#     st.session_state.tasks_df.tasklit_taskframe()

# folder_pane, tasks_pane, actions_pane = st.columns([0.15,0.65,0.10])

# with folder_pane:
#     st.subheader(":file_folder: Select folder", divider="green")
#     folder_select = st.selectbox(
#         "Select folder",
#         options=st.session_state.folder_df["Folders"].to_list(),
#         label_visibility="collapsed"
#     )
#     st.session_state.folder_df.tasklit_folderframe()

# with tasks_pane:
#     st.subheader(":hourglass_flowing_sand: Select task", divider="blue")

#     task_df = get_tasks(folder_select)

#     folder_select = st.selectbox(
#         "Select task",
#         options=task_df["name"].to_list(),
#         label_visibility="collapsed"
#     )
#     task_select = task_df.tasklit_taskframe()

# with actions_pane:
#     st.subheader(":rocket: Actions", divider="grey")
#     run_task_button = st.button(":material/play_circle: Run task", use_container_width=True)
#     stop_task_button = st.button(":material/stop_circle: End task", use_container_width=True)
