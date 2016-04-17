a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Print smaller than: '))

#for x in a:
#  if x < 5: print(x)

new = []

for x in a:
    if x < num: new.append(x)

print(new)
