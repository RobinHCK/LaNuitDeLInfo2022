import numpy as np 
import pandas as pd
import plotly.express as px

def group_col(df, col_1, col_2):
    group = df.groupby(col_1, as_index=False)[col_2].count()
    return group

def plot_map(df, col, pal):
    df = df[df[col]>0]
    fig = px.choropleth(df, locations="Country", locationmode='country names', 
                  color=col, hover_name="Country", 
                  title=col, color_continuous_scale=pal,width=1500)
    fig
    return fig

def update_fig_layout(fig):
    plot_bg_color='rgba(255, 255,255, 0.8)'

    fig.update_layout(xaxis_title="",)
    fig.update_layout(xaxis_title="Dim1",  yaxis_title="Dim2",plot_bgcolor=plot_bg_color,)
    fig.update_yaxes( showline=True, linewidth=2, linecolor='white', mirror=True, showgrid=True, gridwidth=0.1, gridcolor='white', tickprefix='', ticksuffix=' ') 

    fig.update_xaxes(visible=True, showticklabels=True)
    fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='rgb(230, 230, 230)')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='rgb(230, 230, 230)')

    return fig


def plot_hist(data, col1, col2):
    # df = df['patho_niv3']
    group = group_col(data, col1, col2)
    fig = px.bar(group, x=col1, color=col1, y=col2)
    # fig.show()
    fig = update_fig_layout(fig)
    fig.update_layout(
    title='Nombre de personnes atteintes du sida en France selon le sexe',
    title_x = 0.5, 
    xaxis_title="Sexe",
    yaxis_title="Incidence",
    legend_title="Sexe",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)
    return fig