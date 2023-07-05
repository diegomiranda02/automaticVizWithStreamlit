import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

print(df.head())


#st.map(df)



max_bound = max(abs(max(df['lat'])- min(df['lat'])), abs(max(df['lon'])- min(df['lon']))) * 111
zoom = 11.5 - np.log(max_bound)

fig = px.scatter_mapbox(df, lat="lat", lon="lon", zoom=zoom)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)