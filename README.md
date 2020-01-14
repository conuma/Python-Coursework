# Python-Coursework
A collection of Python programming projects that was done while taking INST126 - Introduction to Programming for Information Science and INST326 - Object-Oriented Programming for Information Science. Involves data visualization, analysis of data, and file extraction and analysis.

# INST126
For our final project in the class, our group wanted to see if there was some type of connection between CO2 emmissions and temperature.
We wanted to see if possibly the more CO2 emissions that a country has, the higher or more extreme temperatures they would experience. 
Here's a brief summary of our project: 
      For our project, we were able to extract historical data on CO2 emissions, earthquake occurrences, and temperature for countries           worldwide. Using this data, we were able to use Pandas in order to create a cleaner dataframe, including finding the averages over         the years. Using the earthquake occurrences dataset, we were able to graph the earthquake occurrences worldwide by overlaying it           over a basemap. For the temperatures dataset, we averaged the temperatures over the years and also created a line graph in order to         represent this change over time. Finally, we created a historical CO2 emissions dataset and found the average CO2 emissions per             country. Using these averages, we sorted the dataset to show those with the highest average CO2 emissions at the top. The top 30           countries with the highest average CO2 emissions were then represented in a bar graph. More details can be found in the                     Project FInal.docx file. 
      
      I was in charge of helping clean up the data and mainly creating the map and graphs.
Please see the INST126 Final Project.ipynb file for code for the project. We collaborated using Google Colab and then used Jupyter Lab to write the final code.
Data on CO2 emissions was obtained from https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?end=2014&start=2014&view=map 
Data on temperature, was obtained from https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00934 
Data on earthquake occurences from 1980-2014, which is in the results.txt file was obtained from https://www.ngdc.noaa.gov/nndc/struts/form?t=101650&s=1&d=1 

# INST326
### Final Project
Our final project for the class involved us using MapQuest's heatmap API in order to make a heatmap of UFO sightings in the U.S. This project is found in the onumajuru_catherine_final_3.py file. When the code is run, it will output an html file that displays the heatmap and a javascript file that has a list of all the coordinates that are in the heatmap. This program uses the coordinates from the onumajuru_catherine_latlon.txt file, which was created from another program I created (onumajuru_catherine_final_1.py). This program extracted UFO sightings from the National UFO Reporting Database (http://www.nuforc.org/webreports.html) and counted how many sightings each city in the U.S. had. Then in another program (onumajuru_catherine_final_2.py), it used MapQuest's Open Maps API to get the longitude ad latitude coordinates for each city. These coordinates, along with the count of UFO sightings were saved in a list and used in creating the heatmap. 

### Object Oriented Programming
Files: onumajuru_hw6.py

### Functions and Iterations
Files: onumajuru_catherine_hw3_ex1.py, onumajuru_catherine_hw3_ex2.py, onumajuru_catherine_hw3_ex3.py

# INST447
Our final project for this class involved us determining if there was a relationship between the income of a neighborhood and the amount of redvelopment that happens in that neighborhood. The area we studied was D.C. We obtained our redevelopment data from opendata.dc.gov and our income data from planning.dc.gov. The full project can be found in the jupyter notebook file (GroupProjectNotebook.ipynb). A list and link to all the data used can be found in the Sources of files.docx file. My role in the project was to do the cleaning and processing, while my partner worked on the visualizations or graphs. 
