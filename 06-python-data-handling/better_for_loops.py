inventory_names = [
    "Screw",
    "Wheels",
    "Metal parts",
    "Rubber bits",
    "Screwdrivers",
    "Wood",
]
inventory_numbers = [43, 12, 95, 421, 23, 43]

# inventory_collection = zip(inventory_names, inventory_numbers)
# # print(list(inventory_collection))

# # for name, number in inventory_collection:
# #     print(f"{name} current inventory: {number}")

# # enumerate function - get the current index
# # print(list(enumerate(inventory_names)))

# for index, name in enumerate(inventory_names):
#     print(f"{index}:{name}")
#     if index == len(inventory_names) // 2:
#         print("halfway done")

# exercise get 'Screws [id: 0] - inventory: 43'

inventory_collection = zip(inventory_names, inventory_numbers)

for index, items in enumerate(inventory_collection):
    print(f"{items[0]} [id: {index}] - inventory: {items[1]}")
