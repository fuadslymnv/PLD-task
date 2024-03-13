def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def check_draw(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    while True:
        print_board(board)
        print(f"Player {players[turn]}'s turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if is_valid_move(board, row, col):
            board[row][col] = players[turn]
            if check_winner(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn = 1 - turn  
        else:
            print("Invalid move. Try again.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        tic_tac_toe()
    else:
        print("Thanks for playing!")
tic_tac_toe()