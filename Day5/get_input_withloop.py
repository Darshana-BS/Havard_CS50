#approach1
# while True:
#     n = int(input('Enter input'))
#     if n<0:
#         continue
#     else:
#         break

#approach2
"""while True:
    n = int(input('Enter input'))
    if n>0:
        break
for i in range(n):
    print('meow')
"""
#approach3
# def main(n):
#     meow(n)
# def meow(n):
#     for i in range(n):
#         print('meow')
# main(2)


#approach4
def main():
    number = get_input()
    meow(number)

def get_input():
    while True:
        n = int(input('Enter input'))
        if n > 0:
            # return n
            break
    return n

def meow(n):
    for i in range(n):
        print('meow')
# main(number)