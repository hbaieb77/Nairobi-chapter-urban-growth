import streamlit as st
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import io


# functions : 

def null_perc(df) : 
    percent_missing = df.isnull().sum() * 100 / len(df) 
    missing_value_df = pd.DataFrame({
                                    'percent_missing': percent_missing})
    missing_value_df.sort_values('percent_missing', inplace=True , ascending=False)
    #print(missing_value_df)
    return missing_value_df 


st.header("project name") 
data=pd.read_csv("clean.csv")

filter_country_list=data['Country name'].unique()


# data 
st.subheader("Data : ")
st.write(data)

# data info  
st.subheader("Data Info")
buffer = io.StringIO() 
data.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# null values 
st.subheader("Null values : ")
st.write(null_perc(data) )


st.subheader("Pick a Country ") 
filter_country=st.multiselect("Select Country",filter_country_list)

if(filter_country):
    data=data[data['Country name'].isin(filter_country)]

df_urban = data[[ 'Country name', 'Year', 'Aggregation level',
                'Sub-national region name' , 'Number of individual cases in dataset for region' , 
                'Number of households in dataset for region' , '% population in urban areas' 
                ]] 

df_wealth = data[['Country name', 'Year','Mean International Wealth Index (IWI) score of region',
       '% poor households (with IWI value under 70)',
       '% poorer households (with IWI value under 50)',
       '% poorest households (with IWI value under 35)',
       'Gini coefficient wealth inequality', 'Theil-T wealth inequality',
       'Wealth inequality within groups (THeil-T)']]

df_years_edu = data[['Country name', 'Year','Mean years education of adults aged 20+',
       'Mean years education of women aged 20+',
       'Mean years education of men aged 20+',
       'Mean years education of adults aged 25+',
       'Mean years education of women aged 25+',
       'Mean years education of men aged 25+',
       'Mean years education of adults aged 20-39',
       'Mean years education of women aged 20-39', 
       'Mean years education of men aged 20-39',
       'Mean years education of adults aged 40-59',
       'Mean years education of women aged 40-59',
       'Mean years education of men aged 40-59',
       'Mean years education of adults aged 60+',
       'Mean years education of women aged 60+',
       'Mean years education of men aged 60+']]

df_educ = data[['Country name', 'Year',
       'Educational attendance children 6-8',
       'Educational attendance children 9-11',
       'Educational attendance children 12-14',
       'Educational attendance children 15-17',
       'Educational attendance children 18-20',
       'Educational attendance children 21-23',
       'Educational attendance girls 6-8', 
       'Educational attendance girls 9-11',
       'Educational attendance girls 12-14',
       'Educational attendance girls 15-17',
       'Educational attendance girls 18-20',
       'Educational attendance girls 21-23', 
       'Educational attendance boys 6-8',
       'Educational attendance boys 9-11', 
       'Educational attendance boys 12-14',
       'Educational attendance boys 15-17', 
       'Educational attendance boys 18-20', 
       'Educational attendance boys 21-23']]


df_fert = data[['Country name', 'Year','Total Fertility Rate', 'Age-specific fertility rate age 10-14',
       'Age-specific fertility rate age 15-19',
       'Age-specific fertility rate age 20-24',
       'Age-specific fertility rate age 25-29',
       'Age-specific fertility rate age 30-34',  
       'Age-specific fertility rate age 35-39', 
       'Age-specific fertility rate age 40-44',
       'Age-specific fertility rate age 45-49']] 

df_pop = data[['Country name', 'Year','Total area population in millions',
       'Share of population living in area', '% population aged 0-9',
       '% population aged 10-19', '% population aged 20-29',
       '% population aged 30-39', '% population aged 40-49',
       '% population aged 50-59', '% population aged 60-69', 
       '% population aged 70-79', '% population aged 80-89',
       '% population aged 90+', 'Average household size', 'Dependency ratio',
       'Youth dependency ratio', 'Old age dependency ratio',
       'Demographic Window Phase', '% population aged under 15',
       '% population aged 15-65', '% population aged over 65']]

df_mortality = data[['Country name', 'Year','Infant mortality rate', 'Under five mortality rate',
       'Neo-natal mortality rate', 'Post-neonatal mortality rate',
       'Child mortality rate']] 



# df_urban 

st.subheader("Urban population data :  ") 
st.markdown("<h3 style='font-size:18px;'> # Average Number of individual cases in dataset for region throughout the years </h3>", unsafe_allow_html=True)


