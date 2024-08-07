"""Component to manage folders in task scheduler"""

import streamlit as st
import pythoncom
import win32com.client

@st.dialog("Manage Folders", width="large")
def manage_folders():
    # Connect to Task Scheduler
    pythoncom.CoInitialize()
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    st.write("_Create and delete folders._")

    create_tab, delete_tab = st.tabs(["Create folder", "Delete folder"])
    
        


