# import dependencies
import os
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from dash_bootstrap_templates import load_figure_template

# Set path to input CSV files based on current directory
current_dir = os.path.dirname(__file__)
csv_file_path_1 = os.path.join(current_dir, 'output', 'joined_data.csv')
csv_file_path_2 = os.path.join(current_dir, 'resources', 'regionaldata.csv')
csv_file_path_3 = os.path.join(current_dir, 'resources', 'ranked_dataset.csv')

# Read in cleaned data from CSV
cleandata_df = pd.read_csv(csv_file_path_1)
region_df = pd.read_csv(csv_file_path_2)
radar_df = pd.read_csv(csv_file_path_3)

# Merge the two DataFrames together based on the alpha-3 column they share
cleandata_df = pd.merge(cleandata_df, region_df[['country_name', 'region']], on="country_name")

# Load the figure template
load_figure_template("plotly_dark")

# Set up Dash application environment
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Define Dash HTML layout
<<<<<<< HEAD
app.layout = dbc.Container(fluid=True, children=[
=======
app.layout = html.Div(style={'backgroundColor': background_color, 'padding': '20px'}, children=[
    # Happiness Map
    html.Div([
        html.H2("Happiness Map"),
        dcc.Graph(id='happiness-map')
    ], className='twelve columns', style={'margin-bottom': '20px', 'padding': '20px', 'border': '1px solid #ccc'}),  # Make the map occupy twelve columns

    # Divider
    html.Hr(),
>>>>>>> bfd511d48da074f457873ff794bd732acd1d04ff

    # add Main Title
    html.Div([
<<<<<<< HEAD
        html.H1("World Happiness Analysis", style={'textAlign': 'center', 'color': 'white'})
    ], style={'margin-bottom': '20px'}),

    # Row for Happiness Map
    dbc.Row([
        # Col for Happiness Map
        dbc.Col([
            dcc.Graph(id='happiness-map', style={'height': '500px'})  # Adjusted height
        ], width=12, style={'margin-bottom': '20px'})  # Adjusted width and margin bottom
    ]),

    # Add Dropdown layout, Region selection layout, and Graph layout
    dbc.Row([
        # Col for Dropdown layout and Region selection layout
        dbc.Col([
            html.Label(["Factors affecting Happiness Index"],style={'color':'white','font-weight': 'bold', 'font-size': '15px'}),
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
                        optionHeight=45,  # height between dropdown options
                        disabled=False,
                        multi=False,  # allow multiple selection
                        searchable=True,
                        placeholder='Please select...',
                        clearable=True,
                        style={'width': "100%", 'marginBottom': '35px'},
                        className='select_box',
                        persistence=True,
                        persistence_type='memory'
                        ),
            html.Label("Select Regions", style={'font-weight': 'bold', 'font-size': '20px'}),
            dcc.Checklist(id='region_btns',
                        options=[{'label': region, 'value': region} for region in cleandata_df['region'].unique()],
                        value=[],
                        inline=True)
        ], width=4),  # Adjusted width
        
      
        # Col for Graph layout (right side)
        dbc.Col([
            dcc.Graph(id='the_graph', style={'height': '550px'})  # Adjusted height
        ], width=8, style={'backgroundColor': 'transparent', 'padding': '20px', 'border': '2px solid black'})  # Adjusted width and added styling
    ], style={'margin-bottom': '20px'}),  # Adjusted margin bottom

    # Row for Radar Chart
    dbc.Row([
        # Col for Dropdowns layout (left side)
        dbc.Col([
=======
        html.H2("Factors Affecting Happiness Index"),
        dcc.Dropdown(id='my_dropdown',
                     options=[
                         {'label': 'GDP', 'value': 'GDP'},
                         {'label': 'Infant Mortality', 'value': 'Infant mortality'},
                         {'label': 'Life Expectancy', 'value': 'Life expectancy'},
                         {'label': 'Maternal Mortality Ratio', 'value': 'Maternal mortality ratio'},
                         {'label': 'Minimum Wage', 'value': 'Minimum wage'},
                         {'label': 'Out of Pocket Health Expenditure', 'value': 'Out of pocket health expenditure'},
                         {'label': 'Physicians per Thousand', 'value': 'Physicians per thousand'},
                         {'label': 'Population', 'value': 'Population'},
                         {'label': 'Unemployment Rate', 'value': 'Unemployment rate'},
                         {'label': 'Social Support', 'value': 'Social support'},
                         {'label': 'Freedom to Make Life Choices', 'value': 'Freedom to make life choices'},
                         {'label': 'Generosity', 'value': 'Generosity'},
                         {'label': 'Perceptions of Corruption', 'value': 'Perceptions of corruption'}
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
    ], className='three columns', style={'margin-bottom': '20px', 'padding': '20px', 'border': '1px solid #ccc'}),  # Make the dropdown occupy three columns

    # Divider
    html.Hr(),

    # Checkbox for regions
    html.Div([
        html.H2("Select Regions"),
        dcc.Checklist(id='region_btns',
                      options=[{'label': region, 'value': region} for region in cleandata_df['region'].unique()],
                      value=[],
                      inline=True),
    ], style={'margin-bottom': '20px', 'padding': '20px', 'border': '1px solid #ccc'}),

    # Divider
    html.Hr(),

    # Scatter plot
    html.Div([
        html.H2("Scatter Plot"),
        dcc.Graph(id='the_graph')
    ], style={'margin-bottom': '20px', 'padding': '20px', 'border': '1px solid #ccc'}),

    # Divider
    html.Hr(),

    # Radar Chart
    html.Div([
        html.H2("Radar Chart"),
        html.Div([
            html.Label('Select Country for Analysis', style={'font-weight': 'bold', 'font-size': '20px'}),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in radar_df['country_name'].unique()],
                value=[radar_df['country_name'].unique()[0]],  # Default value
                multi=True,  # Allow multiple selections
                style={'width': '100%'}  # Adjusted width
            ),
        ], style={'margin-bottom': '20px'}),  # Container for country dropdown

        html.Div([
            html.Label('Variables Selection', style={'font-weight': 'bold', 'font-size': '20px'}),
>>>>>>> bfd511d48da074f457873ff794bd732acd1d04ff
            html.Div([
                html.Label('Select Country for Analysis', style={'color':'white','font-weight': 'bold', 'font-size': '20px'}),
                dcc.Dropdown(
<<<<<<< HEAD
                    id='country-dropdown',
                    options=[{'label': country, 'value': country} for country in radar_df['country_name'].unique()],
                    value=[radar_df['country_name'].unique()[0]],  # Default value
                    multi=True,  # Allow multiple selections
                    style={'width': '99%'}  # Adjusted width
                ),
            ], style={'margin-bottom': '20px'}),  # Adjusted margin bottom

            html.Div([
                html.Label('Variables Selection', style={'font-weight': 'bold', 'font-size': '20px'}),
                html.Div([
                    dcc.Dropdown(
                        id=f'dropdown-{i}',
                        options=[{'label': col, 'value': col} for col in radar_df.columns if col != 'country_name'],
                        value=[col for col in radar_df.columns if col != 'country_name'][i % 6],  # Cycle through options if less than 6
                        style={'width': '225%', 'margin-bottom': '5px'}  # Adjusted width and spacing
                    ) for i in range(6)  # Assuming 6 factors for the radar chart
                ], style={'display': 'inline-block', 'vertical-align': 'top'}),  # Inline-block for alignment
            ], style={'text-align': 'left', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),  # Flex to align items to the start
        ], width=4),  # Adjusted width

        
        # Col for Radar Chart (right side)
        dbc.Col([
            dcc.Graph(id='radar-chart', style={'height': '500px'})  # Adjusted height for the graph
        ], width=7, style={'backgroundColor': 'transparent', 'padding': '20px', 'border': '2px solid black'})  # Adjusted width and added styling
    ])
=======
                    id=f'dropdown-{i}',
                    options=[{'label': col, 'value': col} for col in radar_df.columns if col != 'country_name'],
                    value=[col for col in radar_df.columns if col != 'country_name'][i % 6],  # Cycle through options if less than 6
                    style={'width': '300%', 'margin-bottom': '5px'}  # Adjusted width and spacing
                ) for i in range(6)  # Assuming 6 factors for the radar chart
            ], style={'display': 'inline-block', 'vertical-align': 'top'}),  # Inline-block for alignment
        ], style={'text-align': 'left', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),  # Flex to align items to the start

        dcc.Graph(id='radar-chart', style={'height': '800px'})  # Increased height for the graph
    ], style={'margin-bottom': '20px', 'padding': '20px', 'border': '1px solid #ccc'})  # Adjust overall layout width and centering
