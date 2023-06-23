#module which gives access to values that typed in the command line = sys
import sys

# ---------------------------------------------------------------------------
# name1 = input("Enter name1: ")
# print("Hello, my name is: ", sys.argv[1])   #get first element in the list #access name of the prgramm with [1]
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
#IndexError resolved
#if there is nothing at [1] then 
print('\n====approach 1=========')
# try:
#     print("Hello, my name is: ", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
print('\n====approach 2=========')
# if len(sys.argv) <2:
#     print("Too few arguments")
# elif len(sys.argv)>2:
#     print("Too Manay arguments")
# else:
#     # print("Hello, my name is: ", sys.argv[1]")   #SyntaxError
#      print("Hello, my name is: ", sys.argv[1])
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
print('\n====approach 3========= with exit function')
# if len(sys.argv) <2:
#     sys.exit("Too few arguments")
# elif len(sys.argv)>2:
#     sys.exit("Too Manay arguments")

# # keep erros away from the loops
# print("Hello, my name is: ", sys.argv[1])
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
print('\n====approach 4========= with more data  or name')
if len(sys.argv) <2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("Hello, my name is: ", arg)
# ====================================

print('\n====approach 4 (A) ========= with more data  or name')
# get slice of the list = 1: gives 1 and everything else but not name of the file
#print first + all excluding last = 1:-1
#prints last = -1:
for arg in sys.argv[1:-1]:
    print("Hello, my name is: ", arg)
# ---------------------------------------------------------------------------


#pass the name in "firstname lastname" and it prints both the firstname and lastname