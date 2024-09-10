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

Questions for the bot: 
1)	Q: interpret correlations plots under Finished Goods and Lab Results Sections , what do they mean? 
response:  
1.	Microbiological vs Customer Satisfaction Results: Shows a high positive correlation, meaning as microbiological results improve, so does customer satisfaction.
2.	Chemical Results vs Customer Satisfaction Results: Displays a high inverse correlation, where higher chemical results (away from the optimal range) lead to lower customer satisfaction.
3.	Physical Results vs Customer Satisfaction Results: Exhibits a low correlation, with weaker connections between physical test results and customer satisfaction.
4.	Seal Integrity Results vs Customer Satisfaction Results: Demonstrates a moderate correlation, where seal integrity failures lower satisfaction scores.
Each plot now includes a legend indicating the strength of the correlation. 
2)  Are there specific patterns in test failures (occurring at a certain time for example)?
Response:
●	We observed that failures tend to occur at certain times ( after maintenance and during high production), this indicates process issues. Tracking the failures in correlation with production schedules, cleaning procedures, or environmental conditions might help pinpoint the root cause.
3. Do test results show seasonality or environmental dependencies?
Response:
●	We observed that microbiological test failures increased in warmer months and during higher humidity. If such trends exist, preventive measures like more frequent cleaning or environmental monitoring could mitigate the risk.
●	Action: Implement seasonal adjustments to cleaning schedules or environmental controls during higher-risk periods.
4. How do test failures correlate with customer complaints?
Response:
●	We saw that certain types of test failures (seal integrity or chemical deviations) align with customer complaints, it signals a quality issue impacting end users. Close monitoring of these correlations allows for proactive corrections before products hit the market.
●	Action: Focus on improving tests that are most linked to customer satisfaction, like packaging or chemical composition, to prevent complaints.
5. Are certain types of test failures more costly than others?
Response:
●	microbiological failures that lead to product recalls are often much more expensive than packaging failures that only require reworking. In the last month, 2 deviations in microbiological testing occurred that had cost implications. Understanding these different failures helps prioritize areas for investment and process improvement.
●	Action: Allocate resources to areas that reduce the most expensive failures (e.g., tighter microbiological controls).


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

        





