
courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses)

# # length of courses
print(len(courses))

# # access value
print(courses[0])

# # last value
print(courses[-1])

# # first two values
print(courses[:2])

# # last two values
print(courses[2:])

# list methods
# # add item to the end of the game
courses.append('Art')

# # add item to a specific spot in the list
courses.insert(0, 'Gym')

# use extend to add multiple values to the list
courses_2 = ['Art', 'Education']

courses_2.extend(['Math', 'English'])

# remove a value from the list

print(courses)
print(courses_2)