df_grouped = df_urban.groupby(['Year'])[['Number of individual cases in dataset for region', '% population in urban areas']].mean().reset_index()

# Create the bar chart
fig, ax1 = plt.subplots(figsize=(12,6))
ax1.bar(df_grouped['Year'], df_grouped['Number of individual cases in dataset for region'])
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of individual cases in dataset for region')

ax2 = ax1.twinx()
ax2.plot(df_grouped['Year'], df_grouped['% population in urban areas'], color='red', label='% population in urban areas')
ax2.set_ylabel('% population in urban areas')
ax2.legend()

# Show the plot in Streamlit
st.pyplot(fig)








st.markdown("<h3 style='font-size:18px;'> # Top 20 Countries with Highest Average Number of individual cases in dataset for region :</h3>", unsafe_allow_html=True)

df_top_20 = df_urban.groupby('Country name')[['Number of individual cases in dataset for region']].mean().nlargest(20, 'Number of individual cases in dataset for region').sort_values(ascending=False,by='Number of individual cases in dataset for region').reset_index()
fig, ax = plt.subplots(figsize=(15,8))
ax.bar(df_top_20['Country name'], df_top_20['Number of individual cases in dataset for region'])
ax.set_ylabel('Number of individual cases in dataset for region')
ax.set_xlabel('Country')
plt.xticks(rotation=90)
st.pyplot(fig)



df_top_20 = df_urban.groupby('Country name')[['Number of households in dataset for region','% population in urban areas']].mean().nlargest(20, 'Number of households in dataset for region').sort_values(ascending=False,by='Number of households in dataset for region').reset_index()
fig, ax1 = plt.subplots(figsize=(15,8))
ax2 = ax1.twinx()

ax1.plot(df_top_20['Country name'], df_top_20['Number of households in dataset for region'], color='red', label='Number of households in dataset for region')
ax2.plot(df_top_20['Country name'], df_top_20['% population in urban areas'], color='blue', label='% population in urban areas')
ax1.set_ylabel('Number of households in dataset ')
ax2.set_ylabel('Percentage of population in urban areas')
ax1.set_xlabel('Country')
ax1.tick_params(axis='x', rotation=90)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

st.markdown("<h3 style='font-size:18px;'> # Top 20 countries by number of households in dataset and percentage of population in urban areas :</h3>", unsafe_allow_html=True)
st.pyplot(fig)


# df_urban 

st.subheader("Wealth data : ") 
st.markdown("<h3 style='font-size:18px;'> # Line chart of % poor households (with IWI value under given value ) </h3>", unsafe_allow_html=True)

df_temp = df_wealth.drop(columns=['Mean International Wealth Index (IWI) score of region',
                                  'Gini coefficient wealth inequality',
                                  'Theil-T wealth inequality',
                                  'Wealth inequality within groups (THeil-T)'])

df_melted = pd.melt(df_temp,
                    id_vars=['Country name', 'Year'],
                    value_vars=['% poor households (with IWI value under 70)',
                                '% poorer households (with IWI value under 50)',
                                '% poorest households (with IWI value under 35)'],
                    var_name='variable',
                    value_name='value')

df_mean = df_melted.groupby(['variable', 'Year']).mean().reset_index()

fig, ax = plt.subplots(figsize=(15, 8))
for variable in df_melted['variable'].unique():
    df_variable = df_mean[df_mean['variable'] == variable]
    ax.plot(df_variable['Year'], df_variable['value'], label=variable)

ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.legend()

st.pyplot(fig)



st.markdown("<h3 style='font-size:18px;'> # Average Mean International Wealth Index (IWI) score of region </h3>", unsafe_allow_html=True)
df_top_20 = df_wealth.groupby('Year')[['Mean International Wealth Index (IWI) score of region' , 'Gini coefficient wealth inequality']].mean().reset_index()

fig, ax1 = plt.subplots(figsize=(15,6))

ax1.plot(df_top_20['Year'], df_top_20['Mean International Wealth Index (IWI) score of region'], label='Mean International Wealth Index (IWI) score of region')
ax1.set_ylabel('Mean International Wealth Index (IWI) score of region')
ax1.set_xlabel('Year')

