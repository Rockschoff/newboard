import streamlit as st

def render_preq_and_verif():

    with st.expander("Prequisite and Verification Programs"):

        kpis = [  render_sanitation, render_lab_results]
        kpi_names = [ "Sanitation", "Finished Goods and Lab Results"]

        tabs = st.tabs(kpi_names)
        for i , tab in enumerate(tabs):
            with tab:
                kpis[i]()



def render_sanitation():
    st.subheader("Sanitation")
    images1 = ["./prereq_and_verif/static/sanitation/visual_inspection.png" , "./prereq_and_verif/static/sanitation/atp_test.png"]
    images2 = ["./prereq_and_verif/static/sanitation/EMP_grouped.png"]
    images3=["./prereq_and_verif/static/sanitation/grouped_details.png"]

    tabs = st.tabs(["Visual Inspection" , "EMP results"])

    with tabs[0]:
        cols = st.columns([1 , 1])
        for i , col in enumerate(cols):
            with col :
                st.image(images1[i] , use_column_width=True)
    
    with tabs[1]:
        st.image(images2[0])

    if st.checkbox("View Details"):
        st.image(images3[0])

    

def render_lab_results():

    st.subheader("Finished Goods and Lab Results")

    image = "./prereq_and_verif/static/grouped.png"

    st.image(image)

