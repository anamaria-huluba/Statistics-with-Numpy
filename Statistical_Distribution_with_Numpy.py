# STATISTICAL DISTRIBUTIONS WITH NUMPY

# Review

# Let’s review! In this lesson, you learned how to use NumPy to analyze different distributions and 
# generate random numbers to produce datasets. 
# 
# Here’s what we covered:
# What is a histogram and how to map one using Matplotlib
# How to identify different dataset shapes, depending on peaks or distribution of data
# The definition of a normal distribution and how to use NumPy to generate one using NumPy’s 
# random number functions

# The most common distribution in statistics is known as the normal distribution, which is a symmetric, 
# unimodal distribution, np.random.normal. 
# This function takes the following keyword arguments:

# loc: the mean for the normal distribution
# scale: the standard deviation of the distribution
# size: the number of random numbers to generate

# NumPy has a function for generating binomial distributions: np.random.binomial, which we can use to 
# determine the probability of different outcomes.

# The function will return the number of successes for each “experiment”.

# It takes the following arguments:
# N: The number of samples or trials
# P: The probability of success
# size: The number of experiments

# Now you can use NumPy to analyze and graph your own datasets! You should practice building your 
# intuition about not only what the data says, but what conclusions can be drawn from your observations.

# 1. Practice what you’ve just learned with a dataset on sunflower heights! Imagine that you work for a
# botanical garden and you want to see how the sunflowers you planted last year did to see if you want 
# to plant more of them.

# Calculate the mean and standard deviation of this dataset. Save the mean to sunflowers_mean and the 
# standard deviation to sunflowers_std.

import codecademylib
import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv', delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
print(sunflowers_mean)
# returns: 13.00215

sunflowers_std = np.std(sunflowers)
print(sunflowers_std)
# returns: 1.12332225007

# 2. We can see from the histogram that our data isn’t normally distributed. Let’s create a normally 
# distributed sample to compare against what we observed.

# Generate 5,000 random samples with the same mean and standard deviation as sunflowers. Save these to 
# sunflowers_normal.

sunflowers_mean = np.mean(sunflowers)
print(sunflowers_mean)
sunflowers_std = np.std(sunflowers)
print(sunflowers_std)

# sunflowers_normal here:
sunflowers_normal = np.random.normal(
  loc=sunflowers_mean,
  scale=sunflowers_std,
  size=5000
)

# 3. Now that you generated sunflowers_normal, uncomment (remove all of the #) the second plt.hist 
# statement. Press run to see your normal distribution and your observed distribution.

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='Observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='Normal', normed=True)
plt.legend()
plt.show()

# 4. Generally, 10% of sunflowers that are planted fail to bloom. We planted 200, and want to know the probability that fewer than 20 will fail to bloom.

# First, generate 5,000 binomial random numbers that represent our situation. Save them to experiments.

# Calculate probabilities here:
experiments = np.random.binomial(200, 0.1, size=5000)

# 5. What percent of experiments had fewer than 20 sunflowers fail to bloom?

# Save your answer to the variable prob. This is the approximate probability that fewer than 20 of 
# our sunflowers will fail to bloom.

prob = np.mean(experiments < 20)

# 6. Print prob. Is it likely that fewer than 20 of our sunflowers will fail to bloom?

print(prob)
#returns: 0.4612

# There is a probability of 46% likely that fewer than 20 of pour flowers will fail to bloom. 
# The binomial distribution is important because it allows us to know how likely a certain outcome is, 
# even when it’s not the expected one. 



