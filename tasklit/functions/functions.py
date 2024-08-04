import polars as pl
import streamlit as st
import pythoncom
import win32com.client
from tasklit.classes import TaskData

def check_folder_exists(folder_name: str):
    # Connect to Task Scheduler
    pythoncom.CoInitialize()
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    if folder_name == "\\":
        return True
    else:
        root_folder = scheduler.GetFolder("\\")
        if folder_name in [f.Name for f in root_folder.GetFolders(0)]:
            return True
        else:
            return False
        

def get_tasks_by_folder(folder_name: str | None = "\\") -> TaskData:
    # Connect to Task Scheduler
    pythoncom.CoInitialize()
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    folder = scheduler.GetFolder(folder_name)

    tasks = {}
    tasks["name"] = [task.Name for task in folder.GetTasks(0)]
    tasks["state"] = [task.State for task in folder.GetTasks(0)]
    tasks["next_run_time"] = [task.NextRunTime for task in folder.GetTasks(0)]
    tasks["last_run_time"] = [task.LastRunTime for task in folder.GetTasks(0)]
    tasks["last_task_result"] = [task.LastTaskResult for task in folder.GetTasks(0)]
    tasks["missed_runs"] = [task.NumberOfMissedRuns for task in folder.GetTasks(0)]
    tasks["author"] = [
        task.Definition.RegistrationInfo.Author for task in folder.GetTasks(0)
    ]
    df = pl.DataFrame(tasks)
    return TaskData(df)
   
