# szukanie liczb doskonałych:
#suma dzielników daje tę lilczbę np. 6=1+2+3
#wzór: L=1+2+4+.....+2^n
#jeśli L to liczba pierwsza to:
#L*2^n
#jest liczbą doskonałą.
pierwsze = []
czypierwsze = []
for i in range(2, 10000):
    for dz in range(2, i):
        if i % dz == 0:
            czypierwsze.append(i)
    if czypierwsze.count(i) == 0:
        pierwsze.append(i)

L = 0
n = 0
while True:
    L += 2 ** n
    if L in pierwsze:
        print(L * (2 ** n))
    #print(L)
    #print(L * (2 ** n))
    #print()
    n += 1