import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import json


'''
# Environmental Monitoring Dashboard
'''

api_key = st.secrets['api_key']
url_city = 'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'
url_air = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'

air_comp_qualitative = pd.DataFrame({'Qualitative Name':['Good','Fair','Moderate','Poor','Very Poor'],'Index':[1,2,3,4,5],
              'so2':[20,80,250,350,1000],'no2':[40,70,150,200,1000],'pm10':[20,50,100,200,1000],
              'pm2_5':[10,25,50,75,500],'o3':[60,100,140,180,500],'co':[4400,9400,12400,15400,100000]})

name_or_geo = st.selectbox("Would you prefer the air quality for a city or lat/lon?",
                            ('City','Lat/Lon'))
if name_or_geo == 'City':
    city = st.text_input("City Name",'Nairobi')
else:
    lat = st.number_input("Latitude in decimal degrees", -1.2833300)
    lon = st.number_input("Longitude in decimal degrees", 36.8166700)

'''
## Once you have set the inputs above, click the button below to recieve air quality.
'''
aqi_dict = {1:'Good',2:'Fair',3:'Moderate',4:'Poor',5:'Very Poor'}

if st.button("Air Quality"):
    if name_or_geo == 'City':
        response_city = requests.get(url_city.format(city=city,api_key=api_key))
        if response_city.status_code == requests.codes.ok:
            lat = response_city.json()[0]['lat']
            lon = response_city.json()[0]['lon']
        else:
            st.error("Error:",response_city.status_code, response_city.text)
    response_air = requests.get(url_air.format(lat=lat,lon=lon,api_key=api_key))
    if response_air.status_code == requests.codes.ok:
        response_dict = json.loads(response_air.text)
        aqi_overall = response_dict['list'][0]['main']['aqi']
        quality_comp = response_dict['list'][0]['components']
        st.sidebar.write(f'The overall Air Quality Index (AQI) is currently at {aqi_overall} which is {aqi_dict[aqi_overall]}.')
        for x in quality_comp:
            value = quality_comp[x]
            if x not in ['no','nh3']:
                if value < air_comp_qualitative[x][0]:
                    st.write(f'The {x} air component is currently {air_comp_qualitative["Qualitative Name"][0]}.')
                elif value < air_comp_qualitative[x][1]:
                    st.write(f'The {x} air component is currently {air_comp_qualitative["Qualitative Name"][1]}.')
                elif value < air_comp_qualitative[x][2]:
                    st.write(f'The {x} air component is currently {air_comp_qualitative["Qualitative Name"][2]}.')
                elif value < air_comp_qualitative[x][3]:
                    st.write(f'The {x} air component is currently {air_comp_qualitative["Qualitative Name"][3]}.')
                else:
                    st.write(f'The {x} air component is currently {air_comp_qualitative["Qualitative Name"][4]}.')

        '''
        ## Look to add a chart with possibly plotly here that shows the components and highlight the moderate, poor and very poor responses that contribute to low air quality, then remove this.
        '''

    else:
        st.error("Error:",response_air.status_code, response_air.text)
        
        
        
        
    
