import streamlit as st

def main():
    st.title("Resources For Building Advanced City Growth Models")
    
    st.header("What is Urban growth modelling?")
    paragraph = '''
             Urban growth modelling seeks to predict the growth of cities to anticipate 
             and plan for the resource demands they will require. This includes anticipating 
             land use, housing demand and population as well as infrastructure changes such 
             as new roads or public transport. To maintain urban growth in a sustainable way,
               city planners need to be able to look ahead and have a reliable picture of the changes
                 and challenges they face.      
                    '''
    st.write(paragraph)

    st.subheader("What is complex about predicting Urban growth? ")


    st.write("City growth modelling is challenging for several reasons: ")
    st.subheader(" No Consistent City Boundary Definition")
    
    paragraph = '''
   
To make predictions about how cities will grow and change, you need a clear definition of the
 city boundary i.e. the area of land that defines the city. There is no agreed way of defining 
 city boundaries, different countries use different definitions. This creates a challenge because 
 you cannot directly compare or combine city data from different countries because they do not refer to the same thing. 
    '''
    st.write(paragraph)

    st.write("There are 3 typical city boundary definitions used: ")

    st.write("**•	City Proper:** Describes a city according to an administrative boundary, which is essentially an arbitrary boundary. ")
    st.write("**•	Urban Agglomeration:** Considers the extent of the contiguous urban area, or built-up area, to delineate the city’s boundaries.")
    st.write("**•	Metropolitan Area:** Defines its boundaries according to the degree of economic and social interconnectedness of nearby areas, identified by interlinked commerce or commuting patterns, for example.")

    paragraph = '''In general, the Urban Agglomeration or Metropolitan definitions are preferred for defining a city. 
    They reflect the on the ground reality of changes to the density of urbanisation etc. thus reflect the real growth of the city. '''
    
    st.write(paragraph)

    st.subheader("Poor Population Data")
    paragraph = '''
The most reliable city population estimates are made during national censuses. 
Unfortunately, these are only held every 5 to 10 years (or less for some developing countries).
 As such, we end up with a very sparse set of reliable population data. Other population estimates 
 are based on mortality rates, fertility rates and immigration but are simply not as reliable as census data. 

Census data is more reliable, but also suffers from the city boundary definition problem. Often the population 
figures will be based on the City Proper definition and thus likely poorly represent the number of people who place 
demands on the city.
'''

    st.write(paragraph)


    st.subheader("An Inherently Geospatial Problem")
    paragraph = '''
    
City growth modelling is an inherently geospatial problem. Changes in city boundaries,
 population density, building density, commuting lines, pollution, roads, public transport etc.
   are poorly summarised by tabular statistics or metrics. They are best recorded and modelled via
     geospatial maps, satellite imagery etc. This means that simple tabular based models are largely 
     ineffective for making urban growth predictions – you need to use more advanced statistical methods. 

    '''
    st.write(paragraph)


    
    st.subheader("UN World Urbanization Prospects - A Simple Approach to City Population Prediction")
    paragraph = '''
Predicting future city populations is one of the simplest urban modelling objectives. 
Every few years, the UN creates population forecasts for all major cities in the world.
 This last forecast was the [2018 Revision of World Urbanization Prospects](https://population.un.org/wup/). It is an example
   of a simple tabular data approach to Urban Growth Modelling. 

    '''
    st.write(paragraph)


    
    st.subheader("")
    paragraph = '''
    
A high level explanation of the approach can be found [here](https://population.un.org/wup/General/FAQs.aspx) (see last FAQ question).
 The full methodology is available [here](https://population.un.org/wup/Publications/Files/WUP2018-Methodology.pdf).  Please note, the approach relies on figures from the UN’s other initiative, 
 the [World Population Prospects](https://population.un.org/wpp/) which forecasts populations of countries (methodology [here](https://population.un.org/wpp/Publications/Files/WPP2022_Methodology.pdf)). 

 '''
    st.write(paragraph)
    paragraph = '''
The UN’s city population estimates ultimately rely on 2 previous census results, on trends
 related to the ratio between the percentage of population living in urban areas versus the percentage 
 of population living in rural areas and using population projections for the country itself.
'''
    st.write(paragraph)

    paragraph = '''
    [This](https://nap.nationalacademies.org/read/10693/chapter/6) page provides some more intuition / logic behind the UN’s prediction approach. 
    It also provides other simple tabular approaches that rely on local survey data. '''
    st.write(paragraph)


    st.subheader("Criticisms of UN Population Predictions")
    paragraph = '''
    The UN population predictions have been criticised for over-estimating city populations. 
    [This](https://nap.nationalacademies.org/read/10693/chapter/6) book provides some examples of errors in the UN predictions and [this](https://dial.ird.fr/wp-content/uploads/2021/12/2004-08.pdf) paper provides 
    an alternative tweaked method to improve on these errors. 
    '''
    st.write(paragraph)

    paragraph = '''
    The UN has acknowledged these criticisms and attempted to adjust their method to improve the predictions. 
    '''
    st.write(paragraph)


    paragraph = '''
    In this Omdena project, we attempted to estimate
      the typical error in the UN city population predictions.
        We estimated that a UN city population prediction will have a typical error of **20%** of the UN prediction or l
        ess. For example, if the UN population prediction was 400,000 then the typical error will be **20%** of **400,000** 
        or less which is **80,000 or fewer**. This seems like a large error, especially if you a relying on these figures 
        for city planning. 
    '''
    st.write(paragraph)

    st.subheader("   Limitations of Basic Approaches ")

    paragraph = '''
 
The UN is attempting to forecast the city population of every city in the world that has a population of 300,000 or
 more. This is a very ambitious goal and relies on sparse population census data. As such, it is not surprising that 
 it trades accuracy for broad applicability / coverage of cities. 

    '''
    st.write(paragraph)


    paragraph = '''
    We believe that such broad and wide ranging approaches to modelling (i.e. modelling many cities within a single model) 
    will struggle to accurately predict urban growth or provide a particularly useful or detailed picture. Instead, we
      suggest that individual cities should be modelled. Perhaps a single city or several cities could be modelled as a 
      proof of concept. If the modelling proves successful, 
    the process could be streamlined to be applied to many more cities or perhaps transfer learning could be used.  
    '''
    st.write(paragraph)

    st.subheader("Advanced GIS Based Approaches")
    paragraph = '''
    As stated previously, we believe urban growth modelling is inherently suited to geospatial modelling approaches.
      These are quite complex and require a data science / urban growth specialist knowledge that is beyond the current
        project team’s ability. 

        '''
    st.write(paragraph)

    paragraph = '''
We believe that an experienced data scientist, ideally with specialist urban growth knowledge, would be able to use
 available GIS based urban growth planning approaches to successfully create an advanced urban growth model. 


    '''
    st.write(paragraph)



    st.subheader("Common Advanced Urban Growth Models:")
    st.write("Below we list common statistical methods used for urban growth modelling: ")

    st.write("•	Spatial interaction models")
    st.write("•	Cellular automata")
    st.write("•	Agent-based modeling")
    st.write("•	Multi-agent simulation")
    st.write("•	Markov Chain")
    st.write("•	Remote Sensing")
    st.write("•	Analytical Hierarchy Process")




    st.write("[This](https://www.diva-portal.org/smash/get/diva2:621238/FULLTEXT01.pdf) paper provides a summary of common methods for land use modelling and road network growth including pros and cons of each method. ")

    st.write("[This](https://www.scirp.org/journal/paperinformation.aspx?paperid=105728) paper compares different common methods of urban growth modelling. ")
    st.write("[This](https://www.mdpi.com/2072-4292/12/1/109) paper proposes a general method of modelling city growth. ")

    st.subheader("Where can I find GIS data? ")
    st.write("[This](https://mapscaping.com/free-gis-data-and-where-to-find-it/) website provides a broad list of free GIS data such as satellite imagery and maps. ")
    st.write("[Open Street Maps](https://www.openstreetmap.org/#map=11/-1.3042/36.8777&layers=H) is a useful resource for finding maps of buildings, roads, land use, administrative boundaries etc. You can get historical map data from Open Street Maps from [here](https://download.geofabrik.de/)")
    
    st.subheader("Other useful resources: ")
    st.write("[Africanopolis](https://africapolis.org/) has defined urban agglomeration boundaries for all cities / built up areas in Africa.  ")
    
   
if __name__ == "__main__":
    main()
