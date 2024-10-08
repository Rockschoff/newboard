import streamlit as st
def render_process_control():
    with st.expander("Process Control and Monitoring"):

        kpis = [render_cooking, render_refrigeration , render_labeling , render_fmc]
        kpi_names = ["Cooking" , "Refrigeration" , "Labeling" , "Foreign Material Controls"]
        tabs = st.tabs(kpi_names)

        for i , tab in enumerate(tabs):
            with tab:
                kpis[i]()
            

def render_refrigeration():
    st.subheader("Refrigeration")

def render_labeling():
    st.subheader("Labeling")

def render_fmc():
    st.subheader("Foreign Material Controls")     
       


def render_cooking():

    st.subheader("Continuous Cooking Temp")

    cols = st.columns([1 , 1 ,1])
    images = ["./process_control/static/temp_line1.png" , "./process_control/static/temp_line2.png" , "./process_control/static/temp_line1.png"]

    for i , col in enumerate(cols):
        with col:
            st.image(images[i] , use_column_width=True)


    if st.checkbox("View Correlations"):
        
        tabs = st.tabs(["Temperature Vs Product Quality" , "Temperature Vs Customer Complaints" , "Temperature vs Yeild"])

        corr_images = ["./process_control/static/temp_vs_productquality.png","./process_control/static/temp_vs_complaints.png","./process_control/static/temp_vs_yield.png"]

        for i , tab in enumerate(tabs):
            with tab:
                st.image(corr_images[i])


        
    
