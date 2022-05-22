#Проверка логина и пароля
login = "kino"
password = "lili23"
n = 1
count = 1
while n != 4:
    x = input("login: ")
    y = input("Password: ")
    if x == login:
        print('ok login')
        a = 1
    else:
        print('No correct login')
        a = 0

    if y == password:
        print('ok password')
        c = 1
    else:
        print('no correct password')
        c = 0
    if a == 1 and c == 1:
        print('count:', count)
        print('ENTER, WELCOME')
        break
    else:
        print('count:', count)
        print('STOP')
    n += 1
    count += 1
if n <4:
    pass
else:
    print('BLOCKED!!!')

