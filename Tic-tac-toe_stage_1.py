
board = list("_________")
move = 0
win = False

def printer():
    #print(' '.join(board[0:6:])
    print("---------")
    print("|", ' '.join(board[2:9:3]), "|")
    print("|", ' '.join(board[1:8:3]), "|")
    print("|", ' '.join(board[0:7:3]), "|")
    print("---------")


def check_win():
    win_coord = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] and (board[each[0]] == "X" or board[each[0]] == "O"):
            return board[each[0]]
    return False


def check_correct(token):
    valid = False
    while not valid:
        you_coord = input("Enter the coordinates:").split()
        i, j = you_coord[0], you_coord[1]
        if i.isdigit() and j.isdigit():
            i, j = int(i), int(j)
            if i in range(1,4) and j in range(1, 4):
                coord = (i - 1) * 3 + j - 1
                if board[coord] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    board[coord] = token
                    valid = True
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

while not win:
    printer()
    if move % 2 == 0:
        check_correct("X")
    else:
        check_correct("O")
    move += 1
    if move > 4:
        tmp = check_win()
        if tmp:
            printer()
            print(tmp, "wins")
            win = True
        elif move == 9:
            printer()
            print("Draw")
            win = True