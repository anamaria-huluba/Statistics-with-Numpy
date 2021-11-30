#STATISTICS WITH NUMPY

#Betty's Bakery

#Betty has always used her grandmother’s recipe book to make cookies, cakes, pancakes, and bread for her friends and family. She’s getting ready to open a business and will need to start buying all of her milk, eggs, sugar, flour, and butter in bulk.

#Help Betty figure out how much she needs to buy using NumPy arrays describing her recipes.

#1. Start by importing NumPy as np.

import numpy as np

#2. All of Betty’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake 
# recipe calls for:

#Flour	 Sugar	    Eggs	Milk	Butter
#2 cups	 0.75 cups	2 eggs	1 cups	0.5 cups

#Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). 
#Save this array as cupcakes.

cupcakes = np.array([2, 0.75, 2, 1, 0.5])

#3. Betty’s assistant has compiled all of her recipes into a csv (comma-separated variable) file called 
# recipes.csv. Load this file into a variable called recipes.

recipes = np.genfromtxt('recipes.csv', delimiter=',')

#4. Display recipes using print.

#Each row represents a different recipe. Each column represents a different ingredient.

print(recipes)
# returns the two-dimentional array with all the ingredients:
#[[ 2.     0.75   2.     1.     0.5  ]
# [ 1.     0.125  1.     1.     0.125]
# [ 2.75   1.5    1.     0.     1.   ]
# [ 4.     0.5    2.     2.     0.5  ]]

#5. The 3rd column represents the number of eggs that each recipe needs.

#Select all elements from the 3rd column and save them to the variable eggs.

eggs = recipes[:, 2]

print(eggs)
# returns:
# [ 2.  1.  1.  2.]

#6. Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of 
#eggs.

print(eggs == 1)
# returns: [False  True  True False]

#7. Betty is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).

# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.

cookies = recipes[2, :]
print(cookies)
# returns: [ 2.75  1.5   1.    0.    1.  ]

#8. Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. 
# Save your new variable to double_batch.

double_batch = cupcakes * 2

print(double_batch)
#returns: [ 4.   1.5  4.   2.   1. ]

# 9. Create a new variable called grocery_list by adding cookies and double_batch.

grocery_list = cookies + double_batch
print(grocery_list)
# returns: [ 6.75  3.    5.    2.    2.  ]

