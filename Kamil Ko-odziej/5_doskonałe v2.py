# szukanie liczb doskonałych:
#suma dzielników daje tę lilczbę np. 6=1+2+3
#wzór: L=1+2+4+.....+2^n
#jeśli L to liczba pierwsza to:
#L*2^n
#jest liczbą doskonałą.
niedoskonałe = []
doskonałe = []
L = 1
n = 1
while True:
    L += 2 ** n
    do = int(L / 2)
    for i in range(3, do, 2):
        if L % i == 0:
            niedoskonałe.append(L)
    if niedoskonałe.count(L) == 0:
        print(L * (2 ** n))
        doskonałe.append(L * (2 ** n))

    n += 1
    #print(doskonałe)