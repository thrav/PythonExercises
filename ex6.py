word = input('Word to check: ')
length = int(len(word))

w1 = word
w2 = word[::-1]

print(w1,w2)

if w1 == w2: print('yep')
else: print('nope')

for x in range(0,int((length+1)/2)):
    if word[x] != word[length-(x+1)]:
        print('not')
        break

print('a palindrome')
