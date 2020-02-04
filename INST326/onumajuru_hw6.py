#Part 1
fh = open("weather.txt")
weather = fh.readlines()
del weather[0]
for line in weather:
    line1 = line.replace('\n', '')
    parts = line1.split('\t')
    date = parts[0]
    temp = parts[1]
    press = parts[2]
    humid = parts[3]
    wndspd = parts[4]
    print(date, temp)

print("End of part 1")
print(" ")


# Part 2 and 3
class WeatherObservation:
    def __init__(self, date, temp, press, humid, wind):
        pass

        self.date = date
        self.temp = temp
        self.press = press
        self.humid = humid
        self.wind = wind

    # part 4
    def printObservation(self):
        for line in weather:
            if self.date in line:
                return line
        return self.date, self.temp, self.press, self.humid, self.wind


# Part 5
obs_list = []
temp_list = []
press_list = []
humid_list = []
wind_list = []
for line in weather:
    line1 = line.replace('\n', '')
    parts = line1.split('\t')
    date = parts[0]
    temp = parts[1]
    press = parts[2]
    humid = parts[3]
    wind = parts[4]
    # this creates WeatherObservation object for each line in weather file
    row = WeatherObservation(date, temp, press, humid, wind)
# Part 6 - stores each WeatherObservation in list
    obs_list.append(row.printObservation())
    # for part 7
    temp_list.append(float(row.temp))
    press_list.append(float(row.press))
    humid_list.append(int(row.humid))
    wind_list.append(int(row.wind))
# Prints out list of of weather observations from Part 6
print(obs_list)
# Part 7
avg_temp = round(sum(temp_list)/len(temp_list), 2)
avg_press = round(sum(press_list)/len(press_list), 2)
avg_humid = round(sum(humid_list)/len(humid_list), 2)
avg_wind = round(sum(wind_list)/len(wind_list), 2)
print("Average temperature: " + str(avg_temp))
print("Average pressure: " + str(avg_press))
print("Average humidity: " + str(avg_humid))
print("Average wind speed: " + str(avg_wind))

# Part 8
for line in weather:
    line1 = line.replace('\n', '')
    parts = line1.split('\t')
    date = parts[0]
    temp = parts[1]
    press = parts[2]
    humid = parts[3]
    wind = parts[4]
    if str(max(temp_list)) in line:
        max_temp_date = date
    if str(max(press_list)) in line:
        max_press_date = date
    if str(max(humid_list)) in line:
        max_humid_date = date
    if str(max(wind_list)) == wind:
        max_wind_date = date

max_temp = WeatherObservation(max_temp_date, temp, press, humid, wind)
max_press = WeatherObservation(max_press_date, temp, press, humid, wind)
max_humid = WeatherObservation(max_humid_date, temp, press, humid, wind)
max_wind = WeatherObservation(max_wind_date, temp, press, humid, wind)
print("Date with max temp:")
print(max_temp.printObservation())
print("Date with max pressure:")
print(max_press.printObservation())
print("Date with max humidity:")
print(max_humid.printObservation())
print("Date with max wind speed:")
print(max_wind.printObservation())