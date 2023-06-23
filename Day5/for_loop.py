#  initially i = 0 and increments till i = 2 and prints "meow" 3 times
#approach1
for i in [0,1,2]:
    print('meow')
print('1')

# i is required variable as the program needs to make some counting for the increment
# i can have any value ex. _
#approach2
for _ in range(3):
  print('meow') 
print('2')

#approach3
# less use
print('meow\n'*3, end='')
print('3')

# print('meow')