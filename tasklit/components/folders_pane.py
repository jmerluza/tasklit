import polars as pl
import streamlit as st
from tasklit.functions.functions import connect_to_task_scheduler

def get_folders_pane() -> pl.DataFrame:
    """Returns all folders in a data frame."""
    scheduler = connect_to_task_scheduler()
    root_folder = scheduler.GetFolder("\\")
    folders = ["\\"] + [folder.Name for folder in root_folder.GetFolders(0)]
    df = pl.DataFrame({"Folders":folders})
    return df