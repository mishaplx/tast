# разность времени с переводом в секунды
h = int(input())
m = int(input())
c = int(input())
h1 = int(input())
m1 = int(input())
c1 = int(input())
cek1 = h1 * 3600 + m1 * 60 + c1
cek2 = h * 3600 + m * 60 + c
if cek2 > cek1:
    print("error")
else:
    print(cek1 - cek2)