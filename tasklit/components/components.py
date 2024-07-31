import os
import streamlit as st
import win32com
from datetime import datetime, timedelta

@st.dialog("Create a Basic Task")
def create_task(
    scheduler_client,
    folder: str,
    description: str|None=""):

    # Create a new task definition
    task_definition = scheduler_client.NewTask(0)

    # Set trigger (daily trigger)
    trigger = task_definition.Triggers.Create(win32com.client.constants.TASK_TRIGGER_DAILY)
    trigger.StartBoundary = (datetime.now() + timedelta(minutes=1)).isoformat() #starts at 1 minute from now
    trigger.DaysInterval = 1

    # Set action (run a batch file)
    action = task_definition.Actions.Create(0)
    action.Path = "\\SWPWHQFNPA01\Finance\BI_REPORT\ZBI_DataLibrary\Python\JalenWIP\_Task_Scheduler_Scripts\Motivate\motivate_me.bat"  # Change to the path of your batch file