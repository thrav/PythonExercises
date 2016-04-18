import random

c = random.sample(['r','p','s'],1)
c = c[0]
player = input('[R]ock, [P]aper or [S]cissors? ')
p = player.lower()

if p == 'r' or p == 'rock':
    p = 'r'
elif p == 'p' or p == 'paper':
    p = 'p'
elif p == 's' or p == 'scissors':
    p = 's'
else:
    print('invalid input')

print()

if p == 'r':
    if c == 'r':
        print('Computer played Rock. Draw.')
    elif c == 'p':
        print('Computer played Paper. You lose.')
    elif c == 's':
        print('Computer played Scissors. You win!')

if p == 'p':
    if c == 'r':
        print('Computer played Rock. You win!')
    elif c == 'p':
        print('Computer played Paper. Draw.')
    elif c == 's':
        print('Computer played Scissors. You lose.')

if p == 's':
    if c == 'r':
        print('Computer played Rock. You lose.')
    elif c == 'p':
        print('Computer played Paper. You win!')
    elif c == 's':
        print('Computer played Scissors. Draw.')

print()
