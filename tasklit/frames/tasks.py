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
        self.empty = self.df.is_empty()

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
            selection_mode="single-row",
            on_select="ignore"
        )
        return df

def get_tasks(folder_name: str | None = "\\") -> TaskFrame:
    """Get the tasks from the folder name"""
    scheduler = connect_to_task_scheduler()
    folder = scheduler.GetFolder(folder_name)

    tasks = {}

    tasks["name"] = [task.Name for task in folder.GetTasks(0)]
    tasks["state"] = [task.State for task in folder.GetTasks(0)]
    tasks["next_run_time"] = [task.NextRunTime for task in folder.GetTasks(0)]
    tasks["last_run_time"] = [task.LastRunTime for task in folder.GetTasks(0)]
    tasks["last_task_result"] = [task.LastTaskResult for task in folder.GetTasks(0)]
    tasks["missed_runs"] = [task.NumberOfMissedRuns for task in folder.GetTasks(0)]
    tasks["author"] = [task.Definition.RegistrationInfo.Author for task in folder.GetTasks(0)]
    tasks["created_date"] = [task.Definition.RegistrationInfo.Date for task in folder.GetTasks(0)]
    tasks["description"] = [task.Definition.RegistrationInfo.Description for task in folder.GetTasks(0)]
    tasks["source"] = [task.Definition.RegistrationInfo.Source for task in folder.GetTasks(0)]

    df = pl.DataFrame(tasks)

    if df.is_empty():
        return TaskFrame(df)

    else:
        df = (pl.DataFrame(tasks)
            .with_columns(
                pl.col("state").replace(TASK_STATES).name.keep(),
                pl.col("last_task_result").replace(TASK_RESULTS).name.keep()
            )
        )
        return TaskFrame(df)
