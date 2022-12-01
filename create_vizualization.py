import numpy as np 
import pandas as pd
import plotly.express as px



def plot_map(df, col, pal):
    df = df[df[col]>0]
    fig = px.choropleth(df, locations="Country", locationmode='country names', 
                  color=col, hover_name="Country", 
                  title=col, color_continuous_scale=pal,width=1500)
    fig
    return fig