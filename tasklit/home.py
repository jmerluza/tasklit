import streamlit as st
import polars as pl

# =================================================================================================
# TASKS SCHEDULED FOR TODAY METRICS.
# =================================================================================================
st.subheader(":red[_TASKS SCHEDULED FOR TODAY_]")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.write("**READY**")
    with st.container(border=True):
        st.subheader(
            f":green[:material/check_circle:] \
            {st.session_state.today_tasks.count_task_by_state(3)}"
        )

    st.write("**RUNNING**")
    with st.container(border=True):
        st.subheader(f":blue[:material/run_circle:] \
        {st.session_state.today_tasks.count_task_by_state(4)}"
    )

    st.write("**MISSED RUNS**")
    with st.container(border=True):
        st.subheader(f":red[:material/report:] \
        {st.session_state.today_tasks['number_of_missed_runs'].sum()}"
    )

with metric_col2:
    st.write("**COMPLETED**")
    with st.container(border=True):
        st.subheader(f":green[:material/verified:] \
        {st.session_state.today_tasks.filter(pl.col('last_task_result')==0).shape[0]}"
    )

    st.write("**DISABLED**")
    with st.container(border=True):
        st.subheader(f":orange[:material/do_not_disturb:] \
        {st.session_state.today_tasks.count_task_by_state(1)}"
    )

with metric_col3:
    st.write("**SCHEDULED TO RUN**")
    with st.container(border=True):
        st.subheader(f":blue[:material/today:] \
        {st.session_state.today_tasks.filter(pl.col('last_task_result')==267011).shape[0]}"
    )

    st.write("**QUEUED**")
    with st.container(border=True):
        st.subheader(f":orange[:material/playlist_add_check_circle:] \
        {st.session_state.today_tasks.count_task_by_state(2)}"
    )

st.divider()

# =================================================================================================
# TASK STATISTICS FOR TODAY
# =================================================================================================
st.subheader(":red[_TASK STATISTICS FOR TODAY_]")
hist_df = st.session_state.task_history.get_todays_history()

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
with stat_col1:
    st.write("**ERRORS**")
    with st.container(border=True):
        st.subheader(f":red[:material/report:] {hist_df.error_event_count()}")

with stat_col2:
    st.write("**WARNING**")
    with st.container(border=True):
        st.subheader(f":orange[:material/warning:] {hist_df.warning_event_count()}")

with stat_col3:
    st.write("**INFORMATION**")
    with st.container(border=True):
        st.subheader(f":blue[:material/info:] {hist_df.information_event_count()}")

st.write(f"")