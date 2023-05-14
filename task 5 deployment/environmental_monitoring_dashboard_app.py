import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import json
import plotly.express as px


'''
# Environmental Monitoring Dashboard
'''

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

'''
### Once you have set the inputs above, click the button below to recieve air quality.
'''
aqi_dict = {1: 'Good', 2: 'Fair', 3: 'Moderate', 4: 'Poor', 5: 'Very Poor'}

if st.button("Confirm"):
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
            f'The overall Air Quality Index (AQI) is currently at {aqi_overall} which is {aqi_dict[aqi_overall]}.')
        pollutatns = []
        values = []
        quality = []
        for x in quality_comp:
            value = quality_comp[x]
            if x not in ['no', 'nh3']:
                if value < air_comp_qualitative[x][0]:
                    pollutatns.append(x)
                    values.append(air_comp_qualitative[x][0])
                    quality.append(air_comp_qualitative["Qualitative Name"][0])

                elif value < air_comp_qualitative[x][1]:
                    pollutatns.append(x)
                    values.append(air_comp_qualitative[x][0])
                    quality.append(air_comp_qualitative["Qualitative Name"][1])
                elif value < air_comp_qualitative[x][2]:
                    pollutatns.append(x)
                    values.append(air_comp_qualitative[x][0])
                    quality.append(air_comp_qualitative["Qualitative Name"][2])
                elif value < air_comp_qualitative[x][3]:
                    pollutatns.append(x)
                    values.append(air_comp_qualitative[x][0])
                    quality.append(air_comp_qualitative["Qualitative Name"][3])
                else:
                    pollutatns.append(x)
                    values.append(air_comp_qualitative[x][0])
                    quality.append(air_comp_qualitative["Qualitative Name"][4])

        quality_comp_dict = {'Pollutant': pollutatns,
                             'Concentration': values, 'Quality': quality}
        quality_comp_df = pd.DataFrame.from_dict(quality_comp_dict)
        colors = {'good': 'green', 'Poor': 'red', 'Fair': 'orange',
                  'Very Poor': 'magma', 'Moderate': 'yellow'}
        fig = px.bar(quality_comp_df, facet_col='Pollutant', y='Concentration',
                     color='Quality',
                     color_discrete_map=colors, facet_col_spacing=0.05)
        fig.update_xaxes(matches=None, showticklabels=False)
        fig.update_yaxes(matches=None, showticklabels=True)
        fig.layout.xaxis.title.text = 'CO'
        fig.layout.xaxis2.title.text = 'NO2'
        fig.layout.xaxis3.title.text = 'O3'
        fig.layout.xaxis4.title.text = 'SO2'
        fig.layout.xaxis5.title.text = 'PM2.5'
        fig.layout.xaxis6.title.text = 'PM10'
        fig.layout.yaxis.range = (0, 15400)
        fig.layout.yaxis2.range = (0, 200)
        fig.layout.yaxis3.range = (0, 180)
        fig.layout.yaxis4.range = (0, 350)
        fig.layout.yaxis5.range = (0, 75)
        fig.layout.yaxis6.range = (0, 200)
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("Error:", response_air.status_code, response_air.text)
