import streamlit as st
from process_control.process_control import render_process_control
from prereq_and_verif.prereq_and_verif import render_preq_and_verif
from supplier_management.supplier_management import render_supplier_management
from CAPA.CAPA import render_CAPA
from recall_preparedness.recall_preparedness import render_recall_preparedness
from map import render_map

from sidebar import render_sidebar

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

if "show_alerts" not in st.session_state:
    st.session_state.show_alerts=False

st.set_page_config(layout='wide')

st.header("INNOVA-Q - Quality Performfamce Forecast")
render_sidebar()
render_map()
render_preq_and_verif()
render_process_control()
render_supplier_management()
render_CAPA()
render_recall_preparedness()


