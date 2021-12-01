#CrunchieMunchies Project

#You work in marketing for a food company YummyCorps, which is developing a new kind of tasty, wholesome cereal called CrunchieMunchies. You want to demonstrate to consumers 
# how healthy your cereal is in comparison to other leading brands, so you’ve dug up nutritional data on several different competitors.

#Your task is to use NumPy statistical calculations to analyze this data and prove that your CrunchieMunchies cereal is the healthiest choice for consumers.

#1. First, import numpy.

import numpy as np

#2. Look over the cereal.csv file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as calorie_stats.

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

print(calorie_stats)
#returns: 
# [  70.  120.   70.   50.  110.  110.  110.  130.   90.   90.  120.  110.
#  120.  110.  110.  110.  100.  110.  110.  110.  100.  110.  100.  100.
#  110.  110.  100.  120.  120.  110.  100.  110.  100.  110.  120.  120.
# 110.  110.  110.  140.  110.  100.  110.  100.  150.  150.  160.  100.
# 120.  140.   90.  130.  120.  100.   50.   50.  100.  100.  120.  100.
# 90.  110.  110.   80.   90.   90.  110.  110.   90.  110.  140.  100.
# 110.  110.  100.  100.  110.]

#3. There are 60 calories per serving of CrunchieMunchies. How much higher is the average calorie count of your competition?

# Save the answer to the variable average_calories and print the variable to the terminal to see the answer.

average_calories = np.mean(calorie_stats)
print(average_calories)
# returns: 106.883116883

# 4. Does the average calorie count adequately reflect the distribution of the dataset? Let’s sort the data and see.

# Sort the data and save the result to the variable calorie_stats_sorted. Print the sorted data to the terminal.

calorie_stats_sorted = np.sort(calorie_stats)
# returns:
# [  50.   50.   50.   70.   70.   80.   90.   90.   90.   90.   90.   90.
#    90.  100.  100.  100.  100.  100.  100.  100.  100.  100.  100.  100.
#   100.  100.  100.  100.  100.  100.  110.  110.  110.  110.  110.  110.
#   110.  110.  110.  110.  110.  110.  110.  110.  110.  110.  110.  110.
#   110.  110.  110.  110.  110.  110.  110.  110.  110.  110.  110.  120.
#   120.  120.  120.  120.  120.  120.  120.  120.  120.  130.  130.  140.
#   140.  140.  150.  150.  160.]

#5. Do you see what I’m seeing? Looks like the majority of the cereals are higher than the mean. Let’s see if the median is a better representative of the dataset.

#Calculate the median of the dataset and save your answer to median_calories. Print the median so you can see how it compares to the mean.

median_calories = np.median(calorie_stats)
print(median_calories)
#returns: 110.0

#6. While the median demonstrates that at least half of our values are over 100 calories, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.

#Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable nth_percentile.

nth_percentile =  np.percentile(calorie_stats, 25)
print(nth_percentile)
# returns: 100.0
nth_percentile =  np.percentile(calorie_stats, 12)
print(nth_percentile)
# returns: 90.0
nth_percentile =  np.percentile(calorie_stats, 6)
print(nth_percentile)
#returns:75.6
nth_percentile =  np.percentile(calorie_stats, 3)
print(nth_percentile)
# returns:55.6
nth_percentile = 4
#Which means that 4 is the lowest percentile we can go witjout droping below 60 calories. 

# 7. While the percentile shows us that the majority of the competition has a much higher calorie count, it’s an awkward 
# concept to use in marketing materials.

# Instead, let’s calculate the percentage of cereals that have more than 60 calories per serving. Save your answer to the 
# variable more_calories and print it to the terminal.

more_calories = 100 - nth_percentile
print(more_calories)
# returns: 96

# 8. Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, how much variation exists in the dataset? 
# Can we make the generalization that most cereals have around 100 calories or is the spread even greater?

# Calculate the amount of variation by finding the standard deviation. Save your answer to calorie_std and print to the terminal. How can we incorporate this value into our analysis?

calorie_std = np.std(calorie_stats)
print(calorie_std)
# returns: 19.3571853339

#9. Write a short paragraph that sums up your findings and how you think this data could be used to Yummy Corp’s advantage when marketing CrunchieMunchies.

# CrunchieMunchies are less caloric than a significant number of other cereal brands. Beaing in the 4th percentile, means that the other 96% of cereals have more calories. 
#Also, the difference in calories between CrunchieMunchies and other cereals is not insignificant, and we proved that 60 is not within the standard deviation of the average. 
#In fact, 60 is almost two standard deviations away making it a low outlier. 

