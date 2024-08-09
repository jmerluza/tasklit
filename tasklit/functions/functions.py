import polars as pl
import streamlit as st
import pythoncom
import win32com.client
from tasklit.classes import TaskData
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
        

def get_tasks_by_folder(folder_name: str | None = "\\") -> TaskData:
    # Connect to Task Scheduler
    scheduler = connect_to_task_scheduler()
    folder = scheduler.GetFolder(folder_name)

    tasks = {}
    tasks["author"] = [task.Definition.RegistrationInfo.Author for task in folder.GetTasks(0)]
    tasks["name"] = [task.Name for task in folder.GetTasks(0)]
    tasks["state"] = [task.State for task in folder.GetTasks(0)]
    tasks["next_run_time"] = [task.NextRunTime for task in folder.GetTasks(0)]
    tasks["last_run_time"] = [task.LastRunTime for task in folder.GetTasks(0)]
    tasks["last_task_result"] = [task.LastTaskResult for task in folder.GetTasks(0)]
    tasks["missed_runs"] = [task.NumberOfMissedRuns for task in folder.GetTasks(0)]

    df = pl.DataFrame(tasks)

    if df.is_empty():
        return TaskData(df)
    else:
        df = (pl.DataFrame(tasks)
            .with_columns(
                pl.col("state").replace(TASK_STATES).name.keep(),
                pl.col("last_task_result").replace(TASK_RESULTS).name.keep()
            )
        )
        return TaskData(df)
   
