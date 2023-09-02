# duplicates are deleted
example_set = {1, "sam", 3, 6, 9, 2, 6, 3}

print(example_set)

# set methods
example_set.add(5)
example_set.remove(2)


# pop method
print(list(example_set)[0])

# comparison methods

set1 = {1, 2, 3, 4, 4}
set2 = {4, 5, 6, 7}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# exercise
test_list = [
    43,
    25,
    324,
    234,
    5,
    2,
    6,
    7,
    32454,
    52,
    23,
    43,
    54,
    65,
    87,
    423,
    213,
    567,
    32,
    57,
    2,
    1,
    5,
    8,
    546,
    243,
]

list_len = len(test_list)
test_set = set(test_list)

if list_len > len(test_set):
    print("There were duplicates!")
else:
    print("There were no duplicates")
