import streamlit as st
import tkinter as tk
from tkinter import filedialog
from pytask_scheduler.constants import TaskTriggerTypes, MonthlyTriggerValues

def start_date_time():
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.ntask_start_date = st.date_input("Select Start Date")
    with col2:
        st.session_state.ntask_start_time = st.time_input("Select Start Time")

def dow():
    st.subheader("_**Days of Week**_")
    st.write("_The Day of week sets the day on which the task will run. For example, \
             the task will run on Sundays every week._")
    all_dow = st.checkbox("Select all weeks")
    col1, col2, col3 = st.columns(3)
    with col1:
        sun = st.checkbox(label="Sunday")
        wed = st.checkbox(label="Wednesday")
        sat = st.checkbox(label="Saturday")
    with col2:
        mon = st.checkbox(label="Monday")
        thu = st.checkbox(label="Thursday")
    with col3:
        tue = st.checkbox(label="Tuesday")
        fri = st.checkbox(label="Friday")
    
    if all_dow:
        weeks = [True] * 7
    else:
        weeks = [sun, wed, sat, mon, thu, tue, fri]
    checked_schema = dict(
        zip(
            MonthlyTriggerValues.DAYS_OF_WEEK.values(),
            weeks
        )
    )
    st.session_state.ntask_dow = [x for x in checked_schema if checked_schema.get(x)]

def dom():
    st.subheader("_**Days of Month**_")
    all_dom = st.checkbox("Select all days")
    col1, col2, col3 = st.columns(3)
    with col1:
        one = st.checkbox("1")
        four = st.checkbox("4")
        seven = st.checkbox("7")
        ten = st.checkbox("10")
        thirteen = st.checkbox("13")
        sixteen = st.checkbox("16")
        nineteen = st.checkbox("19")
        twentytwo = st.checkbox("22")
        twentyfive = st.checkbox("25")
        twentyeight = st.checkbox("28")
        thirtyone = st.checkbox("31")

    with col2:
        two = st.checkbox("2")
        five = st.checkbox("5")
        eight = st.checkbox("8")
        eleven = st.checkbox("11")
        fourteen = st.checkbox("14")
        seventeen = st.checkbox("17")
        twenty = st.checkbox("20")
        twentythree = st.checkbox("23")
        twentysix = st.checkbox("26")
        twentynine = st.checkbox("29")
        last_day = st.checkbox("Last day")

    with col3:
        three = st.checkbox("3")
        six = st.checkbox("6")
        nine = st.checkbox("9")
        twelve = st.checkbox("12")
        fifteen = st.checkbox("15")
        eighteen = st.checkbox("18")
        twentyone = st.checkbox("21")
        twentyfour = st.checkbox("24")
        twentyseven = st.checkbox("27")
        thirty = st.checkbox("30")

    if all_dom:
        days = [True] * 32
    else:
        days = [
            one,
            two,
            three,
            four,
            five,
            six,
            seven,
            eight,
            nine,
            ten,
            eleven,
            twelve,
            thirteen,
            fourteen,
            fifteen,
            sixteen,
            seventeen,
            eighteen,
            nineteen,
            twenty,
            twentyone,
            twentytwo,
            twentythree,
            twentyfour,
            twentyfive,
            twentysix,
            twentyseven,
            twentyeight,
            twentynine,
            thirty,
            thirtyone,
            last_day
        ]

    checked_schema = dict(
        zip(
            MonthlyTriggerValues.DAYS_OF_MONTH.values(),
            days
        )
    )

    st.session_state.ntask_dom = [x for x in checked_schema if checked_schema.get(x)]

