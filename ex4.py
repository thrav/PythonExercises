num = int(input("Input a number:"))
divs = []

for x in range(1,num+1):
  if num % x == 0: divs.append(x)

print('Divisors:',divs)
