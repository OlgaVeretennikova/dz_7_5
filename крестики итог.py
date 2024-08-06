def greet():
    print('--------------------')
    print('Игра крестики-нолики')
    print('      началась      ')
    print('--------------------')
    print(' формат ввода: x y  ')
    print(' x - номер строки   ')
    print(' y - номер столбца  ')


def print_board():
    print(f"  | 0 | 1 | 2 |")
    print("----------------")
    for i in range(3):
        print(f"{i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("----------------")
    print()

def ask():
    while True:
        cords = input('Ваш ход: ').split()

        if len(cords) != 2:
            print('Введите 2 координаты')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона')
            continue

        if board[x][y] != ' ':
            print('Клетка занята')
            continue

        return x, y

def win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2,0)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]

        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != " ":
            print (f'Выиграл {board[a[0]][a[1]]}')
            return True
    return False

greet()
board = [[" "] * 3 for i in range(3)]
num_chod = 0
while True:
    num_chod += 1
    print_board()
    if num_chod % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if num_chod % 2 == 1:
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'

    if win():
        break

    if num_chod == 9:
        print('Ничья')
        break








