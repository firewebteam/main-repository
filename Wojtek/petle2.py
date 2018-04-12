word = input('insert word: ')
a = 1
parts = []
m = 0
j = 0

for i in range(len(word) - 1):
    parts.append(word[i] + word[i+1])
    if parts.count(parts[j]) > a:
        a += 1
        m = parts[j]
    j += 1

if a == 1:
    print('there is no recurred bigrams')
else:
    print('bigram "{}" recurs {} times'.format(m, a))
