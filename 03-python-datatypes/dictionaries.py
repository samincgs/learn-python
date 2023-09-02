# no duplicate keys (it will be overridden)
test_dict = {"A": 123, "B": [1, 2, 3], 1: True}
print(test_dict.values())
print(test_dict.keys())
print(test_dict.items())

# converting a dictionary
print(list(test_dict))

# indexing in a dictionaries
print(test_dict["A"])
print(test_dict.get("B"))  # doesn't crash when it cannot find a key

# Exercise dlo research and use the update method to add another key value pair
test_dict.update({"C": "Camel"})

print(test_dict)
