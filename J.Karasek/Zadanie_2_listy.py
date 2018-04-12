#1
lista_obecnosci = ["Jarosław", "Zuzanna", "Marek"]
print(sorted(lista_obecnosci))

#2
my_list = [
  ["Jarosław", 19],
  ["Zuzanna", 20],
  ["Marek", 23]
]

#2 - średnia
wiek = []
liczba_osob = len(my_list)
for x in my_list: #dostęp do pojedynczego elementu listy
    wiek.append(x[1])
suma_wiek = sum(wiek)
srednia = suma_wiek/liczba_osob
print("Średni wiek dla %s osób to %s lat" % (liczba_osob, srednia))


#2 - sortowanie wg długości imion
def str_len(x):
    return len(x[0])
my_list.sort(key=str_len)
my_list.reverse()
print(my_list)




#próba bez użycia funkcji
"""kryterium = []
for y in my_list:
    a = len(y[0])
    kryterium.append(a)
    kryterium.sort
print(kryterium)
"""















