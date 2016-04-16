num = int(input('Enter a number: '))
div = int(input('Enter a divisor: '))
mod = num%div
four = num%4

if mod!=0: print('remainder')
else: print('multiple')

if four==0: print('mulitple of four')
