def guess_num(x: int):
    name = input('Hello! What is your name?\n')
    print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')
    cnt = 0
    while True:
        n = int(input('Take a guess.\n'))
        cnt += 1
        if n == x:
            print(f'\nGood job, {name}! You guessed my number in {cnt} guesses!')
            return
        elif x - 2 > n:
            print('\nYour guess is too low.')
        elif x + 2 < n:
            print('\nYour guess is too high.')
        else:
            print('\nYour guess is too close.')

from random import randint
guess_num(randint(1, 20))