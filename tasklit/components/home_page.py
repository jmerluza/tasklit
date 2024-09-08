import streamlit as st
import polars as pl

def ready_metric():
    st.write("**READY**")
    with st.container(border=True):
        st.subheader(
            f":green[:material/check_circle:] \
            {st.session_state.tasks_completed_today.total_number_of_tasks_by_state(3)}"
        )

def completed_metric():
    st.write("**COMPLETED**")
    with st.container(border=True):
        st.subheader(f":green[:material/verified:] \
        {st.session_state.tasks_completed_today.filter(pl.col('last_task_result')==0).shape[0]}"
    )
        
def running_metric():
    st.write("**RUNNING**")
    with st.container(border=True):
        st.subheader(f":blue[:material/run_circle:] \
        {st.session_state.tasks_completed_today.total_number_of_tasks_by_state(4)}"
    )

def scheduled_metric():
    st.write("**SCHEDULED TO RUN**")
    with st.container(border=True):
        st.subheader(f":blue[:material/today:] \
        {st.session_state.tasks_completed_today.filter(pl.col('last_task_result')==267011).shape[0]}"
    )
        
def queued_metric():
    st.write("**QUEUED**")
    with st.container(border=True):
        st.subheader(f":orange[:material/playlist_add_check_circle:] \
        {st.session_state.tasks_completed_today.total_number_of_tasks_by_state(2)}"
    )

def disabled_metric():
    st.write("**DISABLED**")
    with st.container(border=True):
        st.subheader(f":orange[:material/do_not_disturb:] \
        {st.session_state.tasks_completed_today.total_number_of_tasks_by_state(1)}"
    )

def missed_metric():
    st.write("**MISSED RUNS**")
    with st.container(border=True):
        st.subheader(f":red[:material/report:] \
        {st.session_state.tasks_completed_today['number_of_missed_runs'].sum()}"
    )

def task_event_report():
    history_data = st.session_state.task_history
    error_data = history_data.filter(pl.col("Event Log Description")=="ERROR")
    warning_data = history_data.filter(pl.col("Event Log Description")=="WARNING")

    error_task_list = error_data["Task Name"].unique(maintain_order=True).to_list()
    warning_task_list = warning_data["Task Name"].unique(maintain_order=True).to_list()

    st.header("Task Event Report")
    info_count = history_data.information_event_count()
    warning_count = history_data.warning_event_count()
    error_count = history_data.error_event_count()
    st.write(f"_{info_count} information logs | {warning_count} warning logs | {error_count} error logs_")
    for errors in error_task_list:
        with st.expander(errors, icon="⛔"):
            error_df = (error_data
                .filter(pl.col("Task Name")==errors)
                .select("Event Created","Event ID","Event ID Description")
            )
            st.write(f"There were {error_df.shape[0]} errors for this task.")
            st.dataframe(error_df, hide_index=True)

    for warning in warning_task_list:
        with st.expander(warning, icon="⚠️"):
            warning_df = (warning_data
                .filter(pl.col("Task Name")==warning)
                .select("Event Created","Event ID","Event ID Description")
            )
            st.write(f"There were {warning_df.shape[0]} warnings for this task.")
            st.dataframe(warning_df, hide_index=True)

