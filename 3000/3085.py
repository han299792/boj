import sys
data = sys.stdin.read().split()

N = int(data[0])
board = [list(row) for row in data[1:]]

def check(board, N):
    max_cnt = 0
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt        
    
max_candies = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            max_candies = max(max_candies, check(board, N))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            max_candies = max(max_candies, check(board, N))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_candies)
        
        