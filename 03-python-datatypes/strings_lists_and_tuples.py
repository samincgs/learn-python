test_string = "this is a test"
test_list = [1, 2, 3, 4]

# turning a string into a list / tuple
split_str = test_string.split()
print(split_str)

print(list(test_string))
print(tuple(test_string))

# turn a list/ tuple into a string
print("ate".join(["one", "two"]))

# indexing on strings
print(test_string[0])

# exercise
# print(str(test_list).replace("[", "").replace("]", "").replace(",", ""))

solution = str(test_list).strip("[").strip("]").replace(",", "")
print(solution)
