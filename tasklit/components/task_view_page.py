import streamlit as st
from pytask_scheduler import (
    get_task_scheduler_history,
    TaskRestartIntervals,
    TaskExecutionLimit,
    TaskInstancePolicy
)

def view_task_component():
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        folder_select = st.selectbox("Select Folder", st.session_state.folders)
    with r1c2:
        tasks = st.session_state.ts_object.get_folder(folder_select).tasks
        task_select = st.selectbox("Select Task", tasks)

    task_info_schema = st.session_state.ts_object.get_folder(folder_select).get_task(task_select).info()
    
    general_tab, triggers_tab, actions_tab, settings_tab, history_tab = st.tabs([
        "General",
        "Triggers",
        "Actions",
        "Settings",
        "History"
    ])

    with general_tab:
        col1 = st.columns(1)
        with col1:
            st.text_input("Name", task_info_schema.get("name"), disabled=True)
            st.text_input("Location", task_info_schema.get("task_path"), disabled=True)
            st.text_input("Author", task_info_schema.get("author"), disabled=True)
            st.text_area("Description", task_info_schema.get("task_description"), height=25, disabled=True)
    
    with triggers_tab:
        st.write("""
        _:material/warning: Triggers information is not available at this time. \
        The Task Scheduler scripting API does not easily provide access to this information. \
        The best way to get to this information is through the xml text of the registered task \
        but each trigger shows up differently in the xml._
        """)
    
    with actions_tab:
        st.subheader("_Starts a program_")
        st.text_input("Execution File Path", task_info_schema.get("execution_path"), disabled=True)

    with settings_tab:
        st.checkbox("Allow task to be run on demand", task_info_schema.get("AllowDemandStart"), disabled=True)
        st.checkbox("Run task as soon as possible after a scheduled start is missed", task_info_schema.get("StartWhenAvailable"), disabled=True)
        st.text_input(
            "If the task fails, restart every:",
            TaskRestartIntervals.intervals.get(task_info_schema.get("RestartInterval")),
            disabled=True
        )
        st.text_input(
            "Attempt to restart up to:",
            task_info_schema.get("RestartCount"),
            disabled=True
        )
        st.text_input(
            "Stop the task if it runs longer than:",
            TaskExecutionLimit.limits.get(task_info_schema.get("ExecutionTimeLimit")),
            disabled=True
        )
        st.write(f"If the task is already running, then the following rule applies: \
                 {TaskInstancePolicy.definitions.get('MultipleInstances')}")
    
    with history_tab:
        pass

def task_history():
    if "task_history" not in st.session_state:
        st.session_state.task_history = get_task_scheduler_history()
