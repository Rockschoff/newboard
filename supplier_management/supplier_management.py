import streamlit as st


def render_supplier_management():
    with st.expander("Supplier Management"):
        kpi_names = ["Supplier Performance" , "Material Performance" , "Exceptions", "Horizon Scanning"]
        tabs = st.tabs(kpi_names)
        for i , tab in enumerate(tabs):
            with tab:
                st.subheader(kpi_names[i])