import streamlit as st
import pythoncom
import win32com.client
from tasklit.classes.new_task import NewTask

@st.dialog("Create a Basic Task", width="large")
def create_task():
    # Connect to Task Scheduler
    pythoncom.CoInitialize()
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    st.write("_Create a basic task in task scheduler.\
             Currently this will create a task to execute a batch file.\
             Other actions will be added later on._"
    )

    # =============================================================================================
    # Task parameters
    # =============================================================================================
    col1, col2 = st.columns(2)
    with col1:
        task_name = st.text_input("Task Name")
        task_description = st.text_input("Task Description")

    with col2:
        folder = st.text_input("Folder Name", value="\\")
        start_date = st.date_input("Choose a start date", value="today")
        start_time = st.time_input("Choose a start time", value="now")

    task_cadence = st.selectbox("When do you want the task to run?", ("Daily", "Weekly"))

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
                "Please enter the daily interval to run the task.",
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
    # Submit task
    # =============================================================================================
    if st.button("Submit"):
        ntask = NewTask(scheduler)

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
        action = ntask.create_task_action(task_definition, action_file, action_arg)

        # set task information
        task_definition = ntask.create_task_information(task_definition, task_description)

        # Register the task
        ntask.create_new_task(task_definition,folder,task_name)
        pythoncom.CoUninitialize()
        st.rerun()
        

