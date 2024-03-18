# import dependencies
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# read the clean data file 
cleandata_df = pd.read_csv("output/joined_data.csv")
region_df = pd.read_csv("resources/regionaldata.csv")

print(region_df)

print(cleandata_df)

# Merge the two DataFrames together based on the alpha-3 column they share
cleandata_df = pd.merge(cleandata_df, region_df[['country_name', 'region']], on="country_name")
print(cleandata_df)


app.layout = html.Div([
    # Dropdown layout (left side)
    html.Div([
        html.Label(["Fators affecting Happiness Index"]),
        dcc.Dropdown(id='my_dropdown',
                    options=[
                        {'label': 'GDP', 'value': 'GDP'},
                        {'label': 'Infant mortality', 'value': 'Infant mortality'},
                        {'label': 'Life expectancy', 'value': 'Life expectancy'},
                        {'label': 'Infant mortality', 'value': 'Infant mortality'},
                        {'label': 'Maternal mortality ratio', 'value': 'Maternal mortality ratio'},
                        {'label': 'Minimum wage', 'value': 'Minimum wage'},
                        {'label': 'Out of pocket health expenditure', 'value': 'Out of pocket health expenditure'},
                        {'label': 'Physicians per thousand', 'value': 'Physicians per thousand'},
                        {'label': 'Population', 'value': 'Population'},
                        {'label': 'Unemployment rate', 'value': 'Unemployment rate'},
                        {'label': 'Social support', 'value': 'Social support'},
                        {'label': 'Freedom to make life choices', 'value': 'Freedom to make life choices'},
                        {'label': 'Generosity', 'value': 'Generosity'},
                        {'label': 'Perceptions of corruption', 'value': 'Perceptions of corruption'}
                    ],
                    optionHeight=25,  # height between dropdown options
                    # value='GDP',       # default dropdown value
                    disabled=False,
                    multi=False,       # allow multiple selection
                    searchable=True,
                    placeholder='Please select...',
                    clearable=True,
                    style={'width': "100%",'marginBottom':'20px'},
                    className='select_box',
                    persistence=True,
                    persistence_type='memory'
        )
    ], className='three columns'),  # Make the dropdown occupy three columns
    html.Label("Select Regions"),
    dcc.Checklist(id='region_btns', 
                options=[{'label': region, 'value': region} for region in cleandata_df['region'].unique()], 
                value=[],
                inline=True),

    # Graph layout (right side)
    html.Div([
        dcc.Graph(id='the_graph')
    ], className='nine columns'),  # Make the graph occupy nine columns
])
# ----------------------
# add input and output component for scattered plot
# add input and output component for bar chart
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),
    Input(component_id='region_btns', component_property='value')]
)
def update_graph(my_dropdown,selected_regions):
    # print("Selected Dropdown Value:", my_dropdown)  # Add this line to print the dropdown value
    
    cleandata_dff = cleandata_df

    # Filter data based on selected regions
    if selected_regions:
        cleandata_dff = cleandata_dff[cleandata_dff['region'].isin(selected_regions)]

    scattered_chart = px.scatter(
        data_frame=cleandata_dff, 
        x= 'Happiness Score', 
        y=my_dropdown,
        hover_data=['country_name'],
        text="country_name",
        height=550
    )
    return scattered_chart

if __name__ == '__main__':
    app.run_server(debug=True)
