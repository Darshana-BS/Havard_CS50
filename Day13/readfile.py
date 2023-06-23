# read from the file

# with open("names.txt", "r") as file:
#apprach1
#     lines = file.readlines()         #read and storing in a variable


# for line in lines:
#     # print("hello", line, end="")
#     print("hello", line, line.rstrip())


#apprach2
    # for line in file:
    #     print("hello,", line.rstrip())

# approach3 sorted list reading
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")


