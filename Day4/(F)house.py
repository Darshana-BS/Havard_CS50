# name = input('Name?')

#aproach1
# if name == 'Harry':
#     print('A')
# elif name == '2':
#     print('B')
# elif name == '3':
#     print('A')
# elif name == '4':
#     print('D')
# else:
#     print('Who?')


#approach2
# if name == 'Harry' or name == '2' or name == '3':
#     print('A')
# elif name == '4':
#     print('D')
# else:
#     print('Who?')

#approach3
name = input('Name?')
match name:
    case "Harry" | "2" | "3":
        print('A')
    case '4':
        print('D')
    case _:
        print('Who?')
