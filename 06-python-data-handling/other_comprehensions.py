dict_comp = {num: num for num in range(0, 11)}
set_comp = (num for num in range(0, 10))
tuple_comp = tuple(num for num in range(0, 10))
# print(tuple_comp)

# exercise
# create a dictionary with the keys 'A', 'B' , 'C', 'D', 'E'
# each key should have a list as value with the values as [1,2,3,4,5]

exercise_dict_comp = {letter: [1, 2, 3, 4, 5] for letter in "ABCDE"}
print(exercise_dict_comp)
