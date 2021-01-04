# склонение 
n = int(input(""))
if n == 0 or n >= 5 and n <= 19 or n % 10 == 0:
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(n, "korovy")
else:
    print(n, "korov")
