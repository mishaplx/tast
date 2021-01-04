# сортировка, преобразование из чисел в строку
import math
a = int(input(""))
b = int(input(""))
c = int(input(""))
list1 = [a, b, c]
list1.sort()
for i in range(len(list1)):
    list1[i] = str(list1[i])
print(" ".join(list1))
