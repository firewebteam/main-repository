#y = ax ^ 2 + bx + c

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

delta = b**2 - (4*a*c)
pierwiastek_delta = delta*(1/2)

p=-b/(2*a)
q=-delta/(4*a)

x0 = p
x1 = (-b - pierwiastek_delta)/2*a
x2 = (-b + pierwiastek_delta)/2*a

if delta > 0:
    print('Funkcja ma 2 rozwiązania i mają one wartość:  = ', 'x1 =',x1,
          'oraz x2 = ',x2, '\nWierzchołek ma współrzędne: ','x = ',p, 'oraz y = ',q )
elif delta == 0:
    print('Funkcja ma 1 rozwiązanie i jest ono równe: ',x0,'\nWierzchołek ma współrzędne: ','x = ',p, 'oraz y = ',q )
else:
    print("Funkcja nie ma rozwiązań")
