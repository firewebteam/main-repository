print('r - rock, p - paper, s -scissors')

i = 'y'
while i == 'y':
    p1_object = input("Player 1 turn. Insert object: ")
    p2_object = input("Player 2 turn. Insert object: ")

    p1_object += p2_object
    options = {'rs': 1, 'rp': 2, 'ps': 2, 'pr': 1, 'sr': 2, 'sp': 1}
    result = options[p1_object]
    print("player {} won the game!".format(result))

    i = input('Play again? y/n: ')
