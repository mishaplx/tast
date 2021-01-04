# найти минимальное число в списке
def min4(a, b, c, d):
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    return min(list1)
a = int(input(""))
b = int(input(""))
c = int(input(""))
d = int(input(""))
print(min4(a, b, c, d))
