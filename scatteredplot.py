# import dependencies
import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# read the clean data file 
cleandata_df = pd.read_csv("output/joined_data.csv")
region_df = pd.read_csv("resources/regionaldata.csv")

# Merge the two DataFrames together based on the alpha-3 column they share
cleandata_df = pd.merge(cleandata_df, region_df[['country_name', 'region']], on="country_name")

app.layout = html.Div([
    # Main Title
    html.Div([
        html.H1("World Happiness Analysis", style={'textAlign': 'center','color':'white'})
    ]),

    # Dropdown layout (left side)
    html.Div([
        html.Label("Factors affecting Happiness Index", style={'color': 'white'}),
        dcc.Dropdown(id='my_dropdown',
                    options=[
                        {'label': 'GDP', 'value': 'GDP'},
                        {'label': 'Infant mortality', 'value': 'Infant mortality'},
                        {'label': 'Life expectancy', 'value': 'Life expectancy'},
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
                    optionHeight=40,  # height between dropdown options
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
    
    # Region selection layout (left side)
    html.Div([
        html.Label("Select Regions", style={'color': 'white'}),
        dcc.Checklist(id='region_btns', 
                    options=[{'label': region, 'value': region} for region in cleandata_df['region'].unique()], 
                    value=[],
                    inline=True,
                    style={'color': 'white'})  # Set the font color of the checklist options to white
    ], className='three columns'),

    # Graph layout (right side)
    html.Div([
        dcc.Graph(id='the_graph', style={'margin-top': '20px'})  # Adding margin-top to the scatter plot
    ], className='nine columns'),  # Make the graph occupy nine columns
])

# Callback to update the scatter plot
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),
    Input(component_id='region_btns', component_property='value')]
)
def update_graph(my_dropdown, selected_regions):
    cleandata_dff = cleandata_df

    # Filter data based on selected regions
    if selected_regions:
        cleandata_dff = cleandata_dff[cleandata_dff['region'].isin(selected_regions)]

    scattered_chart = px.scatter(
        data_frame=cleandata_dff, 
        x='Happiness Score', 
        y=my_dropdown,
        color='country_name',
        size='Happiness Score',
        # custom_data=['country_name'],
        # hover_name='Country'
        hover_data=['country_name'], text='country_name',
        height=550
    )

    # Update marker size and color scale
    scattered_chart.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
                    selector=dict(mode='markers'))

    return scattered_chart

if __name__ == '__main__':
    app.run_server(debug=True)