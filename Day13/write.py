name = input("What's name? ")

#adding single name to file on every execution, recreates the file with "w" mode and recreate with brandnew content
# file = open("names.txt", "w")

# adding / appending the data to existing data
# file = open("names.txt", "a")

# adding every name in new line
# file = open("names.txt", "a")
# file.write(f"{name},\n")
# file.close()

# with file name use
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# read from the file




