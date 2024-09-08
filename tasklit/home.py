import streamlit as st
import polars as pl
from components.home_page import (
    ready_metric,
    completed_metric,
    running_metric,
    scheduled_metric,
    queued_metric,
    disabled_metric,
    missed_metric,
    task_event_report
)

r1c1, r1c2, r1c3, r1c4 = st.columns(4)
r2c1, r2c2, r2c3 = st.columns(3)
r3c1, r3c2, r3c3 = st.columns(3)
r4c1, r4c2, r4c3 = st.columns(3)

with r1c1:
    ready_metric()

with r1c2:
    completed_metric()

with r1c3:
    running_metric()

with r1c4:
    scheduled_metric()

with r2c1:
    queued_metric()

with r2c2:
    disabled_metric()

with r2c3:
    missed_metric()

st.divider()
task_event_report()