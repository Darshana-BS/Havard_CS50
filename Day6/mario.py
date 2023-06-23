print('approach1')
print('#')
print('#')
print('#')

print("approach2")
for a in range(3):
    print('#')


#------------------------------------------------------------------------
#vertica;l
print("approach3")
def main():
    print_column(3)

def print_column(h):
    # for i in range(h):
    #     print("#")
    print("#\n" * h, end="")

main()
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#horizontal
print("approach4")
def main():
    print_row(4)

def print_row(width):
    print("?" * width)
main()
#------------------------------------------------------------------------


#------------------------------------------------------------------------
#block
print("approach5 block")
def main():
    print_square(3)

def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in square
        for j in range(size):

            #Print brick
            print("#", end="")
        
        #Print a new line after every row
        print()

main()
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#block
print("approach6 block")
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#"*width)
    
main()
#------------------------------------------------------------------------