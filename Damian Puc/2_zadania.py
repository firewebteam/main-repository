#zadanie 1
print("Zadanie 1")
lista_obecnosci=["Lipert Pawel", "Kamienski Aleksander", "Puc Damian"]
lista_obecnosci.sort()
print(lista_obecnosci)

#zadanie 2
print()
print("Zadanie 2")
tab = [["Zdzislaw",73],["Damian",19], ["Aleksandra",16], ["Agnieszka",52]]

sum=0

for i in tab:
    sum=sum+i[1]

print("Sredni wiek to {} lat dla {} osob".format(sum/len(tab),len(tab)))

#zadanie 3
print("")
print("Zadanie 3")

tab.sort(key=lambda x: len(x[0]))
print(tab)
