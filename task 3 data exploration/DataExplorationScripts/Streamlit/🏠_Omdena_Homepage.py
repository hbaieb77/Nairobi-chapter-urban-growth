import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="👋",
)

st.markdown(
    "<h1 style='text-align: center;'>Predictive Urban Growth and Planning in African Cities</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center;'>Omdena - Nairobi, Kenya Chapter</h3>",
    unsafe_allow_html=True,
)

st.markdown("""<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>In this project, we aim to introduce how a group can use our data and research to build a full model that predicts urban growth, city maintenance, and environmental monitoring.&nbsp;</span></p>
<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>&nbsp;</span></p>
<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>We have used the United Nations data, referenced in the resources page, to analyze the reliability of the data by assessing the error rates. The error rates are calculated using population census, estimates, and projections. The analysis is broken down in the accuracy analysis page.</span></p>
<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>&nbsp;</span></p>
<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>We have created an environmental monitoring dashboard that displays the current status of the air quality. This section also breaks down the different components in the air.</span></p>
<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>&nbsp;</span></p>
<p style='margin:0in;font-size:15px;font-family:"Helvetica Neue",serif;color:black;border:none;'><span style='font-family:"Arial",sans-serif;'>Lastly, there is a page dedicated to the resources used along the way. This section breaks down the underlying question, the problems faced when solving the problem, and all the resources used.&nbsp;</span></p>""", unsafe_allow_html=True)

st.sidebar.success("Select a dashboard above.")
