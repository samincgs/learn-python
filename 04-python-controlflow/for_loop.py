# basic_list = [1, 2, 3]
# basic_tuple = (1, 2, 3)
# basic_dict = {1: "one", 2: "two", 3: "three"}
# basic_set = {1, 2, 3}
# basic_string = "one two three"
# basic_num = 0


# for x in range(basic_num, 5, 2):
#     print(x)

# exercise
practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 10, 4]]
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100

for nested_list in practice_list:
    for values in nested_list:
        if values < 50:
            if values < 10:
                continue
            print(values)
        if values > 100:
            break
