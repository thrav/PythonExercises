name = input('Enter your name: ')
age = int(input('Enter your age: '))
curYear = int(input('What year is it? '))
howMany = int(input('How many prints? '))

diff = 100-age
year = curYear+diff

print(howMany * ('\n'+name+', You\'ll turn 100 in the year '+str(year)+'.\n'))
