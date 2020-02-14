import random
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
current_player = 'X'
count = 0
winner = False


def print_board():
    print(f'\nCurrent Player is {current_player}')
    print('==================\n')
    for rows in reversed(board):
        print(rows)


print_board()


def valid_check(x, y):
    if -1 < x < 3 and -1 < y < 3:
        if board[y][x] == '_':
            return True
        else:
            print('space taken')
    else:
        print('input between 0 and 2')


def winner_player():
    big_list = [board[0], board[1], board[2]]
    for i in range(3):
        col = []
        for j in range(3):
            col.append(board[j][i])
        big_list.append(col)

    diag_1 = [board[2][2], board[1][1], board[0][0]]
    diag_2 = [board[2][0], board[1][1], board[0][2]]
    big_list.append(diag_1)
    big_list.append(diag_2)

    for triplet in big_list:
        if triplet.count('X') == 3 or triplet.count('O') == 3:
            print(f'\n{current_player} has wonnered!!')
            return True
        elif count == 9:
            print('\nA flippin draw!')
            return True


def computer_smart():
    win_combos = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    new_coords = []
    for combo in win_combos:
        win_condition = []
        for i in combo:
            win_condition.append(board[i[0]][i[1]])
        win_condition = ''.join(win_condition)
        if win_condition.count('_') == 1:
            if win_condition.count('X') == 2:
                new_coords = combo[win_condition.index('_')]
                print(new_coords)
            elif win_condition.count('O') == 2:
                return(combo[win_condition.index('_')])
        elif ((win_condition.count('_') > 1) and new_coords == []):
            new_coords = [random.randint(0, 2), random.randint(0, 2)]
    return new_coords


def change_player(player):
    global current_player
    if player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def gameplay(X, Y):
    global count
    if valid_check(X, Y):
        board[Y][X] = current_player
        print_board()
        count += 1
        if winner_player():
            return True
        change_player(current_player)


while not winner:
    if current_player == 'X':
        X = int(input('Input X coordinate'))
        Y = int(input('Input Y coordinate'))
        if gameplay(X, Y):
            winner = True
            break
    else:
        com_coords = computer_smart()
        X = com_coords[1]
        Y = com_coords[0]
        if gameplay(X, Y):
            winner = True
            break
