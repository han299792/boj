import sys

data = sys.stdin.read().split()

N = int(data[0])
nums = list(map(int, data[1:]))

T = [nums[i:i+3] for i in range(0, 3*N, 3)]
dp = [[float('inf')] * 3 for _ in range(N)]
dp[0] = T[0]
# dp[n][k] n 번째 집을 k 색으로 칠할 때 최소 비용
for n in range(1, N):
    dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + T[n][0]
    dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + T[n][1]
    dp[n][2] = min(dp[n-1][1], dp[n-1][0]) + T[n][2]

print(min(dp[N-1]))   

#----------------------------------------------------------------
import sys

# 빠른 입력
data = sys.stdin.read().split()

N = int(data[0])
nums = list(map(int, data[1:]))

# 각 집의 비용 테이블 생성
T = [nums[i:i+3] for i in range(0, 3 * N, 3)]

# 이전 집까지의 최소 비용 (초기 상태 = 첫 번째 집)
prev = T[0]

# DP 점화식 적용
for n in range(1, N):
    curr = [
        T[n][0] + min(prev[1], prev[2]),  # 현재 집을 빨강으로 칠할 때
        T[n][1] + min(prev[0], prev[2]),  # 현재 집을 초록으로 칠할 때
        T[n][2] + min(prev[0], prev[1])   # 현재 집을 파랑으로 칠할 때
    ]
    prev = curr  # 다음 반복에서 이전 상태로 사용

# 마지막 집까지 칠했을 때 최소 비용 출력
print(min(prev))
