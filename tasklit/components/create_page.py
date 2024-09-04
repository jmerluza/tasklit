"""Components for the create a new task page."""
import os
import streamlit as st
from pytask_scheduler.constants import (
    MonthlyTriggerValues,
    TaskRestartIntervals,
    TaskExecutionLimit,
    TaskInstancePolicy
)

def start_date_time_widget():
    """Start date and time widgets"""
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.ntask_start_date = st.date_input("Select Start Date")
    with col2:
        st.session_state.ntask_start_time = st.time_input("Select Start Time")

def day_of_week_widget():
    """Days of the week widgets."""
    st.subheader("_**Days of Week**_")
    st.write("_The Day of week sets the day on which the task will run. For example, \
             the task will run on Sundays every week._")

    # button for selecting all the week days.
    all_dow = st.checkbox("Select all weekdays")

    # buttons for the days of week.
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

    checked_schema = dict(zip(MonthlyTriggerValues.DAYS_OF_WEEK.values(),weeks))
    st.session_state.ntask_dow = [x for x in checked_schema if checked_schema.get(x)]

def day_of_month_widget():
    """Days of the month widgets."""
    st.subheader("_**Days of Month**_")

    # button for selecting all the days.
    all_dom = st.checkbox("Select all days")

    # buttons for the days of month.
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
        days = [one,two,three,four,five,six,seven,eight,nine,ten,
            eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,
            twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,
            twentyeight,twentynine,thirty,thirtyone,last_day
        ]

    checked_schema = dict(zip(MonthlyTriggerValues.DAYS_OF_MONTH.values(),days))
    st.session_state.ntask_dom = [x for x in checked_schema if checked_schema.get(x)]

def month_of_year_widget():
    """Months of the year widgets."""
    st.subheader("_**Months of Year**_")

    # button for selecting all months of the year.
    all_moy = st.checkbox("Select all months")

    # buttons for the months of year.
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
        months = [jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]

    checks_schema = dict(zip(MonthlyTriggerValues.MONTHS_OF_YEAR.values(),months))
    st.session_state.ntask_moy = [x for x in checks_schema if checks_schema.get(x)]

def week_of_month_widget():
    """Weeks of the month widget."""
    st.session_state.ntask_wom = st.selectbox(
        "Select Week of Month",
        options=MonthlyTriggerValues.WEEKS_OF_MONTH.keys()
    )

def daily_trigger_component():
    """Field components for the daily trigger."""
    st.subheader("_Daily Task_")
    st.write("_This task will run on a daily schedule._")
    start_date_time_widget()
    st.session_state.ntask_days_interval = st.number_input(
        label="Days Interval",
        min_value=1,
        max_value=6,
        step=1
    )
    st.write("_The days interval sets the number of days \
            in between the scheduled run. For example, an interval 1 will run the task every day, \
            an interval of 2 will run the task every other day._")

def weekly_trigger_component():
    """Field components for the weekly trigger."""
    st.subheader("_Weekly Task_")
    st.write("_This task will run on a weekly schedule._")
    start_date_time_widget()

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

    day_of_week_widget()

def monthly_trigger_component():
    """Field components for the monthly trigger."""
    st.subheader("_Monthly Task_")
    st.write("_This task will run on a monthly schedule or a monthly day-of-week schedule._")
    start_date_time_widget()

    monthly_trigger_type = st.selectbox("Select Type", options=["month","dow"])

    match monthly_trigger_type:
        case "month":
            st.write("_This trigger type can start a task \
                     on a specific day on specific months._")
            month_of_year_widget()
            day_of_month_widget()

        case "dow":
            st.write("_This trigger type can start a task every \
                     first thursday of specific months._")
            month_of_year_widget()
            day_of_month_widget()
            week_of_month_widget()

def onetime_trigger_component():
    """Field components for the one-time trigger."""
    st.subheader("_One-time Task_")
    st.write("_This task will run once on a specified date and time._")
    start_date_time_widget()

def task_action_component():
    """Field components for the task actions."""
    st.write("_:material/warning: Only support for creating an execution action that \
             runs a batch file. Currently, the streamlit `file_uploader` widget is limited \
             in what it returns. Please copy the file link to the batch job and paste it in \
             the text field below._")
    st.session_state.ntask_action_path = st.text_input("File Path", value=None)
    if not st.session_state.ntask_action_path is None:
        if not os.path.exists(rf"{st.session_state.ntask_action_path}"):
            raise ValueError("File path does not exist.")

def task_setting_component():
    """Field components for the task settings."""
    st.write(
        """
        |Setting|Description|
        |---|---|
        |Allow Demand Start (`bool`)|Indicate that the task can be started using \
            the run command of the context menu.|
        |Start When Available (`bool`)|Indicates that the task scheduler can \
            start the task at any time after it's scheduled time has passed.|
        |Enabled (`bool`)|Indicates that the task is enabled. The task can be performed \
            only when this setting is true.|
        |Hidden (`bool`)|Indicates that the task will not be visible in the UI, however, \
            admins can override this setting through the use of a master switch that \
            makes all tasks visible in the UI.|
        |Restart Interval (`str`)|Sets the value that specifies how long the task \
            scheduler will attempt to restart the task.|
        |Restart Count (`int`)|Sets the number of times that the task scheduler will attempt \
            to restart the task.|
        |Execution Time Limit (`str`)|Sets the amount of time allowed to complete the task.|
        |Multiple Instances (`int`)|Sets the policy that defines how the task scheduler \
            deals with multiple instances of the task.|
        """
    )
    r1c1, r1c2 = st.columns([0.15,0.15])
    r2c1, r2c2 = st.columns([0.15,0.15])
    r3c1, r3c2 = st.columns([0.15,0.15])
    r4c1, r4c2 = st.columns([0.15,0.15])

    with r1c1:
        st.session_state.ntask_allow_demand_start = st.checkbox("Allow Demand Start")
    with r1c2:
        st.session_state.ntask_start_when_avail = st.checkbox("Start When Available")

    with r2c1:
        st.session_state.ntask_enabled = st.checkbox("Enabled")
    with r2c2:
        st.session_state.ntask_hidden = st.checkbox("Hidden")

    with r3c1:
        st.session_state.ntask_restart_interval = st.selectbox(
            "Restart Interval", TaskRestartIntervals.intervals.keys())
    with r3c2:
        st.session_state.ntask_restart_count = st.number_input(
            "Restart Count",
            min_value=1,
            max_value=3
        )

    with r4c1:
        st.session_state.ntask_exec_time_limit = st.selectbox(
            "Execution Time Limit", TaskExecutionLimit.limits.keys())

    with r4c2:
        st.session_state.ntask_multiple_instances = st.selectbox(
            "Multiple Instances Policy", TaskInstancePolicy.policies.keys()
        )
