# Lists (mutable) can be changed (methods -> append, push, pop etc.)
my_list = [1,2,3,4, 5.5, 'word']
print(my_list)
print(len(my_list))
# my_list.clear()
# my_list.reverse()
my_list.append('sentence')
print(my_list)

# Tuple (immutable) cannot be changed
my_tuple = (1,2,3,4,5.5, 'word', [7,8,9])
print(my_tuple)


# how to pick elements from a tuple or a list -> Indexing or Slicing
# does not work on dictionaries or sets
print(my_list[0])
print(my_tuple[2])
print(my_tuple[-1][2])
print(my_tuple[-3])

print(my_tuple)

# exercise: get the word / string 'hello'
exercise_list = ['first entry', [123,456,[0, 'hello']], 'bye']

print(exercise_list[1][2][1])