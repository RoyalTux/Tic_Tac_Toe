X = "X"
O = "O"
EMPTY = " "
TIE = "draw"
NUM_SQUARES = 10

#выводим название игры в начале
def game_name():
    print("\n\t\t\tThe game - Tic Tac Toe")

#функция для задания вопроса о первом ходе
def who_first(question):
    answer = None
    while answer not in ("y", "n"):
        answer = input(question).lower()
    return answer

#выбираем кто первый будет ходить
def pieces():
    go_first = who_first("Do you want be first? (y/n): ")
    if go_first == "y":
        print("\nYou'll play as X!")
        human = X
        computer = O
    else:
        print("\nComputer's first turn!")
        computer = X
        human = O
    return computer, human

#вводим одно из чисел (1-9) для выбора ячейки
def ask_number(question, low, high):
    answer = None
    while answer not in range(low, high):
        answer = int(input(question))
    return answer

#делаем игровое поле
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#рисуем поле в консоли
def display_board(board):
    print("\n\t", board[7], "|", board[8], "|", board[9])
    print("\t", "---------")
    print("\t", board[4], "|", board[5], "|", board[6])
    print("\t", "---------")
    print("\t", board[1], "|", board[2], "|", board[3], "\n")

#делаем список доступных ходов
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

#вычисляем победителя
def winner(board):
    WAYS_TO_WIN = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9),
                   (3, 6, 9),
                   (1, 4, 7),
                   (2, 5, 8),
                   (1, 5, 9),
                   (3, 5, 7))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

#ход игрока
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Your turn! Shoose one of this fields(1 - 9):", 1, NUM_SQUARES)
        if move not in legal:
            print("\nError! This field isn't empty!\n")
    return move

#ход компьютера
def computer_move(board, computer, human):
    # делаем копию
    board = board[:]
    # лучшие ходы
    BEST_MOVES = (5, 1, 3, 7, 9, 2, 4, 6, 8)
    # если пк выигрывает
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    # если игрок выигрывает то блокируем ход
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    # если ничья то выбираем квадрат из лучших
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

#переключаем ходы с Х на О и наоборот
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#выводим в консоль инфу о том кто победил
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "Winner!\n")
    else:
        print("Draw\n")

    if the_winner == computer:
        print("You Lose! Game over!")

    elif the_winner == human:
        print("You Won! Congratulations!\n")

    elif the_winner == TIE:
       print("It's a Draw...")

#основная функция
def main():
    game_name()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
