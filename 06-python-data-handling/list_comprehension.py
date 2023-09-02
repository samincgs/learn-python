# list comprehension
# creating lists in one line

# long version
long_list = []
for num in range(0, 100):
    long_list.append(num)

# # 0-99
# my_list = [num for num in range(0, 100)]
# # with if else
# my_conditional_list = [num if num > 10 else 0 for num in range(0, 100)]
# # print(my_list)
# print(my_conditional_list)

inventory_names = [
    "Screw",
    "Wheels",
    "Metal parts",
    "Rubber bits",
    "Screwdrivers",
    "Wood",
]
inventory_numbers = [43, 12, 95, 421, 23, 43]

# inventory_numbers_less_25 = [num for num in inventory_numbers if num < 25]
# print(inventory_numbers_less_25)

# replenish_list = [
#     (name, number)
#     for name, number in zip(inventory_names, inventory_numbers)
#     if number < 25
# ]

# print(replenish_list)

# combine list comprehensions
# combined_comp = [[x for x in range(5)] for y in range(10)]

# for row in combined_comp:
#     print(row)

# exercise
# create the fields for a chess board
# A1 A2 A3 A4 A5 A6 A7 A8

letters = "ABCDEFGH"
nums = "12345678"
nums_opposite = "87654321"

# chess_board_list = [[(x, y) for x in letters] for y in nums]

# for row in chess_board_list:
#     print(row)

chess_board_list = [[f"{row}{col}" for row in letters] for col in nums_opposite]
for row in chess_board_list:
    print(row)