ax2 = ax1.twinx()
ax2.plot(df_top_20['Year'], df_top_20['Gini coefficient wealth inequality'], color='red', label='Gini coefficient wealth inequality')
ax2.set_ylabel('Gini coefficient wealth inequality')

fig.legend()
st.pyplot(fig)



st.markdown("<h3 style='font-size:18px;'> # Correlation between International Wealth Index and Gini coefficient wealth inequality  </h3>", unsafe_allow_html=True)

plt.figure(figsize=(15,8))

sns.scatterplot(data=df_wealth, x='Mean International Wealth Index (IWI) score of region', y='Gini coefficient wealth inequality')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


# df_years_education 

st.subheader("Education data : ") 


df_years_edu_melted = df_years_edu.melt(id_vars=['Country name', 'Year'], 
                    value_vars=['Mean years education of adults aged 20+',
                                'Mean years education of women aged 20+',
                                'Mean years education of men aged 20+',
                                'Mean years education of adults aged 25+',
                                'Mean years education of women aged 25+',
                                'Mean years education of men aged 25+',
                                'Mean years education of adults aged 20-39',
                                'Mean years education of women aged 20-39',
                                'Mean years education of men aged 20-39',
                                'Mean years education of adults aged 40-59',
                                'Mean years education of women aged 40-59',
                                'Mean years education of men aged 40-59',
                                'Mean years education of adults aged 60+',
                                'Mean years education of women aged 60+',
                                'Mean years education of men aged 60+'],
                    var_name='category', value_name='value')

df_years_edu_melted['gender'] = df_years_edu_melted['category'].str.extract('(women|men|adults)')
df_years_edu_melted['age_range'] = df_years_edu_melted['category'].str.extract('(20\+|25\+|20-39|40-59|60\+)')

df_years_edu_melted['age_range'] = df_years_edu_melted['age_range'].str.replace('aged ', '').str.replace('\+', '')
df_years_edu_melted.drop('category', axis=1, inplace=True)


st.markdown("<h3 style='font-size:18px;'> # Line chart of Mean years of education for each age range </h3>", unsafe_allow_html=True)

df_mean = df_years_edu_melted.groupby(['age_range', 'Year']).mean().reset_index()

fig, ax = plt.subplots(figsize=(15, 8))

for age_range in df_years_edu_melted['age_range'].unique():
    df_age_range = df_mean[df_mean['age_range'] == age_range]
    ax.plot(df_age_range['Year'], df_age_range['value'], label=age_range)

ax.set_xlabel('Year') 
ax.set_ylabel('Value')
ax.legend()

# Display the chart
st.pyplot(fig)


st.markdown("<h3 style='font-size:18px;'> # Line chart of Mean years of education for each gender </h3>", unsafe_allow_html=True)

df_mean = df_years_edu_melted.groupby(['gender', 'Year']).mean().reset_index()

fig, ax = plt.subplots(figsize=(15, 8))

for gender in df_years_edu_melted[df_years_edu_melted['gender'] != 'adults']['gender'].unique():
    df_gender = df_mean[df_mean['gender'] == gender]
    ax.plot(df_gender['Year'], df_gender['value'], label=gender)

ax.set_xlabel('Year') 
ax.set_ylabel('Value')
ax.legend()

st.pyplot(fig)


st.markdown("<h3 style='font-size:18px;'> # Top 10 Countries with Highest Average number of years of education </h3>", unsafe_allow_html=True)

df_top_10 = df_years_edu_melted.groupby('Country name')[['value']].mean().nlargest(10, 'value').sort_values(ascending=True,by='value').reset_index()

fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(df_top_10['Country name'], df_top_10['value'])
ax.set_xlabel('Number of years of education')
ax.set_ylabel('Country')


ax2.set_ylim(ax.get_ylim())
ax2.set_yticks(ax.get_yticks())
ax2.set_yticklabels(df_top_10['value'].round(1))

ax2.set_ylabel('Number of years of education')

st.pyplot(fig)



# df_educ 

#st.subheader("Education data : ") 


df_edu_melted = df_educ.melt(id_vars=['Country name', 'Year'], 
                    value_vars=[
        'Educational attendance children 9-11',
       'Educational attendance children 12-14',
       'Educational attendance children 15-17',
       'Educational attendance children 18-20',
       'Educational attendance children 21-23',
       'Educational attendance girls 6-8', 
       'Educational attendance girls 9-11',
       'Educational attendance girls 12-14',
       'Educational attendance girls 15-17',
       'Educational attendance girls 18-20',
       'Educational attendance girls 21-23', 
       'Educational attendance boys 6-8',
       'Educational attendance boys 9-11', 
       'Educational attendance boys 12-14',
       'Educational attendance boys 15-17',  
       'Educational attendance boys 18-20',
       'Educational attendance boys 21-23'],
                    var_name='category', value_name='value')

