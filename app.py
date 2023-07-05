# streamlit library
import streamlit as st
st. set_page_config(layout="centered") 

import time

# JSON to render the API responde into a Python Object
import json

# Pandas
import pandas as pd

# Numpy
import numpy as np

# Plotly
import plotly.express as px


def get_data():    
    # Open data.json file
    f = open('data.json')

    # JSON object as a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()

    # Return the json data
    return data

data_content = get_data()

for key,value in data_content.items():
    if key.startswith("table") and isinstance(value, list):
        st.table(pd.DataFrame(value))

    elif key.startswith("title") and isinstance(value, str):
        st.header(value)
    
    elif key.startswith("subtitle") and isinstance(value, str):
        st.header(value)

    elif isinstance(value, str):
        st.write(value)    

    elif key.startswith("map") and isinstance(value, list):
        # Converting list to Dataframe
        df = pd.DataFrame(value)

        # Snippet of code based on the article 1 in References section
        max_bound = max(abs(max(df['lat'])- min(df['lat'])), abs(max(df['lon'])- min(df['lon']))) * 111
        zoom = 11.5 - np.log(max_bound)

        # Snippet of code based on the article 2 in References section
        fig = px.scatter_mapbox(df, lat="lat", lon="lon", zoom=zoom)

        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)
