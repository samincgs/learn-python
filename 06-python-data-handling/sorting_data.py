list1 = [4, 2, 3, 1, 5]
# print(sorted(list1, reverse=True))

list2 = [("a", 3), ("b", 10), ("c", 6), ("d", 5)]


# def sort_func(item) -> int:
#     return item[1]

# print(sorted(list2, key=lambda item: item[1]))

# exercise
inventory_names = [
    "Screws",
    "Wheels",
    "Metal parts",
    "Rubber bits",
    "Screwdrivers",
    "Wood",
]
inventory_numbers = [43, 12, 95, 421, 23, 43]

combined_list = zip(inventory_names, inventory_numbers)

# # sort this list by inventory numbers
print(sorted(combined_list, key=lambda item: item[1]))


# sort the list by length of the inventory name
print(sorted(combined_list, key=lambda item: len(item[0])))
