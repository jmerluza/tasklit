import streamlit as st
from tasklit.classes.new_task import NewTask

with st.form("create_new_task_form", border=True):
    st.subheader(":material/schedule: Create a new task")
    st.warning(":material/warning: Create new task feature is limited to only creating a basic task that runs a batch file daily or weekly.")

    r1c1, r1c2 = st.columns([0.3,0.7])
    
    with r1c1:
        parent_folder = st.selectbox(
            "Parent folder",
            options=st.session_state.folder_options
        )
    
    with r1c2:
        new_task_name = st.text_input("Task name")

    new_task_description = st.text_input("Task description")

    r2c1, r2c2, r2c3, r2c4 = st.columns([0.15,0.15,0.35,0.40])

    with r2c1:
        start_date = st.date_input("When should the task start?", value="today")
    with r2c2:
        start_time = st.time_input("What time should the task start?", value="now")

    r3c1, r3c2 = st.columns([0.4,0.6])

    with r3c1:
        task_cadence = st.selectbox("How often will the task run?", ("Daily","Weekly"))
        # =============================================================================================
        # Daily task settings
        # =============================================================================================
        if task_cadence == "Daily":
            with st.container(border=True):
                interval = st.selectbox(
                    "Please enter the daily interval to run the task.",
                    (1, 2),
                    help="1 will create a schedule to run every day, 2 will run every other day."
                )
                dow = None

        # =============================================================================================
        # Weekly task settings
        # =============================================================================================
        elif task_cadence == "Weekly":
            with st.container(border=True):
                interval = st.selectbox(
                    "Please enter the weekly interval to run the task.",
                    (1, 2),
                    help="1 will create a schedule to run every week, 2 will run every other week.",
                )
                dow = st.selectbox(
                    "What day would you like the task to run?",
                    (
                        "Sunday",
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday",
                    ),
                )
    
    # =============================================================================================
    # Task action settings
    # =============================================================================================
    action_file = st.file_uploader("Choose a batch file to run")
    action_arg = ""

    if action_file is None:
        action_file = "cmd.exe"
        action_arg = '/c "exit"'

    # =============================================================================================
    # Submit new task
    # =============================================================================================
    if st.form_submit_button("Create new task"):
        ntask = NewTask(st.session_state.scheduler_client)

        # create a new task definition
        task_definition = ntask.create_task_definition()

        # set up trigger
        trigger = ntask.create_task_trigger(
            task_definition,
            task_cadence,
            start_date,
            start_time,
            interval,
            dow
        )

        # set up actions
        action = ntask.create_task_action(
            task_definition,
            action_file,
            action_arg)

        # set task information
        task_definition = ntask.create_task_information(
            task_definition,
            new_task_description)

        # Register the task
        ntask.create_new_task(
            task_definition,
            parent_folder,
            new_task_name
        )
        st.rerun()