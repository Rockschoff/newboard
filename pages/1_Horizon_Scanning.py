import streamlit as st
from tavily import TavilyClient
from openai import OpenAI
import json

st.set_page_config(layout="wide")

tavily_client = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "search_news" not in st.session_state:
    st.session_state["search_news"] = ""
   

st.header("HORIZON SCANNING")

def load_report(ingridents , locations)->None:

    for location in locations:
        for ingridient in ingridents:
            print('okay')
    

    st.session_state.search_news = ""

    return

def get_results_from_tavily(ingridient, location):

    search_phrase = f"Critical recalls and food safety and quality news  for {ingridient} in {location}"

    response = tavily_client.search(query = search_phrase,
                         search_depth="advanced",
                         topic="news",
                         days="365",
                         max_results=10,
                         include_raw_content=True,
                         include_answer=True,
                         use_cache=True)
    
    return response

def generate_horizon_scanning_report(response):

    search_results = json.dumps(response)

    prompt = ("Please use these search results to generate a horizon scanning report the report must be structured"
              "it must access the reisk of each related to us. We a cokkie Manfacturing company with one plant in Autin Texas"
              "And another plant in the Colorado. The search results are related to the ingreident that we use and the country that we"
              "get that ingridinet from. The report should the comprehesive and should explain how it is evalutings\n\n"
              f"Here are teh search results : {search_results}"
              "IMPORTANT NOTES : In your assess asses all the key events in the search results and analyze thier significance,"
              "Whenever you see mention the search results your must links to the correspding new insight"
              "You also provide me information that what it means to me and what should I do now\n\n"
              "Order the risk assessment from very high risk to low risk\n\n"
              "MOST IMPORTANT RULE 1 : Only include the news that relvant food recalls, and food safety in my organization"
              "MOST IMPORTANT RULE 2 : Tie all the analsys to CFR regulations and in the end there should be a refernce section for this as well")
    
    try:
        response = client.chat.completions.create(
            model="o1-preview",
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )
        

        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return "# Error"

    

    

ingridents = st.multiselect("Ingredients" ,
               options=["wheat" , "peanut butter", "chocolate chips","corn flour","eggs" ] ,
               default=["wheat" , "chocolate chips"])

locations = st.multiselect("Locations" , options=["USA" , "France" , "Brazil"] , default=["USA"])

container=st.container()

if st.button("Generate Latest report"):
    with st.status("Loading the data" , expanded=True):
        for location in locations:
            for ingridient in ingridents:
                st.write(f"searching results for {ingridient} in {location}")
                response = get_results_from_tavily(ingridient=ingridient , location=location)
                st.write(f"summary of the search results : {response['answer']}")
                st.write("generating complete report")
                report_markdown = generate_horizon_scanning_report(response)
                st.write("report has been generated continuing to the next step")
                with container.expander(f"{location} , {ingridient}"):
                    st.markdown(report_markdown)


                


