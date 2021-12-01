# Introduction to Numpy Review Project
# 
# 1. You are working on a team of climate scientists and one of your roles is to take the weekly temperature 
# data and input into NumPy arrays for later analysis. The sensor records the temperature 4 times a day, 
# at 0:00, 6:00, 12:00, and 18:00. 
# 
# You are given last weeks data (Monday through Friday) and asked to create a NumPy array.

#We get started by importing the numpy package.

import numpy as np

# 2. Create an array temperatures by importing the data in the CSV temperature_data.csv

# (CSV based on data from the National Oceanic and Atmospheric Administration)

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

#3. Inspect the data by printing it to the terminal.

# The columns are the times, starting at 0:00, and the rows are days, starting on Monday, and the values 
# are the recorded temperatures at that time on those days.

print(temperatures)
#returns: 
# [[ 43.6  45.1  58.8  53. ]
#  [ 47.   44.5  58.3  52.6]
#  [ 46.7  44.2  57.9  52.2]
#  [ 46.5  44.1  57.6  51.9]
#  [ 46.2  43.9  57.2  51.5]]

#4. One of the researchers noticed that the sensor had been incorrectly zeroed and all of the recorded 
#temperatures are 3.0 degrees too cold.

# Adjust the array so that the temperature readings are accurate and save them to temperatures_fixed.

temperatures_fixed = temperatures + 3.0

print(temperatures_fixed)
#returns: 
# [[ 46.6  48.1  61.8  56. ]
#  [ 50.   47.5  61.3  55.6]
#  [ 49.7  47.2  60.9  55.2]
#  [ 49.5  47.1  60.6  54.9]
#  [ 49.2  46.9  60.2  54.5]]

# 5. Another researcher asked you for the temperature values from Monday. Save them to a new array, 
#monday_temperatures.

monday_temperatures = temperatures_fixed[0, :]

print(monday_temperatures)
#returns an array with the temperatures recorded on Monday:
# [ 46.6  48.1  61.8  56. ]

#6. “Hmmm, interesting” the researcher mumbles, “can you also give me the 6:00 AM data for Thursday and 
# Friday?”

#Save this data to a new array thursday_friday_morning.

thursday_friday_morning = temperatures_fixed[-2:, 1]

print(thursday_friday_morning)
#returns an array with only the elements recorded at 6am on Thursday and Friday only:
# [ 47.1  46.9]

#7. Finally, the persistent researcher now wants all the high and low temperatures over the week.

# Select all temperatures that are under 50 degrees or over 60 degrees and save them to a new array 
# temperature_extremes.

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]

print(temperature_extremes)
# returns all values with the specified requirements above:
# [ 46.6  48.1  61.8  47.5  61.3  49.7  47.2  60.9  49.5  47.1  60.6  49.2
#   46.9  60.2]

  









