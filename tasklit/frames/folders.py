import polars as pl
import streamlit as st
from tasklit.functions.functions import connect_to_task_scheduler

def get_folders() -> pl.DataFrame:
    """Returns the root and it subfolders as a dataframe."""
    scheduler = connect_to_task_scheduler()
    root_folder = scheduler.GetFolder("\\")
    folders = ["\\"] + [folder.Name for folder in root_folder.GetFolders(0)]
    df = pl.DataFrame({"Folders":folders})
    return FoldersFrame(df)

class FoldersFrame(pl.DataFrame):
    """The folders data frame."""
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def tasklit_folderframe(self):
        """Changes the folder frame to a streamlit dataframe to output to the app."""
        df = st.dataframe(
            self.df,
            hide_index=True,
            use_container_width=True,
            selection_mode="single-row",
            on_select="ignore"
        )
        return df
