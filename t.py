#1. Exploring the data from American Community Survey "income.csv"
#The first 5 rows of the data
print(income.head())
#Find the county with the lowest median income in the US(median_income). 
#Assign the name of the county(county) to lowest_income_county
lowest_income_county = income["county"][income["median_income"].idxmin()]
#Find the county that has more than 500000 residents with the lowest median income. 
#Assign the name of the county to lowest_income_high_pop_county
high_pop = income[income["pop_over_25"] > 500000]
lowest_income_high_pop_county = high_pop["county"][high_pip["median_income"].idxmin()]

#2. Random Numbers
import random
#Returns a random integer betweeen the number 0 and 10, inclusive.
num = random.randint(0, 10)
#Generate a sequence of 10 random numbers between the values of 0 and 10.
random_sequence = [random.randint(0, 10) for _ in range(10)]
#Sometimes, when we generate a random sequence, we want it to be the same sequence
#whenever the program is run.
#An example is when you use random numbers to select a subset of the data, and you
#want other people looking at the same data to get the same subset.
#We can ensure this by setting a random seed.
#A random seed is an integer that is used to "seed" a random number generator.
#After a random seed is set, the numbers generated after will follow the same sequence.
random.seed(10)
print([random.randint(0,10) for _ in range(5)])
random.seed(10)
# Same sequence as above.
print([random.randint(0,10) for _ in range(5)])
random.seed(11)
# Different seed means different sequence.
print([random.randint(0,10) for _ in range(5)])
#Set a random seed of 20 and generate a list of 10 random numbers between the values 0 and 10.
#Assign the list to new_sequence
random.seed(20)
new_sequence = [random.randint(0,10) for _ in range(10)])
print(new_sequence)

#3. Selecting items from a list
#Let's say that we have some data on how much shoppers spend in a store.
shopping = [300, 200, 100, 600, 20]
#We want to sample the data, and only select 4 elements.
random.seed(1)
shopping_sample = random.sample(shopping, 4)
#4 random items form the shopping list.
print(shopping_sample)

#4. Population vs sample
import matplotlib.pyplot as plt
#A function that returns the result of a die roll.
def roll:
    return random.randint(1,6)
    
random.seed(1)
small_sample = [roll() for i in range(10)]
#Plot a histogram with 6 bins (1 for each possible outcome of the die roll)
plt.hist(small_sample, 6)
plt.show()

#Set the random seed to 1, then generate a medium sample of 100 die rolls. 
#Plot the result using a histogram with 6 bins.
random.seed(1)
medium_sampe = [roll() for i in range(100)]
plt.hist(medium, 6)
plt.show()

#Set the random seed to 1, then generate a large sample of 10000 die rolls.
#Plot the result using a histogram with 6 bins.
random.seed(1)
large_sample = [roll() for i in range(10000)]
plt.hist(large_sample, 6)
plt.show()

#Finding the right sample size
def probability_of_one(num_trials, num_rolls):
	#This function will take in the number of trials, and the number of rolls per trial.
	#Then it will conduct each trail, and record the probability of rolling a one.
    probabilities = []
    for i in range(num_trials):
    	die_rolls = [roll() for _ in range(num_rolls)]
    	one_prob = len([d for d in die_rolls if d==1]) / num_rolls
    	probabilities.append(one_prob)
    return probabilities
  
  random.seed(1)
  small_sample = probability_of_one(300, 50)
  plt.hist(small_sample, 20)
  plt.show()
  
  #Set the random seed to 1, then generate probabilities for 300 trials of 100 die rolls each. Make a histogram with 20 bins.
  random.seed(1)
  medium_sample = probability_of_one(300, 100)
  plt.hist(medium_sample, 20)
  plt.show()
  
  #Set the random seed to 1, then generate probabilities for 300 trials of 1000 die rolls each. Make a histogram with 20 bins.
  random.seed(1)
  large_sample = probability_of_one(300, 1000)
  plt.hist(large_sample, 20)
  plt.show()
  
#6. What are the odds?
#See how the graphs in the last screen got "steeper" as we added more rolls? This is because the variability around the mean decreases as we have more samples in each trial.
#One interesting thing that we can do given the distributions above is find the odds of getting a certain probability for rolling a one given the number of rolls we make.
#So, if we do 100 rolls of the die, and get a .25 probability of rolling a 1, we could look up how many trials in our data above got that probability or higher for one.
#This lets us find how likely our result is.





import random
import matplotlib.pyplot as plt


def roll():
	return random.randint(1, 6)
	
def probability_of_one(num_trials, num_rolls):
	probabilities = []
	for i in range(num_trials):
		die_rolls = [roll() for _ in range(num_rolls)]
		one_prob = len([d for d in die_rolls if d ==1]) / num_rolls
		probabilities.append(one_prob)
	return probabilities

random.seed(1)
small_sample = probability_of_one(300, 100)
plt.hist(small_sample, 20)
plt.show()