df_edu_melted['gender'] = df_edu_melted['category'].str.extract('(boys|girls|children)')
df_edu_melted['age_range'] = df_edu_melted['category'].str.extract('(6-8|9-11|12-14|15-17|18-20|21-23)')

df_edu_melted['age_range'] = df_edu_melted['age_range'].str.replace('aged ', '').str.replace('\+', '')

df_edu_melted.drop('category', axis=1, inplace=True)


df_mean = df_edu_melted.groupby(['age_range', 'Year']).mean().reset_index()

st.markdown("<h3 style='font-size:18px;'> # Line chart of Mean years of educational attendance for each age range </h3>", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(15, 8))

for age_range in df_edu_melted['age_range'].unique():
    df_age_range = df_mean[df_mean['age_range'] == age_range]
    ax.plot(df_age_range['Year'], df_age_range['value'], label=age_range)

ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.legend()

# Display the chart using Streamlit
st.pyplot(fig)



import altair as alt
st.markdown("<h3 style='font-size:18px;'> # Line chart of Mean years of educational attendance for each gender </h3>", unsafe_allow_html=True)

df_mean = df_edu_melted.groupby(['gender', 'Year']).mean().reset_index()

# Create a line chart for each gender
gender_list = df_edu_melted[df_edu_melted['gender'] != 'children' ]['gender'].unique()
chart_data = pd.DataFrame(columns=['Year', 'gender', 'value'])

for gender in gender_list:
    df_gender = df_mean[df_mean['gender'] == gender]
    chart_data = chart_data.append(df_gender)

chart = alt.Chart(chart_data).mark_line().encode(
    x='Year',
    y='value', 
    color='gender'  
).properties(
    width=700, height=400).configure_axis(
    labelFontSize=12, titleFontSize=14
).configure_legend(
    labelFontSize=12, titleFontSize=14
)

st.altair_chart(chart)




# df_fert 


st.subheader("Fertility data : ") 

df_fert_melted = df_fert.drop(columns=['Total Fertility Rate']).melt(id_vars=['Country name', 'Year'], 
                    value_vars=[

        'Age-specific fertility rate age 10-14',
        'Age-specific fertility rate age 15-19',
        'Age-specific fertility rate age 20-24',
        'Age-specific fertility rate age 25-29',
        'Age-specific fertility rate age 30-34',
        'Age-specific fertility rate age 35-39',
        'Age-specific fertility rate age 40-44',
        'Age-specific fertility rate age 45-49'
                                ],
                    var_name='category', value_name='value')


df_fert_melted['age_range'] = df_fert_melted['category'].str.extract('(10-14|15-19|20-24|25-29|30-34|35-39|40-44|45-49)')
df_fert_melted.drop('category', axis=1, inplace=True)



st.markdown("<h3 style='font-size:18px;'> # Top 10 Countries with Highest Average fertility rate </h3>", unsafe_allow_html=True)

df_top_10 = df_fert_melted.groupby(['Country name'])[['value']].mean().nlargest(10, 'value').sort_values(ascending=True, by='value').reset_index()

# Plot the bar chart
fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(df_top_10['Country name'], df_top_10['value'])
ax.set_xlabel('Average fertility rate')
ax.set_ylabel('Country')

# Create a twin y-axis
ax2.tick_params(axis='x')
ax2.set_xlim(ax.get_xlim())

# Show the plot
st.pyplot(fig)


st.markdown("<h3 style='font-size:18px;'> # Bar chart of Mean fertility rate by age_range </h3>", unsafe_allow_html=True)

df_mean = df_fert_melted.groupby(['age_range']).mean().reset_index()

fig, ax = plt.subplots(figsize=(15, 7))
for age_range in df_fert_melted['age_range'].unique():
    df_age_range = df_mean[df_mean['age_range'] == age_range]
    ax.barh(df_age_range['age_range'], df_age_range['value'], label=age_range)

ax.set_xlabel('Value')
ax.set_ylabel('age_range')
ax.legend()

st.pyplot(fig)








