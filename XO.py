print("****************************************")
print("Игра Крестики - Нолики приветствует Вас!")
print("****************************************")

print("X или 0 ставится путем введения двух чисел")
print("т.е. координат x, y")
print("x - по горизонтали, y - по вертикали")
print("****************************************")

field = [[' ']*3, [' ']*3, [' ']*3]

print(f"  0 1 2")
for i in range (3):
    print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
print("Ваш ход, начинают X")
def ask():
    while True:
        longitud = input("Введите координаты через пробел: ").split()
        if len(longitud) != 2:
            print("Вводите два числа !!!")
            continue
        x, y = longitud
        if not (x.isdigit()) or not (y.isdigit()):
            print("Вводить нужно числа!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Число не соответствует координатам")
            continue

        if field[x][y] == " ":
            field[x][y] = A
            print(f"  0 1 2")
            for i in range(3):
                print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
            return x, y
        else:
            print("Это поле занято")
            return ask()
paso = 0
for i in range(10):
    paso += 1
    if field[0][0] == field[0][1] == field[0][2] != " ":
        print("Победа!!!", A)
        break
    if field[1][0] == field[1][1] == field[1][2] != " ":
        print("Победа!!!", A)
        break
    if field[2][0] == field[2][1] == field[2][2] != " ":
        print("Победа!!!", A)
        break
    if field[0][0] == field[1][0] == field[2][0] != " ":
        print("Победа!!!", A)
        break
    if field[0][1] == field[1][1] == field[2][1] != " ":
        print("Победа!!!", A)
        break
    if field[0][2] == field[1][2] == field[2][2] != " ":
        print("Победа!!!", A)
        break
    if field[0][0] == field[1][1] == field[2][2] != " ":
        print("Победа!!!", A)
        break
    if field[0][2] == field[1][1] == field[2][0] != " ":
        print("Победа!!!", A)
        break
    if paso <= 9:
        if i % 2 == 0:
            A = 'X'
            l = ask()
        else:
            A = 'O'
            l = ask()
    else:
        print("Игра окончена, НЕТ ПОБЕДИТЕЛЯ")
