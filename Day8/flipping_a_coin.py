# 1 popular coin toss
import random

coin = random.choice(["heads", "tails"]) #it has 50-50 chance due to string in the list
print(coin)


# 2 coin toss another way
from random import choice
coin = choice(["heads", "tails"]) #it has 50-50 chance due to string in the list
print(coin)

# 3 random number
import random
number = random.randint(1,10)  #print the random number with 10% probabity of each
print(number)

#4shuffle the cards
import random
cards = ["Jack", "Queen", "King", "A", "B"]
random.shuffle(cards)
print(cards)  # normal list
for card in cards:   #for each card to be printed one at a time
    print(card)