>>>>>>> bfd511d48da074f457873ff794bd732acd1d04ff
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
        font=dict(color='white')  # Text color set to white
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
        color= 'region',
        size='Happiness Score',
        hover_data=['country_name'],
        text="country_name",
        height=550
    )
    # Update legend position and title
    scattered_chart.update_layout(legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5))
    # scattered_chart.update_traces(showlegend=True, legendtitle_text="Region") 
   
    return scattered_chart

# Define radar chart callback function
@app.callback(
    Output('radar-chart', 'figure'),
    [Input(f'dropdown-{i}', 'value') for i in range(6)] +
    [Input('country-dropdown', 'value')]
)
def update_radar_chart(*args):
    # Last argument is the list of selected countries
    categories = list(args[:-1])
    selected_countries = args[-1]
    
    # Filter DataFrame for selected countries
    filtered_df = radar_df[radar_df['country_name'].isin(selected_countries)]
    
    # Prepare data for radar chart
    radar_data = []
    for country in filtered_df['country_name'].unique():
        country_data = filtered_df[filtered_df['country_name'] == country]
        radar_data.append(go.Scatterpolar(
            r=[country_data[category].values[0] for category in categories],
            theta=categories,
            fill='toself',
            name=country
        ))
    
    fig = go.Figure(radar_data)
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, filtered_df[categories].max().max()]
            )
        ),
        showlegend=True,
        font=dict(color='white'),  # Text color set to white
        paper_bgcolor='rgba(0,0,0,0)'  # Transparent background
    )
    
    return fig

# Run Dash application when script is run
if __name__ == '__main__':
    app.run_server(debug=True)
