grid = [list(map(int, input().split())) for _ in range(9)]

max_val = -1
row = col = 0

for i in range(9):
    for j in range(9):
        if grid[i][j] > max_val:
            max_val = grid[i][j]
            row = i + 1 
            col = j + 1

print(max_val)
print(f"{row} {col}")
