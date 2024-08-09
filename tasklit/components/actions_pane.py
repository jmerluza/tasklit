import streamlit as st

def get_folder_actions():
    folder_actions_container = st.container(border=True)
    folder_actions_container.button(":alarm_clock: Create Basic Task", use_container_width=True)
    folder_actions_container.button(":hourglass_flowing_sand: Create Task", use_container_width=True)
    folder_actions_container.button(":bookmark_tabs: Import Task", use_container_width=True)
    folder_actions_container.button(":floppy_disk: Display All Running Task", use_container_width=True)
    folder_actions_container.button(":file_folder: New Folder", use_container_width=True)
    folder_actions_container.button(":x: Delete Folder", use_container_width=True)
    return folder_actions_container

def get_task_actions():
    task_actions_container = st.container(border=True)
    task_actions_container.button(":fire: Run", use_container_width=True)
    task_actions_container.button(":black_square_for_stop: End", use_container_width=True)
    task_actions_container.button(":small_red_triangle_down: Disable", use_container_width=True)
    task_actions_container.button(":page_with_curl: Export", use_container_width=True)
    task_actions_container.button(":x: Delete", use_container_width=True)