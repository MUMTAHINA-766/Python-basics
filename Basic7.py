#functions

#fibonacci sequence:0 1 1 2 3 5 8 13 ....
#addition of two sequence number is next number
"""
def fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        print(x)
        print(y)

    for i in range(1,n):
        z = x+y
        x = y
        y = z
        print(z)

fibonacci(7)
"""

# guess age game
# fail in guessing or success in guessing

import random as r
secret_age = r.randint(1, 10)
flag = False

def game_func(guessed_age, secret):
    if guessed_age<secret:
        return 'Too low'
    elif guessed_age>secret:
        return 'Too high'
    else:
        return 'CORRECT!'

for i in range(1, 6):
    print('Take a guess. You have ' + str(6-i) + ' guesses left.')
    guess = int(input())
    if game_func(guess, secret_age) == 'CORRECT!':
        print('You won the game!')
        flag = True
        break
if not flag:
    print('You have lost!')


