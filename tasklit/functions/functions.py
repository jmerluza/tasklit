import polars as pl
import streamlit as st
import pythoncom
import win32com.client
from tasklit.constants import TASK_STATES, TASK_RESULTS

def connect_to_task_scheduler():
    # Connect to Task Scheduler
    pythoncom.CoInitialize()
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    return scheduler
    

def check_folder_exists(folder_name: str):
    # Connect to Task Scheduler
    scheduler = connect_to_task_scheduler()
    if folder_name == "\\":
        return True
    else:
        root_folder = scheduler.GetFolder("\\")
        if folder_name in [f.Name for f in root_folder.GetFolders(0)]:
            return True
        else:
            return False
        
def get_task_definition(folder_name: str, task_name: str):
    """Get task definition by task name.
    
    Parameters:
        folder_name (`str`): Folder name.
        task_name (`str`): Name of task within the folder.
    """
    folder = st.session_state.scheduler_client.GetFolder(folder_name)
    task = folder.GetTask(task_name)
    task_definition = task.Definition
    return task_definition

def create_task_definition():
    """Create a new task definition. Used for creating a new task."""
    task_definition = st.session_state.scheduler_client.NewTask(0)
    return task_definition
    
