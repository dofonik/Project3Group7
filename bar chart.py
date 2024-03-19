import pandas as pd
import plotly.express as px
import plotly.io as pio

df = pd.read_csv("output/joined_data.csv")
df = df[df['Happiness Score'] == 'World Happiness']
df = df.groupby(['GDP', 'Infant mortality', 'Life expectancy', 'Infant mortality', 'Maternal mortality ratio', 'Minimum wage',  'Out of pocket health expenditure', 'Physicians per thousand', 'Population', 'value', 'Unemployment rate', 'Social support', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'], as_index=False)[['detenues', 'under_trial', 'convicts', 'others', 'Happiness Score']].sum()

barchart = px.bar(
    data_frame=df,
    x=['GDP', 'Infant mortality', 'Life expectancy', 'Infant mortality', 'Maternal mortality ratio', 'Minimum wage', 'Out of pocket health expenditure', 'Physicians per thousand', 'Population', 'value', 'Unemployment rate', 'Social support', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'],
    y="Happiness Score",
    color="country_name",
    opacity=0.9,
    orientation="v",
    barmode='relative',
    labels={
        "Happiness Score": "Happiness Score",
        "x": "Variables",
        "y": "Happiness Score",
        "country_name": "Country",
    },
    title='World Happiness Index',
    width=1400,
    height=720,
    template='gridon',
)

pio.show(barchart)
