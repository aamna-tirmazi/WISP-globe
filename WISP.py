import pandas as pd
import plotly.express as px

df = pd.read_csv("WISP:country.csv")

country_fixes = {
    "Antigua": "Antigua and Barbuda",
    "Bosnia-Herzegovina": "Bosnia and Herzegovina",
    "Czech Republic": "Czechia",
    "Korea": "South Korea",
    "Russia": "Russia",
    "United States": "United States",
    "Vietnam": "Vietnam"
}

df["Country"] = df["Country"].replace(country_fixes)

fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Scholars",
    hover_name="Country",
    hover_data={"Scholars": True},
    color_continuous_scale="Blues",
    range_color=(0, df["Scholars"].max()),
    title="Number of WISP Scholars by Country"
)

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type="natural earth"
    ),
    coloraxis_colorbar=dict(
        title="Number of Scholars"
    )
)

fig.show()