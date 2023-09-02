my_list = [1, 2, 3, 4, 5]

# # map - changes values with a function inside of a iterable
# powered_list = map(lambda x: x**2, my_list)

# print(list(powered_list))

# # filters out values from a condition
# filtered_list = filter(lambda x: x < 3, my_list)
# print(list(filtered_list))


# exercise
# create the same lists using list comprehension

powered_comp = [num**2 for num in my_list]
filtered_comp = [num for num in my_list if num < 4]
print(filtered_comp)
