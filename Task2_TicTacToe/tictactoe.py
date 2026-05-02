import random

board = [" " for _ in range(9)]

def print_board():
    print("\nBoard:")
    for i in range(3):
        print(board[i*3:(i+1)*3])

def check_winner(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")

    while True:
        print_board()
        
        try:
            move = int(input("Enter position (0-8): "))
        except:
            print("Enter a number!")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if " " not in board:
            print_board()
            print("Draw!")
            break

        ai_move = random.choice([i for i in range(9) if board[i]==" "])
        board[ai_move] = "O"

        if check_winner("O"):
            print_board()
            print("🤖 AI wins!")
            break

play()