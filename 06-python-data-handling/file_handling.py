# open and close it manually
# file = open("test.txt")
# print(tuple(file))
# file.close()

with open("test.txt") as file:
    # print(file.read())
    for line in list(file):
        print(line)

# write some file
with open("test.txt", "a") as file:
    file.write("write some MORE")
