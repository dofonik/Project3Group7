import os
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objs as go

#Set path to input CSV file based on current directory
current_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(current_dir, 'output', 'joined_data.csv')

#Read in cleaned data from CSV
data = pd.read_csv(csv_file_path)

#Set up Dash application environment
app = dash.Dash(__name__)

#Define Dash HTML layout
app.layout = html.Div([
    dcc.Graph(id='happiness-map')
])

#Use Dash decorator function to define the callback function
#This allows us to update the visualisation with mouse hover over popups
@app.callback(
    Output('happiness-map', 'figure'),
    [Input('happiness-map', 'hoverData')]
)

#Define update map function
#This function takes in data from country currently being hovered over by user mouse
def update_map(hoverData):
    #Plot the choropleth geomap
    fig = go.Figure(go.Choropleth(
        #Use data from CSV for locations, z and text
        locations=data['country_name'],
        z=data['Happiness Score'], #Happiness score
        locationmode='country names',
        colorscale='RdYlGn',  #Colour scale to red-yellow-green
        colorbar_title="Happiness Index Score",
        hoverinfo='location+z', #Hover info set to show country name and happiness score
    ))

    #Update layout configures visual settings of the map
    fig.update_layout(
        title_text='World Happiness Index',
        geo=dict(
            showcoastlines=True,
            showcountries=True,
            showland=True,
            countrycolor='black',  #Country border color
            landcolor='lightgray',  #Land color
            projection_type='natural earth'  #Projection type
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor='rgb(229, 236, 246)',
        plot_bgcolor='rgb(229, 236, 246)',
        font=dict(color='black')
    )

    return fig

#Run Dash application when script is run
if __name__ == '__main__':
    app.run_server()
