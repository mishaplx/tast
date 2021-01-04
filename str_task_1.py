# находжение строки между символами h и копирование этой строки
str1 = input("")
a = str1.find("h")
b = str1.rfind("h")
str_dl = str1[a + 1:b]
print(str1[:b] + str_dl + str1[b:])
