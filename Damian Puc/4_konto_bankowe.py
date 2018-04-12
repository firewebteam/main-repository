imie="Damian"
haslo="haslo123"
saldo=4326

x=input("Wprowadz haslo: ")
if x==haslo:
    z = int(input("Wprowadz numer: "))
    if z==2:
        print("Saldo=", saldo)
        while z==2:
            print('Jesli chcesz wplacic pieniadze wpisz "wplac", a jesli wyplacic wpisz "wyplac": ')
            y=input()
            if y=="wplac":
                kwota=int(input("Wprowadz kwote do wplacenia: "))
                saldo=saldo+kwota
            elif y=="wyplac":
                kwota = int(input("Wprowadz kwote do wyplacenia: "))
                if kwota > saldo:
                    print("Idz do roboty")
                else:
                    saldo=saldo-kwota
            else:
                print("Zla komenda")
            print("Saldo=", saldo)
            print("")
            z=int(input("Wprowadz numer: "))
            if z!=2:
                break


else:
    print("Zle haslo")