import streamlit as st
from components.create_page import (
    daily_trigger_component,
    weekly_trigger_component,
    monthly_trigger_component,
    onetime_trigger_component,
    task_action_component,
    task_setting_component
)

st.header(":material/add_circle: Create New Task")
with st.expander("Instructions", icon="ℹ️"):
    st.write(
        """
        1. Select folder.
        2. Create a task name.
        3. Enter task description.
        4. Choose a trigger type.
        5. Choose an action type.
        6. Configure task settings.
        7. Create task.
        """
    )

# =================================================================================================
# Basic task information.
# =================================================================================================
r1c1, r1c2 = st.columns(2)
with r1c1:
    folder_select = st.selectbox("Select Folder", ["\\"] + st.session_state.folders)
with r1c2:
    task_name = st.text_input(label="Task Name")
task_description = st.text_area(label="Task Description", height=25)

# =================================================================================================
# Task trigger.
# =================================================================================================
st.header(":material/joystick: Task Trigger")
with st.container(border=True):
    trigger_type = st.selectbox(
        "Select Trigger",
        options=["daily","weekly","monthly","one-time"],
    )
    match trigger_type:
        case "daily":
            daily_trigger_component()
        case "weekly":
            weekly_trigger_component()
        case "monthly":
            monthly_trigger_component()
        case "ont-time":
            onetime_trigger_component()

# =================================================================================================
# Task action.
# =================================================================================================
st.header(":material/action_key: Task Action")
with st.container(border=True):
    task_action_component()

# =================================================================================================
# Task settings.
# =================================================================================================
st.header(":material/tune: Task Settings")
with st.container(border=True):
    task_setting_component()
# =================================================================================================
# Subnmit button.
# =================================================================================================
st.button(label="Submit")
