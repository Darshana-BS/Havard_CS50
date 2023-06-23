score = int(input('enter the score: '))

#approach1
"""
if score >= 90 and score <=100:
    print('Your grade = A')
elif score>=80 and score<90:
    print('Your grade = B')
elif score>=70 and score<80:
    print('Your grade = C')
elif score>=60 and score>70:
    print('Your  grade = D')
else:
    print('Your Garde = F')
"""

#approach2
# if 90<=score <=100:
#     print('Your grade = A')
# elif 80<=score <90:
#     print('Your grade = B')
# elif 70<=score <80:
#     print('Your grade = C')
# elif 60<=score >70:
#     print('Your  grade = D')
# else:
#     print('Your Garde = F')


#approach3
if score >= 90:
    print('Your grade = A')
elif score >= 80:
    print('Your grade = B')
elif score >= 70:
    print('Your grade = C')
elif score >= 60:
    print('Your  grade = D')
else:
    print('Your Garde = F')