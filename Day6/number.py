#Valueerror Solution
"""
try:
    x = int(input("What's X? ")) #input
    print(f'x is {x}')
except ValueError:
    print("X is not an integer")
"""

#NameError
"""
try:
    x = int(input("What's X? ")) #input
except ValueError:
    print("X is not an integer")

print(f'x is {x}')
"""

#NameError Solution1
"""try:
    x = int(input("What's X? ")) #input
except ValueError:
    print("X is not an integer")
else:
    print(f'x is {x}')
"""

#NameError Solution2
"""
while True:
    try:
        x = int(input("What's X? ")) #input
    except ValueError:
        print("X is not an integer")
    else:
        break    
print(f'x is {x}')
"""

#NameError Solution3 (issue in this code asking for input twice)
"""while True:
    try:
        x = int(input("What's X? ")) #input
        break
    except ValueError:
        print("X is not an integer")    
print(f'x is {x}')
"""


#NameError solution5
# def main():
#     x = get_int()
#     print(f'x is {x}')

# def get_int():
#     while True:
#         try:
#             x = int(input("What's X? ")) #input
#             # break
#         except ValueError:
#             print("X is not an integer")   
#         else:
#             break
#     return x

# main()

#NameError solution6
# def main():
#     x = get_int()
#     print(f'x is {x}')

# def get_int():
#     while True:
#         try:
#             return int(input("What's X? "))
#         except ValueError:
#             print("X is not an integer")   

# main()

# #NameError solution6 pass
# def main():
#     x = get_int()
#     print(f'x is {x}')

# def get_int():
#     while True:
#         try:
#             return int(input("What's X? "))
#         except ValueError:
#             pass 

# main()

#NameError solution8
def main():
    x = get_int("What's X? ")
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass 

main()