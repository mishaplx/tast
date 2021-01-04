# округление
from math import floor, ceil
x = float(input(""))
if x - int(x) < 0.5:
    print(floor(x))
else:
    print(ceil(x))
