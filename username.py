# username
username = str(input("введите имя - "))
if len(username)>= 100:
    print("error")
else:
    print('Hello, {}!'.format(username))