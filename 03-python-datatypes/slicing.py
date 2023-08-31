# slicing
# [start: end : step]
# end does not include number, stops before it

test_list = [1,2,3,4,5,6,7,8,9,10]
print(test_list[0:8:2])
print(test_list[8:0:-1])

# leave value empty while slicing
default_slicing = test_list[::]

print(default_slicing)

# exercise
# start from 8 and go to 2, pick every second element
exercise_list = test_list[7: 0: -2]
print(exercise_list)
