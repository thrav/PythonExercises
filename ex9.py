import random

num = random.sample(range(1,10),1)[0]

guess = int(input('Pick a number 1-9: '))
while 1 == 1:
    if guess not in range(1,10):
        print('Invalid Number')
    elif guess == num:
        print('You got it!')
        break
    elif guess < num:
        print('Higher')
    else:
        print('Lower')
    guess = int(input('Try again. Pick a number 1-9: '))
