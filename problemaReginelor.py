def este_valid(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row -1:
            return False
        return True

def rezolvare_n_queens(n, board=[], row=0):
    if row == n:
        print(board)
        return
    for col in range(n):
        if este_valid(board, row, col, n):
            rezolvare_n_queens(n, board + [col], row + 1)

rezolvare_n_queens(4)