# Project3Group7

## Overview

We aim to analyze the happiness index of each country and its correlation with various socio-economic indicators. Happiness is a crucial measure of societal well-being, and understanding its relationship with factors such as GDP, life expectancy, health expenses etc, can provide valuable insights into the best path towards societal happiness.

To navigate through this vast data landscape, we've leaned on three types of visual tools: geomaps, spider charts, and scatter plots. Geomaps help us visualize happiness across the globe, spotlighting trends and outliers. Spider charts allow us to compare how various factors contribute to happiness within individual countries, while scatter plots give us insight into the relationships between these factors, helping us pinpoint what impacts happiness most significantly.

The datasets for our analysis are the World Happiness Report 2021 which reviews the state of happiness in the world, and the Global Country Information Dataset 2023 which tracks various metrics of different countries.

In preparing the data for our global happiness project, we started with Python to import and clean our dataset, ensuring we worked with a dataset which had complete information.
After cleaning, we mapped our tables using Quick DBD, then structured our database in PostgreSQL. This allowed us to join our three datasets into one.

We approached this project using Dash which is a Python framework that allows us to create visualisations just using Python.
Dash allowed us to use its pre-built components to handle our HTML porting that drives the visualisations. Dash also follows a reactive programming paradigm, which means we did not have to code in any checks to see if the user had selected different data or had interacted with the visualisation, as Dash will automatically update the visualisations based on changes the user has made.

## Instructions

Before running the MergedDash.py script, ensure that you have all required packages installed with this command run in your command-line interface:

    pip install pandas plotly dash dash-bootstrap-components dash-bootstrap-templates

Once these packages are installed, the mainscript which named "MergedDash.py" can be run with the command 'python MergedDash.py'

This will launch the Dash application and your terminal will respond with "Dash is running on http://xx/". xx is the address and port number of the Dash application.

The visualisation can be run using Google Chrome, pasting the URL into the browser.

## Ethical Considerations

Privacy - We have chosen a dataset in which there is no personal data presented as to not breach the privacy of participants partaking in the survey. The Gallup World Poll has taken great care to obtain consent from participants of the survey. Thus, we have ensured that the data is anonymised and aggregated appropriately to prevent identification of individuals.

Subjectivity - We have considered the potential for our dataset to be biased due to the methods with which happiness is measured and the subjectivity of happiness itself in different cultures. Instead of imposing a singular definition of happiness, the World Happiness Report uses an individualistic approach to determining happiness set by the participants themselves. This helps account for cultural nuances and aims to present a nuanced understanding of happiness that transcends cultural boundaries.

"We use observed data on the six variables and estimates of their associations with life evaluations to explain the variation across countries. They include GDP per capita, social support, healthy life expectancy, freedom, generosity, and corruption. Our happiness rankings are not based on any index of these six factors – the scores are instead based on individuals’ own assessments of their lives... Life evaluations from the Gallup World Poll provide the basis for the annual happiness rankings. They are based on answers to the main life evaluation question. The Cantril Ladder asks respondents to think of a ladder, with the best possible life for them being a 10 and the worst possible life being a 0. They are then asked to rate their own current lives on that 0 to 10 scale. The rankings are from nationally representative samples over three years." - https://worldhappiness.report/about/

Bias/Representativeness - It is important to determine if our dataset is derived from survey numbers large enough to provide an accurate estimate of overall population happiness in each country where participants were surveyed. In this case, the World Happiness Report boasts 95% confience intervals for its data (https://worldhappiness.report/faq/).

## Data Sources

https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021

https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023

https://www.kaggle.com/datasets/andradaolteanu/country-mapping-iso-continent-region
