import polars as pl
import streamlit as st
from tasklit.constants import TASK_STATES, TASK_RESULTS
from tasklit.functions.functions import connect_to_task_scheduler

def show_task_actions():
    with st.session_state.actions_pane:
        st.button(":hourglass_flowing_sand: Manage Task", use_container_width=True)

class TaskFrame(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def total_number_of_tasks(self):
        """Counts the total number of tasks."""
        return self.df.shape[0]

    def total_number_of_missed_runs(self):
        """Counts the total number of missed runs."""
        return self.df["missed_runs"].sum()
    
    def total_number_of_tasks_by_state(self, state: str):
        """Counts the total number of tasks by state."""
        return self.df.filter(pl.col("state")==state).shape[0]
    
    def group_by_last_run_results(self):
        """The number of tasks by last results."""
        res = (self.df
            .group_by("last_task_result")
            .agg(pl.col("name").count().alias("Number of tasks").cast(pl.Int64))
            .sort("Number of tasks", descending=True)
        )
        df = st.dataframe(
            res,
            hide_index=True,
            use_container_width=True,
        )
        return df

    def tasklit_taskframe(self):
        """Changes the task frame to a streamlit data frame to display on the app."""
        select_cols = [
            "name",
            "state",
            "next_run_time",
            "last_run_time",
            "last_task_result",
            "missed_runs"
        ]
        rename_cols = [
            "Name",
            "Status",
            "Next Run Time",
            "Last Run Time",
            "Last Run Results",
            "Missed Runs"
        ]

        df = st.dataframe(
            (self.df
                .select(select_cols)
                .rename(dict(zip(select_cols, rename_cols)))
            ),
            hide_index=True,
            use_container_width=True,
        )
        return df
    
def list_scheduled_tasks_in_folder(folder, folder_name, tasks_list):
    tasks = folder.GetTasks(0)
    for i in range(tasks.Count):
        task = tasks.Item(i + 1)
        tasks_list.append({
            "folder_name": folder_name,
            "name": task.Name,
            "state": task.State,
            "next_run_time": task.NextRunTime,
            "last_run_time": task.LastRunTime,
            "last_task_result": task.LastTaskResult,
            "missed_runs": task.NumberOfMissedRuns,
            "author": task.Definition.RegistrationInfo.Author,
            "created_date": task.Definition.RegistrationInfo.Date,
            "description": task.Definition.RegistrationInfo.Description,
            "path": task.Path,
            "source": task.Definition.RegistrationInfo.Source
        })

    # Recursively list tasks in subfolders
    subfolders = folder.GetFolders(0)
    for i in range(subfolders.Count):
        subfolder = subfolders.Item(i + 1)
        list_scheduled_tasks_in_folder(subfolder, folder_name + "\\" + subfolder.Name, tasks_list)

def get_all_scheduled_tasks():
    scheduler = connect_to_task_scheduler()
    root_folder = scheduler.GetFolder("\\")
    tasks_list = []
    list_scheduled_tasks_in_folder(root_folder, "\\", tasks_list)
    return tasks_list

def get_tasks() -> TaskFrame:
    """Get the tasks from the folder name"""
    tasks_list = get_all_scheduled_tasks()
    df = pl.DataFrame(tasks_list)

    if df.is_empty():
        return TaskFrame(df)

    else:
        df = (pl.DataFrame(tasks_list)
            .with_columns(
                pl.col("state").replace(TASK_STATES).name.keep(),
                pl.col("last_task_result").replace(TASK_RESULTS).name.keep()
            )
        )
        return TaskFrame(df)
