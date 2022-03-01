def hello():
    print()
    print("             Игра крестики-нолики")
    print()
    print("Чтобы сыграть, введите координаты x и y через пробел")
    print("x -строка; y -столбец")
    print()


field = [[" "] * 3 for i in range(3)]

def show():
    print("     0 | 1 | 2  ")
    print("   ------------- ")
    for j in range(3):
        cell = " | ".join(field[j])
        print(f" {j} | {cell} |")
        print("   ------------- ")

def start_game():
    while True:
        cords = input("Сделайте ход: ").split()

        if len(cords) != 2:
            print("Необходимо ввести 2 координаты!")
            continue

        x, y = cords

        if not x.isdigit() or not y.isdigit():
            print("Введите число!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Такой клетки нет")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

def win():
    win_cords = (((0, 0), (0, 1), (0, 2)),
                 ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)),
                 ((0, 0), (1, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)),
                 ((0, 2), (1, 2), (2, 2)))

    for cord in win_cords:
        symbol = []
        for k in cord:
            symbol.append(field[k[0]][k[1]])
        if symbol == ["X", "X", "X"]:
            print("Выиграл 'X'")
            return True
        if symbol == ["0", "0", "0"]:
            print("Выиграл '0''")
            return True
    return False
hello()

num = 0
for go in range(9):
    show()
    num += 1
    if num % 2 == 1:
        print("Ходит: 'X'")
    else:
        print("Ходит: '0'")

    x, y = start_game()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if num == 9:
        print(" Ничья!")
        break

