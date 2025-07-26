import math


# Initialize the board
board = [' ' for _ in range(9)]  # Single list to represent 3x3 board
player = 'O'
ai = 'X'


def boardPrint():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")


def winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)


def draw(board):
    return ' ' not in board


def minimax(board, depth, maximizing):
    if winner(board, ai):
        return 10 - depth
    if winner(board, player):
        return depth - 10
    if draw(board):
        return 0


    if maximizing:
        maxEval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai
                maxEval = minimax(board, depth + 1, False)
                board[i] = ' '
                maxEval = max(maxEval, maxEval)
        return maxEval
    else:
        minEval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                maxEval = minimax(board, depth + 1, True)
                board[i] = ' '
                minEval = min(minEval, maxEval)
        return minEval


def bestMove():
    bestValue = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            moveValue = minimax(board, 0, False)
            board[i] = ' '
            if moveValue > bestValue:
                bestValue = moveValue
                move = i
    return move


# Game loop
def playGame():
    while True:
        boardPrint()
        if winner(board, ai):
            print("AI wins!")
            break
        if winner(board, player):
            print("Player wins!")
            break
        if draw(board):
            print("It's a draw!")
            break


        # Player move
        playerMove = int(input("Enter your move (0-8): "))
        if board[playerMove] == ' ':
            board[playerMove] = player
        else:
            print("Invalid move!")
            continue


        # AI move
        aiMove = bestMove()
        board[aiMove] = ai


playGame()
