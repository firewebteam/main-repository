contacts = {"Arek": 506234556,
            "Basia": 607456233,
            "Maja": 589311911,
            "Martyna": 778456332,
            "Paweł": 501223493
            }

def phone_number(name):
   return("Numer telefonu to: %s" %(contacts[name]))

play = ''
while play != "zakończ":
  print("KONTAKTY:")
  for key in contacts:
    print(key)
  name = input("Podaj imię: ")
  if name in contacts:
    print(phone_number(name))
  else:
    print("Nie ma takiego kontaktu.")
    print("Jaką czynność chcesz wykonać? \nA - dodaj nowy kontakt B - usuń bieżący kontakt C - wyjdź ")
    action = input("Czynność: ")
    if action == "A":
      new_name = input("Wprowadź imię: ")
      new_number = input("Wprowadź numer: ")
      new_element = contacts[new_name] = new_number
      play = input("Dodałeś nowy konakt,jeśli chcesz ponownie wyświetlić numery, wciśnij enter,jeśli nie, napisz 'zakończ'")
    elif action == "B":
      delete = input("Który kontakt chcesz usunąć? ")
      if delete in contacts:
        contacts.pop(delete)
        play = input("Usunąłeś bieżący konakt,jeśli chcesz ponownie wyświetlić numery, wciśnij enter,jeśli nie, napisz 'zakończ'")
      else:
        print("Nie ma takiego kontaktu.")
        play = input("Jeśli chcesz ponownie wyświetlić numery, wciśnij enter,jeśli nie, napisz 'zakończ'")
    else:
      play = "zakończ"
      print("Do widzenia!")



#posortować kontakty po dodaniu






