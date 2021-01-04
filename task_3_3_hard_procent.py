from math import ceil
p = int(input(""))
x = int(input(""))
y = int(input(""))
k = int(input(""))
x_y = float("{}.{}".format(x, y))
res = x_y + x_y * (p / 100) 
for i in range(k):
    res += res * (p / 100) 
    print(res)
#res1 = (res - int(res)) * 100
#print(int(res), int(round(res1, 2)))