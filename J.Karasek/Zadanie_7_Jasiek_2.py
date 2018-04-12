# wzór na długość wektora
# u = abs(sqrt(x**2 + y**2))

t = float(input("Czas:"))
x = 3
y = 2
from math import sqrt
v = sqrt(x**2 + y**2)
v = abs(v)
s = v*t
if t <= 100:
  print("Jasiek przeszedł %s metrów" %s)
else:
    print("Jasiek przeszedł całą drogę")
