import polars as pl
import streamlit as st
from tasklit.classes.folder_manager import FolderManager

st.warning(":material/warning: Delete folder feature not implemented.")
col1, col2, col3, col4, col5 = st.columns([0.1,0.1,0.3,0.3,0.2])
with col1:
    create_folder = st.button("Create Folder")
with col2:
    delete_folder = st.button("Delete Folder")

if create_folder:
    with st.form("create_new_folder_form", border=True):
        st.subheader(":file_folder: Create New Folder")
        new_folder_col1, new_folder_col2 = st.columns([0.2,0.8])
        
        with new_folder_col1:
            parent_folder = st.selectbox(
                "Select parent folder",
                options=st.session_state.folder_options
            )
        with new_folder_col2:
            new_folder_name = st.text_input("Enter new folder name")
        
        if st.form_submit_button("Create new folder"):
            folder = FolderManager(st.session_state.scheduler_client)
            folder.create_folder(new_folder_name, parent_folder)
