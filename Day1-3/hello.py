"""
#Ask the your for thier name
name = input("What's your name? ")

#remove whitespca from str #make code look better
name = name.strip()

#capitalize user's name input first letter
# name = name.capitalize()

#capitalize for the every name in the input
name = name.title()

#ask for the your's age
# name2 = input("What is your age? ")

#say hello to user
# print("hello, " + name)
# print("hello,", name, sep=" ")
# print("hello, ", end ="")
# print(name)
# print("hello,", name, "with age", name2)

# print("hello,\"friend\"")

#spcial string ahead hence we use f
print(f"hello, {name}")
#"""


#Ask the your for thier name
name = input("What's your name? ").strip().title()

#Split users name
first, last = name.split(" ")

#spcial string ahead hence we use f
print(f"hello, {first}")
