# Election Results

# You’re part of an impartial research group that conducts phone surveys prior to local elections. 
# During this election season, the group conducted a survey to determine how many people would vote 
# for Cynthia Ceballos vs. Justin Kerrigan in the mayoral election.

# Now that the election has occurred, your group wants to compare the survey responses to the actual 
# results.

# 1. First, import numpy and matplotlib.

import numpy as np
import matplotlib as plt

# 2. At the top of script.py is a list of the different survey responses.

# Calculate the number of people who answered ‘Ceballos’ and save the answer to the variable 
# total_ceballos.

# Print the variable to the terminal to see its value.

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for response in survey_responses if response == "Ceballos"])
print(total_ceballos)
# returns: 33

# 3. Calculate the percentage of people in the survey who voted for Ceballos and save it to the variable 
# percentage_ceballos.

# Print the variable to the terminal to see its value.

survey_length = float(len(survey_responses))
print(survey_length)
# returns: 70.0
percentage_ceballos = total_ceballos / survey_length
print(percentage_ceballos)
# returns: 0.471428571429

# 4. In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. Your supervisors
# are concerned because this is a very different outcome than what the poll predicted. They want you to 
# determine if there is something wrong with the poll or if given the sample size, it was an entirely 
# reasonable result.

# Generate a binomial distribution that takes the number of total survey responses, the actual success 
# rate, and the size of the town’s population as its parameters. Then divide the distribution by the 
# number of survey responses. Save your calculation to the variable possible_surveys.

possible_surveys = np.random.binomial(survey_length, 0.54, size=10000) / survey_length

# 5. Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.

plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()
# 6. As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted 
# for Ceballos in the actual election.

# Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% 
# of the vote and save it to the variable ceballos_loss_surveys.

possible_surveys_length = float(len(possible_surveys))
incorrect_predictions = len(possible_surveys[possible_surveys < 0.50])
ceballos_loss_surveys = incorrect_predictions / possible_surveys_length
print(ceballos_loss_surveys)
# returns: 0.2189, which means that there's about 20% chance that we get the wrong prediction. 

# 7. With this current poll, about 20% of the time a survey output would predict Kerrigan winning, 
# even if Ceballos won the actual election.

# Your co-worker points out that your poll would be more accurate if it had more responders.

# Generate another binomial distribution, but this time, see what would happen if you had instead 
# surveyed 7,000 people. Divide the distribution by the size of the survey and save your findings to 
# large_survey.

large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length,0.54, size=10000) / large_survey_length 

plt.hist(possible_surveys, range=(0,1), bins=20)
plt.hist(large_survey, alpha=0.5, range=(0,1), bins=20)
plt.show()

# 8. Now, recalculate the percentage of surveys that would have an outcome of Ceballos losing and save 
# it to the variable ceballos_loss_new, and print the value to the terminal.

incorrect_predictions = len(large_survey[large_survey < 0.50])
ceballos_loss_new = incorrect_predictions / large_survey_length
print(ceballos_loss_new)
# returns: 0.0

# What do we notice about this new value?
#A much larger sample size is a much better representation of what the outcome of the resulta would be. 

# What advice would you give to your supervisors about predicting results from surveys?
# There are 0% chance of getting a result below 50% when using a more representative sample size, 
# in our case of 7000. This clearly shows that a larger smaple size will result in more accurate 
# predictions and less chance of failure. 

