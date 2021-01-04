# сумма цифр, числа N
N = int(input(""))
a = N // 100
b = (N // 10) % 10
c = N % 10
s = a + b + c
print(s)
