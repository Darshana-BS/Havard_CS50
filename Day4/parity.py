#number -> even or odd

def main():
    x = int(input('enter x:'))
    if is_even(x):
        print('Is Even')
    else:
        print('Is Odd')

def is_even(n):
    # approach1
    # if n%2 == 0:
    #     return True
    # else:
    #     return False
    
    #approach2
    # return True if n%2 == 0 else False

    #approach3
    return n%2 ==0
main()
