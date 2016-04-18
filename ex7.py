import random
a = random.sample(range(1,100),10)
b = []
c = a

for x in a:
    if x % 2 == 0:
        b.append(x)

d = [x for x in c if x%2==0]

print(a)
print(c)
print(b)
print(d)
