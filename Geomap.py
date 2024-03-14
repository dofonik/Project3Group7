import os
import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Define the path to the CSV file
csv_file_path = os.path.join(current_dir, 'output', 'joined_data.csv')

# Read the CSV file
data = pd.read_csv(csv_file_path)

# Create Dash application
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Graph(id='happiness-map')
])

# Callback to update map
@app.callback(
    dash.dependencies.Output('happiness-map', 'figure'),
    [dash.dependencies.Input('happiness-map', 'hoverData')]
)
def update_map(hoverData):
    # Plot geo map
    fig = go.Figure(go.Choropleth(
        locations=data['country_name'],
        z=data['Happiness Score'],
        locationmode='country names',
        colorscale='Viridis',
        colorbar_title="Happiness Index",
        hoverinfo='location+z',
        text=data['country_name'] + '<br>Happiness Score: ' + data['Happiness Score'].astype(str),
    ))

    fig.update_layout(
        title_text='World Happiness Index',
        geo=dict(
            showcoastlines=True,
        )
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
