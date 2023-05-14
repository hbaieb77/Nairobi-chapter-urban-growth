import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px


import io


df = pd.read_csv('UN_city_pop_projections_long.csv')
df.drop(columns=['Unnamed: 0','Region','Country_Code','City_Code','data_sources_UN'],inplace=True)


# Define the function for each page
def page1_function():
    st.subheader("UN City Population Predictions")
    st.markdown("_This plot shows the predicted population of different African cities from 1950 to 2035. The data from 2019 to 2035 are UN future predictions (that were made in 2018). The data from 1950 to 2018 is based on census data. The data from years that did not have a census is interpolated from the census years i.e. a smooth curve is fitted between the years when a census took place._")
    

    # filter_country_list=df['Country_or_area'].unique()
    # filter_country=st.multiselect("Select Country",filter_country_list)

    filter_country_list = df['Country_or_area'].unique()
    filter_country = st.multiselect("Select Country", filter_country_list)

    if filter_country:
        filter_city_list = df[df['Country_or_area'].isin(filter_country)]['City'].unique()
        filter_city = st.multiselect("Select City", filter_city_list)
    else:
        filter_city = []
    
    df_country = df[df['Country_or_area'].isin(filter_country) ]
    

    df_grouped = df_country.groupby(['City', 'year'])[['population']].sum().reset_index()
    df_grouped = df_grouped[df_grouped['City'].isin(filter_city)]
    df_top_10 = df_grouped.sort_values(by=['year', 'population'], ascending=False).groupby('year').head(10)

    labels = {'year':'Year', 'population':'Predicted Population'}
    fig = px.line(df_top_10, x='year', y='population', color='City', labels = labels)
    st.plotly_chart(fig)
    st.subheader("Data Sources")
    st.markdown("- UN City Population Predictions taken from 2018 Revision of World Urbanization Prospects (https://population.un.org/wup/)")
    


        

def page2_function():
    st.subheader("City Population - UN predictions vs model predictions")
    st.markdown("_This visualization compares the population predictions made by the United Nations (UN) with model predictions. It showcases the population trends of cities in the selected country and provides insights into the accuracy of the UN predictions compared to a model-based approach._")

    filter_country_list = df['City'].unique()
    filter_country = st.selectbox("Select City", filter_country_list)


    # second 
    df_pred = pd.read_csv('combined_dataset.csv')
    df_pred = df_pred.filter(regex=r'^(?!.*_UN_prediction)')
    years = df_pred.year.unique()
    new_columns = [col.replace('_prediction', '') for col in df_pred.columns]
    df_pred.columns = new_columns
    df_pred = pd.melt(df_pred, id_vars=['year'], var_name='City', value_name='population')
    df_pred.rename(columns={'population': 'population_pred'}, inplace=True)
    df_pred.set_index(['year', 'City'], inplace=True)

    df_city_pop = df[['year', 'City', 'population']]
    df_city_pop = df_city_pop[df_city_pop['year'].isin(years)]
    df_city_pop.set_index(['year', 'City'], inplace=True)

    merged_df = df_city_pop.merge(df_pred, left_index=True, right_index=True)
    merged_df.reset_index(inplace=True)

    # Plotting

    #city_data = merged_df[merged_df['City'].isin(filter_country)]
    city_data = merged_df[merged_df['City'].isin([filter_country])]

    fig = px.line(city_data, x='year', y=['population', 'population_pred'],
                  labels={'value': 'Population', 'variable': 'Prediction Type'},
                  color_discrete_sequence=['#1f77b4', '#ff7f0e'])

    fig.update_layout(title="Comparison of UN City Population Prediction to Simple ARIMA Prediction",
                      xaxis_title="Year", yaxis_title="Population")

    st.plotly_chart(fig)
    st.subheader("Data Sources")
    st.markdown("- UN City Population Predictions taken from 2018 Revision of World Urbanization Prospects (https://population.un.org/wup/)")

def page3_function():
    st.subheader("Top 10 cities by population for 2035")
    st.markdown("_This visualization showcases the top 10 cities with the highest projected populations for the year 2035. It provides insights into the cities that are expected to experience significant population growth and become major urban centers in the future._")

    top_cities = df[df['year']==2035].groupby(['City'])['population'].sum().nlargest(10)
    top_cities = top_cities.sort_values(ascending=False)

    fig = px.bar(
    data_frame=top_cities,
    x=top_cities.values,
    y=top_cities.index,
    orientation='h',
    labels={'x': 'Population', 'y': 'City'})

    st.plotly_chart(fig)
    st.subheader("Data Sources")
    st.markdown("- UN City Population Predictions taken from 2018 Revision of World Urbanization Prospects (https://population.un.org/wup/)")

def page4_function():
    st.subheader("City Populations Mapped: ")
    st.markdown("_This visualization displays the locations of cities on a map, along with their respective populations. It provides a geographical representation of cities and allows for a visual understanding of population distribution across different regions._")

    fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', 
                        size = 'population', animation_frame = 'year',
                        hover_name='City', mapbox_style = 'open-street-map',
                        zoom=1.6, height = 600, color_discrete_sequence=['red'])   
    st.plotly_chart(fig) 



    st.subheader("Data Sources")
    st.markdown("- UN City Population Predictions taken from 2018 Revision of World Urbanization Prospects (https://population.un.org/wup/)")
pages = {
    "UN City Population Predictions": page1_function,
    "UN predictions compared to ARIMA": page2_function,
    "Top 10 Largest Cities 2035": page3_function , 
    "Cities Mapped": page4_function
}

# Create a sidebar with radio buttons for each page
selection = st.selectbox("Select population prediction", list(pages.keys()))

# Call the appropriate page function based on the user's selection
pages[selection]()

















