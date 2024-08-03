import os
import tkinter as tk
import streamlit as st
from tkinter import filedialog
from datetime import datetime, timedelta
import pythoncom
import win32com.client
from tasklit.constants import TASK_TRIGGERS, ActionTypes, TaskCreation, TaskLogon

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

    col1, col2 = st.columns(2)
    with col1:
        task_name = st.text_input("Task Name")
        task_description = st.text_input("Task Description")

    with col2:
        folder = st.text_input("Folder Name")
        start_date = st.date_input("Choose a start date", value="today")
        start_time = st.time_input("Choose a start time", value="now")

    task_cadence = st.selectbox("When do you want the task to run?", ("Daily", "Weekly"))

    if folder is None:
        folder = "\\"

    task_folder = scheduler.GetFolder(folder)

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

    # =============================================================================================
    # Task action settings
    # =============================================================================================
    run_file = st.file_uploader("Choose a batch file to run")
    action_arg = ""

    if run_file is None:
        run_file = "cmd.exe"
        action_arg = '/c "exit"'
    
    if st.button("Submit"):
        # create a new task definition
        task_definition = st.session_state["client"].NewTask(0)

        # set up trigger
        trigger = task_definition.Triggers.Create(TASK_TRIGGERS.get(task_cadence))
        trigger.StartBoundary = datetime.combine(start_date, start_time).isoformat()

        match task_cadence:
            case "Daily":
                trigger.DaysInterval = daily_interval
            case "Weekly":
                trigger.WeeksInterval = weekly_interval
                trigger.DaysOfWeek = weekly_dow
        
        # set up actions
        action = task_definition.Actions.Create(ActionTypes.TASK_ACTION_EXEC) # for now this is the default.
        action.Path = run_file
        action.Arguments = action_arg

        # set task information
        task_definition.RegistrationInfo.Description = task_description
        task_definition.Settings.Enabled = True
        task_definition.Settings.StopIfGoingOnBatteries = False

        # Register the task
        task_folder.RegisterTaskDefinition(
            task_name,
            task_definition,
            TaskCreation.TASK_CREATE_OR_UPDATE,
            "", # no user
            "", # no password
            TaskLogon.TASK_LOGON_NONE
        )
        st.rerun()