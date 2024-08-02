import os
import streamlit as st
import win32com.client
from datetime import datetime, timedelta

# from tasklit.constants import TriggerCadence


@st.dialog("Create a Basic Task", width="large")
def create_task():
    col1, col2 = st.columns(2)
    with col1:
        task_name = st.text_input("Task Name")
        task_description = st.text_input("Task Description")

    with col2:
        folder = st.text_input("Folder Name")
        start_date = st.date_input("Choose a start date", value="today")
        start_time = st.time_input("Choose a start time", value="now")

    task_cadence = st.selectbox("When do you want the task to run?", ("Daily", "Weekly"))

    # =============================================================================================
    # Daily task settings
    # =============================================================================================
    if task_cadence == "Daily":
        with st.container(border=True):
            daily_interval = st.selectbox(
                "Please enter the daily interval to run the task.",
                (1, 2),
                help="1 will create a schedule to run every day, 2 will run every other day."
            )
    # =============================================================================================
    # Weekly task settings
    # =============================================================================================
    elif task_cadence == "Weekly":
        with st.container(border=True):
            weekly_interval = st.selectbox(
                "Please enter the daily interval to run the task.",
                (1, 2),
                help="1 will create a schedule to run every week, 2 will run every other week.",
            )
            weekly_dow = st.selectbox(
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

    if st.button("Submit"):
        st.rerun()

    # # Create a new task definition
    # task_definition = scheduler_client.NewTask(0)

    # # Set trigger (daily trigger)
    # trigger = create_trigger(task_definition, task_cadence)
    # trigger.StartBoundary = (
    #     datetime.now() + timedelta(minutes=1)
    # ).isoformat()  # starts at 1 minute from now
    # trigger.DaysInterval = 1

    # # Set action (run a batch file)
    # action = task_definition.Actions.Create(0)
    # action.Path = "\\SWPWHQFNPA01\Finance\BI_REPORT\ZBI_DataLibrary\Python\JalenWIP\_Task_Scheduler_Scripts\Motivate\motivate_me.bat"  # Change to the path of your batch file
