
-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "country_code" (
    "country_name" VARCHAR   NOT NULL,
    "Alpha-2_code" VARCHAR(2)   NOT NULL,
    "Alpha-3_code" VARCHAR(3)   NOT NULL,
    "Numeric" VARCHAR(5)   NOT NULL,
    CONSTRAINT "pk_country_code" PRIMARY KEY (
        "country_name"
     )
);

CREATE TABLE "world-data-2023" (
    "country_name" VARCHAR   NOT NULL,
    "Density" INTEGER   NOT NULL,
    "Abbreviation" VARCHAR(2)   NOT NULL,
    "Agricultural" NUMERIC   NOT NULL,
    "Land_Area(Km2)" INTEGER   NOT NULL,
    "Armed_Forces_size" INTEGER   NOT NULL,
    "Birth_Rate" NUMERIC   NOT NULL,
    "Calling_Code" INTEGER   NOT NULL,
    "Capital/Major_City" VARCHAR(50)   NOT NULL,
    "Co2-Emissions" INTEGER   NOT NULL,
    "CPI" NUMERIC   NOT NULL,
    "CPI_Change(%)" NUMERIC   NOT NULL,
    "Currency-Code" VARCHAR(3)   NOT NULL,
    "Fertility_Rate" NUMERIC   NOT NULL,
    "Forested_Area(%)" NUMERIC   NOT NULL,
    "Gasoline_Price" NUMERIC   NOT NULL,
    "GDP" INTEGER   NOT NULL,
    "Gross_primary_education_enrollment(%)" NUMERIC   NOT NULL,
    "Gross_tertiary_education_enrollment(%)" NUMERIC   NOT NULL,
    "Infant_mortality" NUMERIC   NOT NULL,
    "Largest_city" VARCHAR(50)   NOT NULL,
    "Life_expectancy" NUMERIC   NOT NULL,
    "Maternal_mortality_ratio" INTEGER   NOT NULL,
    "Minimum_wage" NUMERIC   NOT NULL,
    "Official_language" VARCHAR(50)   NOT NULL,
    "Out_of_pocket_health_expenditure" NUMERIC   NOT NULL,
    "Physicians_per_thousand" NUMERIC   NOT NULL,
    "Population" INTEGER   NOT NULL,
    "Population:Labor_force_participation(%)" NUMERIC   NOT NULL,
    "Tax_revenue(%)" NUMERIC   NOT NULL,
    "Total_tax_rate" NUMERIC   NOT NULL,
    "Unemployment_rate" NUMERIC   NOT NULL,
    "Urban_population" INTEGER   NOT NULL,
    "Latitude" NUMERIC   NOT NULL,
    "Longitude" NUMERIC   NOT NULL
);

CREATE TABLE "world-happiness-report-2021" (
    "Country_name" VARCHAR   NOT NULL,
    "Regional_indicator" VARCHAR(50)   NOT NULL,
    "Ladder_score" NUMERIC   NOT NULL,
    "Standard_error_of_ladder_score" NUMERIC   NOT NULL,
    "upperwhisker" NUMERIC   NOT NULL,
    "lowerwhisker" NUMERIC   NOT NULL,
    "Logged_GDP_per_capita" NUMERIC   NOT NULL,
    "Social_support" NUMERIC   NOT NULL,
    "Healthy_life_expectancy" NUMERIC   NOT NULL,
    "Freedom_to_makelifechoices" NUMERIC   NOT NULL,
    "Generosity" NUMERIC   NOT NULL,
    "Perceptions_of_corruption" NUMERIC   NOT NULL,
    "Ladder_score_in_Dystopia" NUMERIC   NOT NULL,
    "Explained_by:Log_GDP_per_capita" NUMERIC   NOT NULL,
    "Explained_by:Social_support" NUMERIC   NOT NULL,
    "Explained_by:Healthy_life_expectancy" NUMERIC   NOT NULL,
    "Explained_by:Freedom_to_make_life_choices" NUMERIC   NOT NULL,
    "Explained_by:Generosity" NUMERIC   NOT NULL,
    "Explained_by:Perceptions_of_corruption" NUMERIC   NOT NULL,
    "Dystopia+residual" NUMERIC   NOT NULL
);

ALTER TABLE "world-data-2023" ADD CONSTRAINT "fk_world-data-2023_country_name" FOREIGN KEY("country_name")
REFERENCES "country_code" ("country_name");

ALTER TABLE "world-happiness-report-2021" ADD CONSTRAINT "fk_world-happiness-report-2021_Country_name" FOREIGN KEY("Country_name")
REFERENCES "country_code" ("country_name");

