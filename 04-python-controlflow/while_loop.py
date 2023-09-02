# x = 1
# while x <= 10:
#     print(f"run {x} times")
#     x += 1


# break && continue

# x = 0
# while x < 10:
#     if x == 5:
#         continue

#     print(f"run {x} times")
#     x += 1

# exercise
# use a while loop to create a list with only even values from 0 to 100
# do not add the value 58

even_list = []
x = 0

while x <= 100:
    if x % 2 == 0 and x != 58:
        even_list.append(x)

    x += 1

print(even_list)
