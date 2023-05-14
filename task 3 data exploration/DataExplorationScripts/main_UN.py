import streamlit as st
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static




import io


df = pd.read_csv('../../src/data/UN_pop_projections/UN_city_pop_projections_long.csv')
df.drop(columns=['Unnamed: 0','Region','Country_Code','City_Code','data_sources_UN'],inplace=True)


# Define the function for each page
def page1_function():
    st.subheader("Population development of cities in Selected Country")
    
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

    sns.set_style("whitegrid")
    fig = plt.Figure(figsize=(14,10))
    ax = fig.subplots()
    sns.lineplot(x='year', y='population', hue='City', data=df_top_10, ax=ax)

    ax.set_title('Population development of cities in Country')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')

    st.pyplot(fig)
    
    


        

def page2_function():
    st.write("City Population - UN predictions vs model predictions")

    filter_city_list = df['City'].unique()
    filter_city = st.multiselect("Select city", filter_city_list)


    # second 
    df_pred = pd.read_csv('../DataExplorationScripts/combined_dataset.csv')
    df_pred = df_pred.filter(regex=r'^(?!.*_UN_prediction)' )
    years = df_pred.year.unique()
    new_columns = [col.replace('_prediction', '') for col in df_pred.columns]
    df_pred.columns = new_columns
    df_pred = pd.melt(df_pred, id_vars=['year'], var_name='City', value_name='population')
    df_pred.rename(columns={'population':'population_pred'},inplace=True)
    df_pred.set_index(['year', 'City'], inplace=True)


    df_city_pop = df[['year','City','population']]
    df_city_pop = df_city_pop[df_city_pop['year'].isin(years ) ]
    df_city_pop.set_index(['year', 'City'], inplace=True) 
    #len(df_city_pop.City.unique())

    merged_df = df_city_pop.merge(df_pred, left_index=True, right_index=True)
    merged_df.reset_index(inplace=True)


    plt.figure(figsize=(15,6))
    
    city_data = merged_df[merged_df['City'].isin(filter_city)] 

    fig = plt.Figure(figsize=(14,10))
    ax = fig.subplots()

    sns.lineplot(data=city_data, x='year', y='population', label='UN Predictions' , ax = ax)
    sns.lineplot(data=city_data, x='year', y='population_pred', label='Model Predictions', ax = ax)

    st.pyplot(fig)

def page3_function():
    st.write("Top 10 cities by population for 2035")

    top_cities = df[df['year']==2035].groupby(['City'])['population'].sum().nlargest(10)
    top_cities = top_cities.sort_values(ascending=False)

    fig = plt.figure(figsize=(15,8))
    ax = fig.subplots()
    sns.barplot(x=top_cities.values, y=top_cities.index, ax=ax)

    ax.set_xlabel('Population')
    ax.set_ylabel('City') 
    ax.set_title('Top 10 cities by population')

    st.pyplot(fig)

def page4_function():
    
    years = df['year'].unique()
    
    years.sort()

    # Sidebar filter for year
    selected_year = st.sidebar.selectbox("Select year", years)

    # Filter data for selected year 
    df_selected = df[df['year'] == selected_year]
    
    # Create map
    m = folium.Map(location=[28.0339, 1.6596], zoom_start=4)

    # Create a MarkerCluster object 
    marker_cluster = MarkerCluster().add_to(m)

    # Loop through the dataframe and add markers to the map
    for index, row in df_selected.iterrows():
        # Create a popup message 
        popup_message = f"{row['City']}, Population: {row['population']}"
            
        # Create a circle marker and add it to the marker cluster
        folium.CircleMarker(location=[row['Latitude'], row['Longitude']],
                            radius=np.sqrt(row['population']),
                            popup=popup_message,
                            fill=True,
                            fill_opacity=0.7,
                            color='blue').add_to(marker_cluster)

    # Display the map
    folium_static(m)    


pages = {
    "Population development": page1_function,
    "City Population": page2_function,
    "Top 10 cities by populatio": page3_function , 
    "Map": page4_function
}

# Create a sidebar with radio buttons for each page
selection = st.sidebar.selectbox("Go to", list(pages.keys()))

# Call the appropriate page function based on the user's selection
pages[selection]()

















