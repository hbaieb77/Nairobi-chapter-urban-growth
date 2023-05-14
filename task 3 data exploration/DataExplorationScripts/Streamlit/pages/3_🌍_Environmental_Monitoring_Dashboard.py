import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import json
import plotly.express as px


'''
# Environmental Monitoring Dashboard
'''
st.markdown('Get real time air quality data anywhere in the world by providing a **city name** or **latitude / longitude** coordinate below.<br><br>We provide a basic Air Quality Index and a breakdown of the levels of polluting gases, such as Carbon monoxide (CO), Nitrogen monoxide (NO), Nitrogen dioxide (NO<sub>2</sub>), Ozone (O<sub>3</sub>), Sulphur dioxide (SO<sub>2</sub>), Ammonia (NH<sub>3</sub>), and particulates (PM<sub>2.5</sub> and PM<sub>10</sub>). This dashboard is powered by <a href="https://openweathermap.org/api">openweathermap</a>.', unsafe_allow_html=True)

api_key = st.secrets['api_key']
url_city = 'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'
url_air = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'

air_comp_qualitative = pd.DataFrame({'Qualitative Name': ['Good', 'Fair', 'Moderate', 'Poor', 'Very Poor'], 'Index': [1, 2, 3, 4, 5],
                                     'so2': [20, 80, 250, 350, 1000], 'no2': [40, 70, 150, 200, 1000], 'pm10': [20, 50, 100, 200, 1000],
                                     'pm2_5': [10, 25, 50, 75, 500], 'o3': [60, 100, 140, 180, 500], 'co': [4400, 9400, 12400, 15400, 100000]})

name_or_geo = st.selectbox("Would you prefer the air quality for a city or lat/lon?",
                           ('City', 'Lat/Lon'))
if name_or_geo == 'City':
    city = st.text_input("City Name", 'Nairobi')
else:
    lat = st.number_input("Latitude in decimal degrees", -1.2833300)
    lon = st.number_input("Longitude in decimal degrees", 36.8166700)

aqi_dict = {1: 'Good', 2: 'Fair', 3: 'Moderate', 4: 'Poor', 5: 'Very Poor'}

if st.button("Click To Get Air Quality"):
    if name_or_geo == 'City':
        response_city = requests.get(
            url_city.format(city=city, api_key=api_key))
        if response_city.status_code == requests.codes.ok:
            lat = response_city.json()[0]['lat']
            lon = response_city.json()[0]['lon']
        else:
            st.error("Error:", response_city.status_code, response_city.text)
    response_air = requests.get(url_air.format(
        lat=lat, lon=lon, api_key=api_key))
    if response_air.status_code == requests.codes.ok:
        response_dict = json.loads(response_air.text)
        aqi_overall = response_dict['list'][0]['main']['aqi']
        quality_comp = response_dict['list'][0]['components']
        st.write(
            f'Overall Air Quality Index (AQI) is **{aqi_overall}** which is **{aqi_dict[aqi_overall]}**')
        pollutatns = []
        values = []
        quality = []
        for x in quality_comp:
            value = quality_comp[x]
            if x not in ['no', 'nh3']:
                if value < air_comp_qualitative[x][0]:
                    pollutatns.append(x)
                    values.append(value)
                    quality.append(air_comp_qualitative["Qualitative Name"][0])

                elif value < air_comp_qualitative[x][1]:
                    pollutatns.append(x)
                    values.append(value)
                    quality.append(air_comp_qualitative["Qualitative Name"][1])
                elif value < air_comp_qualitative[x][2]:
                    pollutatns.append(x)
                    values.append(value)
                    quality.append(air_comp_qualitative["Qualitative Name"][2])
                elif value < air_comp_qualitative[x][3]:
                    pollutatns.append(x)
                    values.append(value)
                    quality.append(air_comp_qualitative["Qualitative Name"][3])
                else:
                    pollutatns.append(x)
                    values.append(value)
                    quality.append(air_comp_qualitative["Qualitative Name"][4])

        quality_comp_dict = {'Pollutant': pollutatns,
                             'Concentration': values, 'Quality': quality}
        quality_comp_df = pd.DataFrame.from_dict(quality_comp_dict)
        colors = {'Good': 'green', 'Poor': 'crimson', 'Fair': 'orange',
                  'Very Poor': 'red', 'Moderate': 'yellow'}
        labels = {'Concentration':'Concentration (μg/m<sup>3</sup>)'}
        order = {'Quality':['Good', 'Fair', 'Moderate', 'Poor', 'Very Poor']}
        fig = px.bar(quality_comp_df, facet_col='Pollutant', y='Concentration', category_orders = order,
                     color='Quality', labels = labels,
                     color_discrete_map=colors, facet_col_spacing=0.05)
        fig.update_xaxes(matches=None, showticklabels=False)
        fig.update_yaxes(matches=None, showticklabels=True)
        fig.layout.xaxis.title.text = 'CO'
        fig.layout.xaxis2.title.text = 'NO2'
        fig.layout.xaxis3.title.text = 'O3'
        fig.layout.xaxis4.title.text = 'SO2'
        fig.layout.xaxis5.title.text = 'PM2.5'
        fig.layout.xaxis6.title.text = 'PM10'
        fig.layout.yaxis.range = (0, 17000)
        fig.layout.yaxis2.range = (0, 220)
        fig.layout.yaxis3.range = (0, 200)
        fig.layout.yaxis4.range = (0, 385)
        fig.layout.yaxis5.range = (0, 85)
        fig.layout.yaxis6.range = (0, 220)
        
        for annotation in fig.layout.annotations:
            annotation.text = ''
        st.plotly_chart(fig, use_container_width=True, theme = None)

    else:
        st.error("Error:", response_air.status_code, response_air.text)
