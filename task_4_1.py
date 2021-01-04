# найти периметр, зная точки в пространстве
from math import sqrt

def distance(x1, y1, x2, y2, x3, y3):
    s1 = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    s2 = sqrt((pow(x3 - x2, 2) + pow(y3 - y2, 2)))
    s3 = sqrt((pow(x1 - x3, 2) + pow(y1 - y3, 2)))
    p = s1 + s2 + s3
    return p


x1 = int(input(""))
y1 = int(input(""))
x2 = int(input(""))
y2 = int(input(""))
x3 = int(input(""))
y3 = int(input(""))
print(distance(x1, y1, x2, y2, x3, y3))
