import sys
import math
import random

print('''Instruction:
1 - Rock
2 - Scissors
3 - Paper''')

#User choise
user = int(input('Enter the number: '))

if(user == 1):
    print('You choosed ROCK')
elif(user == 2):
    print('You choosed SCISSORS')
elif(user == 3):
    print('You choosed PAPER')
else:
    print('Incorrect number')
    
#Computer choise
comp = random.randint(1,3)

if(comp == 1):
    print('Oponent choosed ROCK')
elif(comp == 2):
    print('Oponent choosed SCISSORS')
elif(comp == 3):
    print('Oponent choosed PAPER')

#Game logic

if(comp == user):
    print('Draw!')
elif((user == 1 and comp == 3)
or (user == 2 and comp == 1)
or (user ==3 and comp == 2)):
    print('You lose')
else:
    print('You WIN!')
