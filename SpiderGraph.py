import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Reading the CSV file
df = pd.read_csv(r"resources\ranked_dataset.csv")

app = dash.Dash(__name__)

# Preparing dropdown options for the radar chart dimensions
dropdown_options = [{'label': col, 'value': col} for col in df.columns if col != 'country_name']

# Adding a country selection dropdown
country_options = [{'label': country, 'value': country} for country in df['country_name'].unique()]

app.layout = html.Div([
    html.Div([
        html.Label('Select Country for Analysis', style={'font-weight': 'bold','font-size': '30px'}),
        dcc.Dropdown(
            id='country-dropdown',
            options=country_options,
            value=[country_options[0]['value']],  # Default value
            multi=True,  # Allow multiple selections
            style={'width': '100%'}  # Adjusted width
        ),
    ], style={'margin-bottom': '20px'}),  # Container for country dropdown
    
    html.Div([
        html.Label('Variables Selection', style={'font-weight': 'bold','font-size': '30px'}),
        html.Div([
            dcc.Dropdown(
                id=f'dropdown-{i}',
                options=dropdown_options,
                value=dropdown_options[i % len(dropdown_options)]['value'],  # Cycle through options if less than 6
                style={'width': '300%', 'margin-bottom': '5px'}  # Adjusted width and spacing
            ) for i in range(6)  # Assuming 6 factors for the radar chart
        ], style={'display': 'inline-block', 'vertical-align': 'top'}),  # Inline-block for alignment
    ], style={'text-align': 'left', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start'}),  # Flex to align items to the start
    
    dcc.Graph(id='radar-chart', style={'height': '800px'})  # Increased height for the graph
], style={'width': '100%', 'max-width': '1200px', 'margin': '0 auto'})  # Adjust overall layout width and centering

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
    filtered_df = df[df['country_name'].isin(selected_countries)]
    
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
        showlegend=True
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
