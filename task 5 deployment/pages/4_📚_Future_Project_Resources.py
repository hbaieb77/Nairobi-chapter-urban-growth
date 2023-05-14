import streamlit as st

st.write("""<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <span style='font-size:27px;font-family:"Arial",sans-serif;'>Resources For Building Advanced City &nbsp;</span>
    <span style='font-size:15px;font-family:"Arial",sans-serif;'>
        <br>&nbsp;
    </span>
    <span style='font-size:27px;font-family:"Arial",sans-serif;'>Growth Models:</span>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>What is Urban growth modelling?&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>Urban growth modelling seeks to predict the growth of cities to anticipate and plan for the resource demands they will require. This includes anticipating land use, housing demand and population as well as infrastructure changes such as new roads or public transport. To maintain urban growth in a sustainable way, city planners need to be able to look ahead and have a reliable picture of the changes and challenges they face.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>What is complex about predicting Urban growth?&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>City growth modelling is challenging for several reasons:&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>
        <span style="font-size:15px;">&nbsp;</span>
    </strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>
        <span style="font-size:15px;">No Consistent City Boundary Definition</span>
    </strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>To make predictions about how cities will grow and change, you need a clear definition of the city boundary i.e. the area of land that defines the city. There is no agreed way of defining city boundaries, different countries use different definitions. This creates a challenge because you cannot directly compare or combine city data from different countries because they do not refer to the same thing.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>There are 3 typical city boundary definitions used:&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<div style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom:0in;list-style-type: disc;">
        <li style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
            <strong>City Proper</strong>
            : Describes a city according to an administrative boundary, which is essentially an arbitrary boundary.&nbsp;
        </li>
    </ul>
</div>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<div style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom:0in;list-style-type: disc;">
        <li style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
            <strong>Urban Agglomeration</strong>
            : Considers the extent of the contiguous urban area, or built-up area, to delineate the city &rsquo;s boundaries.&nbsp;
        </li>
    </ul>
</div>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<div style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom:0in;list-style-type: disc;">
        <li style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
            <strong>Metropolitan Area:&nbsp;</strong>
            Defines its boundaries according to the degree of economic and social interconnectedness of nearby areas, identified by interlinked commerce or commuting patterns, for example.
        </li>
    </ul>
</div>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>In general, the Urban Agglomeration or Metropolitan definitions are preferred for defining a city. They reflect the on the ground reality of changes to the density of urbanisation etc. thus reflect the real growth of the city.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Poor Population Data</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>The most reliable city population estimates are made during national censuses. Unfortunately, these are only held every 5 to 10 years (or less for some developing countries). As such, we end up with a very sparse set of reliable population data. Other population estimates are based on mortality rates, fertility rates and immigration but are simply not as reliable as census data.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>Census data is more reliable, but also suffers from the city boundary definition problem. Often the population figures will be based on the City Proper definition and thus likely poorly represent the number of people who place demands on the city.</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>An Inherently Geospatial Problem</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>City growth modelling is an inherently geospatial problem. Changes in city boundaries, population density, building density, commuting lines, pollution, roads, public transport etc. are poorly summarised by tabular statistics or metrics. They are best recorded and modelled via geospatial maps, satellite imagery etc. This means that simple tabular based models are largely ineffective for making urban growth predictions &ndash;you need to use more advanced statistical methods.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>UN World Urbanization Prospects - A Simple Approach to City Population Prediction</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    Predicting future city populations is one of the simplest urban modelling objectives. Every few years, the UN creates population forecasts for all major cities in the world. This last forecast was the <a href="https://population.un.org/wup/">2018 Revision of World Urbanization Prospects</a>
    . It is an example of a simple tabular data approach to Urban Growth Modelling.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    A high level explanation of the approach can be found <a href="https://population.un.org/wup/General/FAQs.aspx">here</a>
    (see last FAQ question). The full methodology is available <a href="https://population.un.org/wup/Publications/Files/WUP2018-Methodology.pdf">here</a>
    . &nbsp;Please note, the approach relies on figures from the UN &rsquo;s other initiative, the <a href="https://population.un.org/wpp/">World Population Prospects</a>
    which forecasts populations of countries (methodology <a href="https://population.un.org/wpp/Publications/Files/WPP2022_Methodology.pdf">here</a>
    ).&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>The UN &rsquo;s city population estimates ultimately rely on 2 previous census results, on trends related to the ratio between the percentage of population living in urban areas versus the percentage of population living in rural areas and using population projections for the country itself.</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://nap.nationalacademies.org/read/10693/chapter/6">This</a>
    page provides some more intuition / logic behind the UN &rsquo;s prediction approach. It also provides other simple tabular approaches that rely on local survey data.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Criticisms of UN Population Predictions</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    The UN population predictions have been criticised for over-estimating city populations. <a href="https://nap.nationalacademies.org/read/10693/chapter/6">This</a>
    book provides some examples of errors in the UN predictions and <a href="https://dial.ird.fr/wp-content/uploads/2021/12/2004-08.pdf">this</a>
    paper provides an alternative tweaked method to improve on these errors.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>The UN has acknowledged these criticisms and attempted to adjust their method to improve the predictions.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    In this Omdena project, we attempted to estimate the typical error in the UN city population predictions.&nbsp;<span style='font-family:"Source Sans Pro",sans-serif;color:#31333F;background:white;'>We estimated that a UN city population prediction will have a typical error of &nbsp;</span>
    <strong>
        <span style='font-family:"Source Sans Pro",sans-serif;color:black;background:white;'>20%</span>
    </strong>
    <span style='font-family:"Source Sans Pro",sans-serif;color:black;background:white;'>
        &nbsp;of the UN prediction or less. For example, if the UN population prediction was 400,000 then the typical error will be <strong>20%</strong>
        of <strong>400,000</strong>
        or less which is <strong>80,000 or fewer</strong>
        . This seems like a large error, especially if you a relying on these figures for city planning.&nbsp;
    </span>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <span style='font-family:"Source Sans Pro",sans-serif;color:black;background:white;'>&nbsp;</span>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Limitations of Basic Approaches &nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>The UN is attempting to forecast the city population of every city in the world that has a population of 300,000 or more. This is a very ambitious goal and relies on sparse population census data. As such, it is not surprising that it trades accuracy for broad applicability / coverage of cities.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>We believe that such broad and wide ranging approaches to modelling (i.e. modelling many cities within a single model) will struggle to accurately predict urban growth or provide a particularly useful or detailed picture. Instead, we suggest that individual cities should be modelled. Perhaps a single city or several cities could be modelled as a proof of concept. If the modelling proves successful, the process could be streamlined to be applied to many more cities or perhaps transfer learning could be used. &nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Advanced GIS Based Approaches</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>As stated previously, we believe urban growth modelling is inherently suited to geospatial modelling approaches. These are quite complex and require a data science / urban growth specialist knowledge that is beyond the current project team &rsquo;s ability.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>We believe that an experienced data scientist, ideally with specialist urban growth knowledge, would be able to use available GIS based urban growth planning approaches to successfully create an advanced urban growth model.&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Common Advanced Urban Growth Models:</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>Below we list common statistical methods used for urban growth modelling:&nbsp;</p>
<ul style="list-style-type: disc;">
    <li>Spatial interaction models &nbsp;</li>
    <li>Cellular automata</li>
    <li>Agent-based modeling</li>
    <li>Multi-agent simulation</li>
    <li>Markov Chain</li>
    <li>Remote Sensing</li>
    <li>Analytical Hierarchy Process</li>
</ul>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://www.diva-portal.org/smash/get/diva2:621238/FULLTEXT01.pdf">This</a>
    paper provides a summary of common methods for land use modelling and road network growth including pros and cons of each method.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://www.scirp.org/journal/paperinformation.aspx?paperid=105728">This</a>
    paper compares different common methods of urban growth modelling.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://www.mdpi.com/2072-4292/12/1/109">This</a>
    paper proposes a general method of modelling city growth.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Where can I find GIS data?&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://mapscaping.com/free-gis-data-and-where-to-find-it/">This</a>
    website provides a broad list of free GIS data such as satellite imagery and maps.&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://www.openstreetmap.org/#map=11/-1.3042/36.8777&layers=H">Open Street Maps</a>
    is a useful resource for finding maps of buildings, roads, land use, administrative boundaries etc. You can get historical map data from Open Street Maps from <a href="https://download.geofabrik.de/">here</a>
    .&nbsp;
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>Other useful resources:&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <strong>&nbsp;</strong>
</p>
<p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;'>
    <a href="https://africapolis.org/">Africanopolis</a>
    has defined urban agglomeration boundaries for all cities / built up areas in Africa. &nbsp;
</p>""", unsafe_allow_html = True
)
