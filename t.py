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