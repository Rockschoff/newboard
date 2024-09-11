import streamlit as st


def render_recall_preparedness():
    with st.expander("Recall Preparedness"):

        kpi_names = ["Recalls" , "Withdrawls" , "Near Misses"]

        tabs = st.tabs(kpi_names)

        for i , tab in enumerate(tabs):
            with tab:
                st.subheader(kpi_names[i])