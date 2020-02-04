# INST326
### Final Project
Our final project for the class involved us using MapQuest's heatmap API in order to make a heatmap of UFO sightings in the U.S. This project is found in the onumajuru_catherine_final_3.py file. When the code is run, it will output an html file that displays the heatmap and a javascript file that has a list of all the coordinates that are in the heatmap. This program uses the coordinates from the onumajuru_catherine_latlon.txt file, which was created from another program I created (onumajuru_catherine_final_1.py). This program extracted UFO sightings from the National UFO Reporting Database (http://www.nuforc.org/webreports.html) and counted how many sightings each city in the U.S. had. Then in another program (onumajuru_catherine_final_2.py), it used MapQuest's Open Maps API to get the longitude ad latitude coordinates for each city. These coordinates, along with the count of UFO sightings were saved in a list and used in creating the heatmap. 

### Object Oriented Programming
Files: onumajuru_hw6.py, weather.txt
- Reads in weather file and splits each line into its component parts
- Creates a class, WeatherObservation that has a working __init__ function
- Each instance of WeatherObservation corresponds to a row of data in the weather file. Each instance should has a date, temperature, pressure, humidity, and wind speed value. Adapts __init__ function to take these values as arguments and set variables for each instance equal to the values passed in.
- WeatherObservation class has a function printObservation() that will print all the data for a given weather observation.
- After splitting up each line, a WeatherObservation object is created to store the information in the appropriate attributes.
- Creates a list that stores ALL the weather observations I create. One WeatherObservation per line in the weather file is created.
- Prints out the average temperature, pressure, humidity, and wind speed calculated over all the data. Uses the WeatherObservation instances that were created to do this.
- Finds the date with the maximum temp, max pressure, max humidity, and max wind speed. For each date, prints the day's full info using the printObservation() function.

### Functions and Iterations
Files: onumajuru_catherine_hw3_ex1.py, onumajuru_catherine_hw3_ex2.py, onumajuru_catherine_hw3_ex3.py
- A program that simulates the Ship, Captain Crew dice game (Homework3_Ship, Captain, Crew.pdf)

