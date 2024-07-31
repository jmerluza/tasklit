import polars as pl
import streamlit as st
from tasklit.classes import TaskData

def get_tasks_by_folder(
    scheduler_client, folder_name: str | None = None
) -> pl.DataFrame:
    if folder_name:
        folder_name = f"\{folder_name}"
    else:
        folder_name = "\\"

    folder = scheduler_client.GetFolder(folder_name)

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
