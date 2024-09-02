import streamlit as st
import polars as pl
st.header("Tasks Scheduled Today")

# =================================================================================================
# Total Metrics
# =================================================================================================

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    with st.container(border=True):
        st.write(":green[:material/check_circle: READY]")
        st.metric(
            "TASKS READY",
            st.session_state.today_tasks.count_task_by_state(3),
            label_visibility="collapsed"
        )
    with st.container(border=True):
        st.write(":blue[:material/run_circle: RUNNING]")
        st.metric(
            "TASKS RUNNING",
            st.session_state.today_tasks.count_task_by_state(4),
            label_visibility="collapsed"
        )
    with st.container(border=True):
        st.write(":red[:material/report: MISSED RUNS]")
        st.metric(
            "TASKS MISSED RUNS",
            st.session_state.today_tasks["number_of_missed_runs"].sum(),
            label_visibility="collapsed"
        )


with metric_col2:
    with st.container(border=True):
        st.write(":green[:material/verified: COMPLETED]")
        st.metric(
            "TASKS COMPLETED",
            st.session_state.today_tasks.filter(
                pl.col("last_task_result")==0
            ).shape[0],
            label_visibility="collapsed"
        )
    with st.container(border=True):
        st.write(":orange[:material/do_not_disturb: DISABLED]")
        st.metric(
            "TASKS DISABLED",
            st.session_state.today_tasks.count_task_by_state(1),
            label_visibility="collapsed"
        )
    
    
with metric_col3:
    with st.container(border=True):
        st.write(":blue[:material/today: SCHEDULED TO RUN]")
        st.metric(
            "TASKS SCHEDULED",
            st.session_state.today_tasks.filter(
                pl.col("last_task_result")==267011
            ).shape[0],
            label_visibility="collapsed"
        )
    with st.container(border=True):
        st.write(":orange[:material/playlist_add_check_circle: QUEUED]")
        st.metric(
            "TASKS QUEUED",
            st.session_state.today_tasks.count_task_by_state(2),
            label_visibility="collapsed"
        )
    

task_list = (st.session_state.today_tasks
    .select(
        "name",
        "task_state_definition",
        "next_run_time",
        "last_run_time",
        "last_task_result_definition"
    )
    .rename({
        "name":"NAME",
        "task_state_definition":"STATE",
        "next_run_time":"NEXT RUN TIME",
        "last_run_time":"LAST RUN TIME",
        "last_task_result_definition":"LAST TASK RESULT"
    })
    .sort("NAME")
)

st.dataframe(task_list, hide_index=True)
