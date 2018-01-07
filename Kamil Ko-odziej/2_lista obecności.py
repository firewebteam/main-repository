#1.1
lista_ob = ['Kamil', 'Alek', 'Damian']

#1.2
print(lista_ob)
lista_ob.sort()
print(lista_ob)

#2.1
wiek = [('Damian', 30), ('Jacek', 19), ('Danusia', 22)]

#2.2
sum = 0
i = 0
for v in wiek:
    sum += v[1]
    i += 1
śr = sum / i
print('Średni wiek to %.2f' % śr)

#2.3
print(sorted(wiek, key=lambda wiek: len(wiek[0]), reverse=True))

#wiek.sort(key=lambda wiek: len(wiek[0]), reverse=True)
#print(wiek)

#print(sorted(wiek, key=lambda wiek: wiek[1]))