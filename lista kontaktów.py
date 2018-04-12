kontakty = {"Maciek": 706045689,
            "Ola": 854065231,
            "Marzena": 245678910,
            "Karol": 522830025
            }

def number(nazwa):
    return("Numer telefonu: %s" %(kontakty[nazwa]))

play = ''
while play != "zakończ":
    print("Kontakty:")
    for key in kontakty:
        print(key)
    nazwa = input("Wprowadź imię:")
    if nazwa in kontakty:
        print(number(nazwa))
    else:
        print("Podany kontakt nie istnieje")
        print("Co chcesz zrobić? / 1 - wprowadź nowy kontakt, 2 - usuń kontakt, 3 - wyświetl całą listę")
        akcja = input("Czynność: ")
        if akcja == "1":
            new_name = input("Wprowadź imię: ")
            new_number = input("Wprowadź numer: ")
            new_element = kontakty[new_name] = new_number
            play = input("Pomyślnie dodano numer. Aby ponownie wyświetlić kontakty, wybierz 3")
        elif akcja == "2":
            delete = input("Wybierz kontakt do usunięcia")
            if delete in kontakty:
                kontakty.pop(delete)
                play = input("Pomyślnie usunięto numer. Aby ponownie wyświetlić kontakty, wybierz 3")
            else:
                print("Wybrany kontakt nie istnieje")
                play = input("Aby wyświetlić kontakty, wyvierz 3")
        elif akcja == "3":
            print(kontakty)
        else:
            play = "zakończ"
            print("Żegnaj")
