import streamlit as st
from process_control.process_control import render_process_control
from prereq_and_verif.prereq_and_verif import render_preq_and_verif

from map import render_map

from sidebar import render_sidebar

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

st.set_page_config(layout='wide')
render_sidebar()
render_map()
render_preq_and_verif()
render_process_control()


