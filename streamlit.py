import streamlit as st
from process_control.process_control import render_process_control
from prereq_and_verif.prereq_and_verif import render_preq_and_verif

st.set_page_config(layout='wide')



render_preq_and_verif()
render_process_control()