def moy():
    st.subheader("_**Months of Year**_")
    all_moy = st.checkbox("Select all months")
    col1, col2, col3 = st.columns(3)
    with col1:
        jan = st.checkbox("January")
        apr = st.checkbox("April")
        jul = st.checkbox("July")
        octo = st.checkbox("October")

    with col2:
        feb = st.checkbox("February")
        may = st.checkbox("May")
        aug = st.checkbox("August")
        nov = st.checkbox("November")

    with col3:
        mar = st.checkbox("March")
        jun = st.checkbox("June")
        sep = st.checkbox("September")
        dec = st.checkbox("December")

    if all_moy:
        months = [True] * 12
    else:
        months = [
            jan,
            feb,
            mar,
            apr,
            may,
            jun,
            jul,
            aug,
            sep,
            octo,
            nov,
            dec
        ]
    
    checks_schema = dict(
        zip(
            MonthlyTriggerValues.MONTHS_OF_YEAR.values(),
            months
        )
    )

    st.session_state.ntask_moy = [x for x in checks_schema if checks_schema.get(x)]

def wom():
    st.session_state.ntask_wom = st.selectbox(
        "Select Week of Month",
        options=MonthlyTriggerValues.WEEKS_OF_MONTH.keys()
    )

def daily_trigger_fields():
    st.subheader("_Daily Task_")
    st.write("_This task will run on a daily schedule._")
    start_date_time()
    st.session_state.ntask_days_interval = st.number_input(
        label="Days Interval",
        min_value=1,
        max_value=6,
        step=1)
    st.write("_The days interval sets the number of days \
            in between the scheduled run. For example, an interval 1 will run the task every day, \
            an interval of 2 will run the task every other day._")
    
def weekly_trigger_fields():
    st.subheader("_Weekly Task_")
    st.write("_This task will run on a weekly schedule._")
    start_date_time()

    # Week interval
    st.session_state.ntask_weeks_interval = st.number_input(
        label="Weeks Interval",
        min_value=1,
        max_value=2,
        step=1
    )
    st.write("_The Weeks Interval sets the number of weeks in between the scheduled run. \
             For example, an interval of 1 will run the task every week, an interval of 2 \
             will run the task every other week._")
    
    # Day of week
    dow()
    
    
def monthly_trigger_fields():
    st.subheader("_Monthly Task_")
    st.write("_This task will run on a monthly schedule or a monthly day-of-week schedule._")
    start_date_time()

    monthly_trigger_type = st.selectbox("Select Type", options=["month","dow"])

    match monthly_trigger_type:
        case "month":
            st.write("_This trigger type can start a task on a specific day on specific months._")
            moy()
            dom()
            
        case "dow":
            st.write("_This trigger type can start a task every first thursday of specific months._")
            moy()
            dow()
            wom()

def onetime_trigger_fields():
    st.subheader("_One-time Task_")
    st.write("_This task will run once on a specified date and time._")
    start_date_time()

def file_picker() -> str:
    root = tk.Tk()
    fpath = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("Batch files", "*.bat"),
            ("All files", "*.*")
        ]
    )
    root.withdraw()
    return fpath

def task_action_fields():
    st.write("_:material/warning: Only support for creating an execution action that \
             runs a batch file._")
    

st.header(":material/add_circle: Create New Task")
with st.expander("Instructions"):
    st.write(
        """
        1. Select a folder for the new task to be in.
        2. Create a name for the task.
        3. Enter task description.
        4. Choose a trigger type.
        5. Choose an action type. (only execution of a batch file is currently implemented.)
        6. Configure task settings.
        7. Click create.
        """
    )

r1c1, r1c2 = st.columns(2)

with r1c1:
    folder_select = st.selectbox("Select Folder", ["\\"] + st.session_state.folders)
with r1c2:
    task_name = st.text_input(label="Task Name")

task_description = st.text_area(label="Task Description", height=25)

st.header(":material/joystick: Task Trigger")
with st.container(border=True):
    trigger_type = st.selectbox(
        "Select Trigger",
        options=["daily","weekly","monthly","one-time"],
    )
    match trigger_type:
        case "daily":
            daily_trigger_fields()
        case "weekly":
            weekly_trigger_fields()
        case "monthly":
            monthly_trigger_fields()
        case "ont-time":
            onetime_trigger_fields()

st.header(":material/action_key: Task Action")
with st.container(border=True):
    task_action_fields()