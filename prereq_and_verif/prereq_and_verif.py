import streamlit as st
from uuid import uuid4
def render_preq_and_verif():

    with st.expander("Prerequisite and Verification Programs"):

        kpis = [   render_sanitation, render_lab_results, render_preventive_maintanence,render_internal_audits ,render_training]
        kpi_names = [   "Sanitation", "Product Lab Results","Preventive Maintenance", "Internal Audits", 'Training' ]

        tabs = st.tabs(kpi_names)
        for i , tab in enumerate(tabs):
            with tab:
                kpis[i]()



def render_training():
    st.subheader("Training")

    images = ["./prereq_and_verif/static/training/training_grouped.png"]
    st.image(images[0])

def render_internal_audits():
    st.subheader("Internal Audits")
    
    images = ["./prereq_and_verif/static/internal_audits/observations.png","./prereq_and_verif/static/internal_audits/common_observations.png"]
    tab_names = ["Internal Audit Observations" , "Comman Observations"]

    tabs = st.tabs(tab_names)
    for i , tab in enumerate(tabs):
        with tab:
            st.image(images[i])


def render_preventive_maintanence():
    st.subheader('Preventive Maintenance')

    images = ["./prereq_and_verif/static/preventive_maintanence/equipment_pass_rate.png" ,
              "./prereq_and_verif/static/preventive_maintanence/general_efficiency.png" ,
              "./prereq_and_verif/static/preventive_maintanence/stoppage_reasons.png"]
    corr_images = ["./prereq_and_verif/static/preventive_maintanence/qualty_control_vs_pm.png" ,
                   "./prereq_and_verif/static/preventive_maintanence/complaints_vs_equipment_performance.png",
                   "./prereq_and_verif/static/preventive_maintanence/quality_vs_equipment_performance.png",
                   "./prereq_and_verif/static/preventive_maintanence/yield_vs_eqipment_perfomance.png" ]
    
    tab_names = ["Equipment Pass Rate" , "General Efficiency" , "Reasons fro Stoppage"]
    corr_tab_names = ["Cost of Quality Control vs Preventive Maintanence" ,
                      "Customer Complaints vs Equipment Performance",
                      "Product Quality vs Equipment Performance",
                      "Yield vs Equipment Performance"]
    
    tabs = st.tabs(tab_names)
    for i , tab in enumerate(tabs):
        with tab:
            st.image(images[i])

    if st.checkbox("View Correlations" , key="pm_corr"):
        corr_tabs = st.tabs(corr_tab_names)
        for i  , corr_tab in enumerate(corr_tabs):
            with corr_tab:
                st.image(corr_images[i])


    

    

def render_sanitation():
    st.subheader("Sanitation")
    st.error("3 ATP tests failed, equipment resanitized. Several Listeria spp tests failed, product on hold, investigation ongoing.")
    st.warning("2 visual inspection test failed, equipment resanitized. Several Coliform tests failed, product on hold")
    # st.warning("2 visual inspection test failed, equipment resanitized")
    images1 = ["./prereq_and_verif/static/sanitation/visual_inspection.png" , "./prereq_and_verif/static/sanitation/atp_test.png"]
    images2 = ["./prereq_and_verif/static/sanitation/EMP_grouped.png"]
    images3=["./prereq_and_verif/static/sanitation/grouped_details.png"]

    corr_images = ["./prereq_and_verif/static/sanitation/sanitation_vs_micro_biological_test_failure.png","./prereq_and_verif/static/sanitation/sanitation_vs_yield_n_product_waste.png"]
    corr_tab_names = ["Sanitation vs Microbiology Test Failures",
                      "Sanitation vs Product Waste and Yield"]


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

    if st.checkbox("View Correlations" , key="sani_corr"):
        corr_tabs = st.tabs(corr_tab_names)

        for i , corr_tab in enumerate(corr_tabs):
            with corr_tab:
                st.image(corr_images[i])

    

def render_lab_results():

    st.subheader("Finished Goods and Lab Results")

    image = "./prereq_and_verif/static/lab_results/grouped.png"

    st.image(image)

    corr_images=["./prereq_and_verif/static/lab_results/microbiological_reuslts_vs_satifaction.png",
                 "./prereq_and_verif/static/lab_results/physical_results_vs_satisfaction.png",
                 "./prereq_and_verif/static/lab_results/chem_results_vs_satisfaction.png",
                 "./prereq_and_verif/static/lab_results/seal_integrity_vs_cusotmer_satisfaction.png",
                 "./prereq_and_verif/static/lab_results/cost_vs_micro_biological.png"]
    
    corr_tab_names = ["Microbiological Results vs Customer Satisfaction",
                      "Physical Results vs Customer Satisfaction",
                      "Chemical Results vs Customer Satisfaction",
                      "Seal Integrity vs Cusomter Satisfaction",
                      "Cost vs Microbiological Results"]
    

    if st.checkbox("View Correlations" , key="lab_results_corr"):
        corr_tabs = st.tabs(corr_tab_names)

        for i , corr_tab in enumerate(corr_tabs):
            with corr_tab :
                st.image(corr_images[i])

