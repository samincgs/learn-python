import random, string
from datetime import datetime
from math import sin


random_number = random.randint(0, 10)
test_list = [1, 2, 3, 4, 5, 6]


print(random.choice(test_list))

print(string.ascii_lowercase)

print(sin(1))

# exercise
# get current time from datetime
print(datetime.now())
