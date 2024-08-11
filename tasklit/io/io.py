import streamlit as st

def tasklit_manage_folder():
    bt = st.button(":file_folder: Manage Folder", use_container_width=True)
    return bt

def tasklit_run():
    bt = st.button(":fire: Run", use_container_width=True)
    return bt

def tasklit_end():
    bt = st.button(":black_square_for_stop: End", use_container_width=True)
    return bt

def tasklit_disable():
    bt = st.button(":small_red_triangle_down: Disable", use_container_width=True)
    return bt

def tasklit_manage_task():
    bt = st.button(":hourglass_flowing_sand: Manage Task", use_container_width=True)
    return bt