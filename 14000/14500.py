import sys

N, M = map(int, sys.stdin.readline().split())

nums = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    nums.append(row)
    
#청록색
cnt_max = 0
for _ in range(N):
    for i in range(0, M-3, 1):
        sum = row[i] + row[i+1] + row[i+2] + row[i+3]
        cnt_max = max(cnt_max, sum)
for i in range(N-3):
    for j in range(M):
        sum = nums[i][j] + nums[i+1][j] + nums[i+2][j] + nums[i+3][j]
        cnt_max = max(cnt_max, sum)
     
for i in range(N-1):
    for j in range(M-1):
        sum = nums[i][j] + nums[i][j+1] + nums[i+1][j] + nums[i+1][j+1]
        cnt_max = max(cnt_max, sum)
        
for i in range(N-2):
    for j in range(M-1):
        sum_1 = nums[i][j] + nums[i+1][j] + nums[i+2][j] + nums[i+2][j+1]
        sum_2 = nums[i][j+1] + nums[i+1][j] + nums[i+2][j] + nums[i+2][j]
        sum_3 = nums[i][j] + nums[i+1][j+1] + nums[i+2][j+1] + nums[i+2][j+1]
        sum_4 = nums[i][j+1] + nums[i+1][j+1] + nums[i+2][j+1] + nums[i+2][j]
        cnt_max = max(cnt_max, sum_1, sum_2, sum_3, sum_4)
 
for i in range(N-1):
    for j in range(M-2):
        sum_1 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j]
        sum_2 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j+1]
        sum_3 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j+1]
        sum_4 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j+1]
        cnt_max = max(cnt_max, sum)

        
for i in range(N-2):
    for j in range(M-1):
        sum = nums[i][j] + nums[i+1][j] + nums[i+1][j+1] + nums[i+2][j+1]
        cnt_max = max(cnt_max, sum)
        
for i in range(N-1):
    for j in range(M-2):
        sum = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j+1]
        cnt_max = max(cnt_max, sum)

print(cnt_max)