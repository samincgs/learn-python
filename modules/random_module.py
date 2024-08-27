# RANDOM MODULE
import random

# random number between 0 and 1 not including the 1 (0.01 -> 0.99)
value = random.random()
print(value)

# random floating value between 1 - 10
value = random.uniform(1, 10)
print(value)

# random integers 
value = random.randint(1, 6)
print(value)

# random value in a list of values
greetings = ['Hello', 'Hey', 'Hi', 'Hola','Hiya']
value = random.choice(greetings)
print(value + ' Sam')

# get multiple random values in a list
colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=10, weights=[18, 18, 2]) # add different weights and number of times k
print(results)

# randomly shuffle a list of values
deck = [x for x in range(1, 53)]
random.shuffle(deck)
print(deck)

# get 5 random cards from this deck sample method get unique values from the list
hand = random.sample(deck, k=5)
print(hand)

