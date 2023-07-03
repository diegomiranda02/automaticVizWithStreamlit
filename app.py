# streamlit library
import streamlit as st
st. set_page_config(layout="wide") 
# HTML requests library
from requests_html import HTMLSession

# basic libraries
import time

# JSON to render the API responde into a Python Object
import json

# Pandas
import pandas as pd


# start an HTML session to get page contents
sess = HTMLSession()

# call the server API routes to get an answer
def get_data(command):    
    api_url = f"http://localhost:8000/llm_api?command={command}"
    course_json = sess.get(api_url).text
    return course_json

# insert fields on the interface
st.title('NLP AI')
st.title('Assistente')
command = st.text_input("O que deseja?", "Gerar um relatorio?", disabled=False)

# check if the Send button was pressed and get the API Data
if st.button("Enviar"):        
    with st.spinner('Consulta em andamento...'):
        data = get_data(command=command)
        data_content = json.loads(data)

        count = 0
        for key,value in data_content.items():

            if isinstance(value, str):
                # Print text Streamlit
                t = st.empty()
                for i in range(len(value) + 1):
                    t.markdown("## %s" % value[0:i])
                    time.sleep(0.04)

            if isinstance(value, list):
                #print(value)
                df_from_list = pd.DataFrame(value)
                print(df_from_list)
                st.table(df_from_list)

            count += 1
