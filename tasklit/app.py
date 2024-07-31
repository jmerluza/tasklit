import streamlit as st

st.title(":clock2: TaskLit")
hcol1, hcol2, hcol3, hcol4 = st.columns(4)

with hcol1:
    st.button(label="Create Task", use_container_width=True)
with hcol2:
    st.button(label="Remove Task", use_container_width=True)
with hcol3:
    st.button(label="Import Task", use_container_width=True)
with hcol4:
    st.button(label="Run Task", use_container_width=True)

st.divider()
