import polars as pl


def get_tasks_by_folder(
    scheduler_client, folder_name: str | None = None
) -> pl.DataFrame:
    if folder_name:
        folder_name = f"\{folder_name}"
    else:
        folder_name = "\\"

    folder = scheduler_client.GetFolder(folder_name)

    df = {}
    df["name"] = [task.Name for task in folder.GetTasks(0)]
    df["description"] = [
        task.Definition.RegistrationInfo.Description for task in folder.GetTasks(0)
    ]
    df["next_run_time"] = [task.NextRunTime for task in folder.GetTasks(0)]
    df["last_run_time"] = [task.LastRunTime for task in folder.GetTasks(0)]
    df["last_task_result"] = [task.LastTaskResult for task in folder.GetTasks(0)]
    df["missed_runs"] = [task.NumberOfMissedRuns for task in folder.GetTasks(0)]
    df["author"] = [
        task.Definition.RegistrationInfo.Author for task in folder.GetTasks(0)
    ]

    return df
