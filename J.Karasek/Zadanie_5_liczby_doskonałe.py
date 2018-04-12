lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for num in range(lower,upper + 1): #sprawdza liczby w przedziale domkniętym
    result = 0                     #suma dzielników (instrukcja jest po pierwszej pętli, bo result musibyć równy zero dla każdej następnej sprawdzanej liczby num)
    for i in range(1, num):        #pętla dla dzielników,jeśli iteracja się skończy przechodzi do pętli wyżej
        if num % i == 0:
            result += i
    if num == result:               #jeśli sprawdzi wszystkie dzielniki danej liczby(num), to opuszcza drugą pętlę for i sprawdza, czy spełniony jest warunek dla liczb doskonałych
        print(num)
