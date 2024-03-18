# import dependencies
import os
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash
from dash import dcc, html, Input, Output

# Set path to input CSV files based on current directory
current_dir = os.path.dirname(__file__)
csv_file_path_1 = os.path.join(current_dir, 'output', 'joined_data.csv')
csv_file_path_2 = os.path.join(current_dir, 'resources', 'regionaldata.csv')

# Read in cleaned data from CSV
cleandata_df = pd.read_csv(csv_file_path_1)
region_df = pd.read_csv(csv_file_path_2)

# Merge the two DataFrames together based on the alpha-3 column they share
cleandata_df = pd.merge(cleandata_df, region_df[['country_name', 'region']], on="country_name")

# Set up Dash application environment
app = dash.Dash(__name__)

# Define Dash HTML layout
app.layout = html.Div([
    # Happiness Map
    html.Div([
        dcc.Graph(id='happiness-map')
    ], className='twelve columns'),  # Make the map occupy twelve columns

    # Dropdown layout (left side)
    html.Div([
        html.Label(["Factors affecting Happiness Index"]),
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
                     disabled=False,
                     multi=False,  # allow multiple selection
                     searchable=True,
                     placeholder='Please select...',
                     clearable=True,
                     style={'width': "100%", 'marginBottom': '20px'},
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

# Define update map function
# This function takes in data from country currently being hovered over by user mouse
@app.callback(
    Output('happiness-map', 'figure'),
    [Input('happiness-map', 'hoverData')]
)
def update_map(hoverData):
    # Plot the choropleth geomap
    fig = go.Figure(go.Choropleth(
        # Use data from CSV for locations, z and text
        locations=cleandata_df['country_name'],
        z=cleandata_df['Happiness Score'],  # Happiness score
        locationmode='country names',
        colorscale='RdYlGn',  # Colour scale to red-yellow-green
        colorbar_title="Happiness Index Score",
        hoverinfo='location+z',  # Hover info set to show country name and happiness score
    ))

    # Update layout configures visual settings of the map
    fig.update_layout(
        title_text='World Happiness Index',
        geo=dict(
            showcoastlines=True,
            showcountries=True,
            showland=True,
            countrycolor='black',  # Country border color
            landcolor='lightgray',  # Land color
            projection_type='natural earth'  # Projection type
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor='rgb(229, 236, 246)',
        plot_bgcolor='rgb(229, 236, 246)',
        font=dict(color='black')
    )

    return fig

# Add input and output component for scattered plot
# Add input and output component for bar chart
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),
     Input(component_id='region_btns', component_property='value')]
)
def update_graph(my_dropdown, selected_regions):
    # print("Selected Dropdown Value:", my_dropdown)  # Add this line to print the dropdown value

    cleandata_dff = cleandata_df

    # Filter data based on selected regions
    if selected_regions:
        cleandata_dff = cleandata_dff[cleandata_dff['region'].isin(selected_regions)]

    scattered_chart = px.scatter(
        data_frame=cleandata_dff,
        x='Happiness Score',
        y=my_dropdown,
        hover_data=['country_name'],
        text="country_name",
        height=550
    )
    return scattered_chart

# Run Dash application when script is run
if __name__ == '__main__':
    app.run_server(debug=True)
