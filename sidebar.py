import streamlit as st
import time
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

system_message="""

You are a helpful FDA assitant that is attached to the QPF (Quality Performance and Forecast) Dashbaord gives helpful answers to the user queries about the dashboard,
The Dashbaord is bring together information that is related to FSQ. You can answer questions  about the dasboards based on the factaul data provided below

where ever possible always tei your reponse with FDA regulations and give actionable steps to the user

HERE IS FACTUAL DATA ABOUT THE PLANT THAT YOU KNOW FROM THE DASHBOARD

Are there any temperature control violations that could impact food safety?
   BOT : Yes, there was one instance where the temperature dropped below the critical limit of 158°F, potentially compromising food safety due to undercooking.

What percentage of cooking cycles stayed within the optimal food safety range?
   BOT: 96% of cooking cycles stayed within the safe temperature range of 158°F to 175°F, with 4% requiring further attention.

Is there a correlation between cooking temperature and microbial test results?
BOT: Yes, lower cooking temperatures correlate with an increased risk of positive microbial test results, particularly in undercooked products.

Can you identify any recurring patterns in temperature violations?
BOT: Temperature violations typically occur during the late afternoon shifts. It may be worth reviewing shift protocols and equipment maintenance.

Have any batches been flagged for re-testing or re-cooking due to temperature issues?
BOT: Yes, two batches in the last quarter were flagged for re-testing due to cooking temperatures falling below the critical limit.

How can we improve temperature control to minimize food safety risks?
BOT: Implementing more frequent equipment calibration and continuous monitoring during shifts where deviations tend to occur may help maintain tighter temperature control.

Were there any temperature deviations that could result in a potential product recall?
BOT: Yes, one temperature deviation fell below the critical limit, posing a risk of undercooking, which could lead to a recall if undetected.

What actions are required to prevent temperature-related non-conformances in the future?
BOT: Regular audits of cooking equipment and enhanced real-time monitoring with alerts during shifts showing

"""

def bot_response()->str:

    # self.system_message= self.system_message+ f"{st.session_state.app.generate_app_state()}" + """ Please make good use of this infomration to answer the user queries"""
    run = client.beta.threads.create_and_run(
        assistant_id=st.secrets['OPENAI_ASSISTANT_ID'],
        model = st.secrets["OPENAI_MODEL"],
        thread =  {
            "messages": st.session_state.chat_history
            },

        tool_choice={"type": "file_search"},
        instructions=system_message
    )
    def wait_on_run(run):
        
        while run.status == "queued" or run.status == "in_progress":
            print("Waiting")
            run = client.beta.threads.runs.retrieve(
                thread_id=run.thread_id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run
    run = wait_on_run(run)
    messages = client.beta.threads.messages.list(thread_id=run.thread_id)
    # print(messages.data[0])
    return messages.data[0].content[0].text.value

def render_sidebar():
    with st.sidebar:

        st.write("Ask In-Q Center")
        
        container = st.container(height=500 , border=True)

        input = st.chat_input()

        if input :
            st.session_state.chat_history.append({"role" : "user" , "content" : input})


        with container:
            for message in st.session_state.chat_history:
                st.chat_message(message["role"]).write(message["content"])

        if st.session_state.chat_history and st.session_state.chat_history[-1]["role"]=="user":
            status = st.status("IN-Q center is processing the query" , state="running")
            message={"role" : "assistant" , "content" : bot_response()}
            status.update(label="Reponse has been loaded" , state="complete")
            st.session_state.chat_history.append(message)
            with container:
                st.chat_message(message["role"]).write(message["content"])

        





