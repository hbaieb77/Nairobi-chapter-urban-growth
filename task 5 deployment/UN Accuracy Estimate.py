import streamlit as st
import streamlit.components.v1 as components

st.header("How reliable are the UN Population Predictions")
st.subheader('Typical Error Estimate:')
st.markdown('We estimate that a UN city population prediction will have a typical error of <span style="color:red; font-weight:bold">20%</span> of the UN prediction or less. For example, if the UN population prediction was 400,000 then the typical error will be <span style="color:red; font-weight:bold">20%</span> of <span style="color:red; font-weight:bold">400,000</span> or less which is <span style="color:red; font-weight:bold">80,000 or fewer</span>.', unsafe_allow_html=True)
st.markdown('It is unlikely that the error will exceed <span style="color:red; font-weight:bold">30%</span> of the UN population estimate.', unsafe_allow_html=True)
st.subheader('How did we estimate the error?')
st.markdown('The UN city population predictions were made in 2018. Since then, several African countries have made more recent estimates or direct census polls of their city populations. The 3 types of new city population estimates are defined below:')

st.markdown('- <span style="font-weight:bold">Population Census</span> - Directly measured and / or adjusted according to a nation wide census.',unsafe_allow_html=True)

st.markdown('- <span style="font-weight:bold">Population Estimate</span> - Calculated using the current birth and death rates and the estimated migration or they are based on population registers.',unsafe_allow_html=True)

st.markdown('- <span style="font-weight:bold">Population Projections</span> - Are calculations referring to the future, their accuracy is often poor.',unsafe_allow_html=True)

st.markdown('We estimated the typical error in the UN city population estimates by comparing the UN’s population predictions to the city population estimates made since 2018.',unsafe_allow_html=True)
if st.button('Click here to view our full analysis'):   
    HtmlFile3 = open('compare_un_to_census.html','r',encoding='utf-8')
    source_code3 = HtmlFile3.read()
    components.html(source_code3,height=700,width = 1000,scrolling=True)
    st.checkbox("Hide",True)
st.subheader('Prediction Errors Visualised')
labels = ["Prediction Error vs Population Prediction", "UN Population Prediction vs Recent Population Estimate"]
options = st.selectbox("Select Error Visualisation",labels)
if options == 'Prediction Error vs Population Prediction':
   HtmlFile1 = open("Prediction Error vs Population Prediction.html", 'r', encoding='utf-8')
   st.markdown('_This plot shows the percentage error in each UN prediction we tested. This error is plotted against the population that was predicted. We have highlighted the 20% and 20% - 30% error regions and show that most observations fall into the 20% region, some fall into the 20 - 30% region and very few lie outside this range._')
   source_code1 = HtmlFile1.read() 
   components.html(source_code1,height = 600,width=1000)

if options == 'UN Population Prediction vs Recent Population Estimate':
   st.markdown('_Here we plot the UN population prediction against the recently estimated population for every city we tested. Perfect predictions (where the UN population exactly equals the recently estimated population) would lie along the blue line. The vertical distance between the blue line and the point is the error in the prediction. Points above the line represent over-estimates and points below represent under-estimates._')
   #st.markdown('_Perfect predictions (where the UN population exactly equals the recently estimated population) would lie along the blue line. The vertical distance between the blue line and the point is the error in the prediction. Points above the line represent over-estimates and points below represent under-estimates._')

   st.markdown('_We have Shaded the 30% error region - any points lying outside this shaded region have an error larger than 30%. Most points lie within this region._')
   st.markdown('_**Please note** - you need to zoom in by clicking and dragging on the plot to see more detail._')
   HtmlFile2 = open('UN Predicted Population3 vs Measured Population.html','r')
   source_code2 = HtmlFile2.read()
   components.html(source_code2,height = 600,width=1000)
   st.markdown('_*The 30% error region is not symmetric over the blue perfect prediction line. This is unintuitive but is not a mistake. It is because the percentage error is calculated by dividing by the UN population estimate, which is on the y axis._')

st.subheader("Data Sources")
st.markdown("- Recent City Population Estimates provided by Thomas Brinkhoff: City Population (http://www.citypopulation.de)")
st.markdown("- UN City Population Predictions taken from 2018 Revision of World Urbanization Prospects (https://population.un.org/wup/)")

