import random
a = random.sample(range(1,100), 20)
b = random.sample(range(1,100), 20)

print(a,'\n'+str(b),'\n','Format:',format(set(a)&set(b)))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
nA = []
nB = []
common = []

#strip duplicates
for x in a:
    if x not in nA:
        nA.append(x)

for x in b:
    if x not in nB:
        nB.append(x)

#add if common
for i in nA:
    if i in nB:
        common.append(i)

print('Duplicates:',common)
