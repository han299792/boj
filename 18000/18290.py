import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# N: 행, M: 열, K: 선택할 칸의 개수
N, M, K = map(int, input().split())

# N x M 격자판 입력받기
grid = [list(map(int, input().split())) for _ in range(N)]

# 이미 선택한 칸을 표시하기 위한 배열
# visited[i][j]가 True이면 (i, j)는 현재 조합에 포함된 것
visited = [[False] * M for _ in range(N)]

# 최종 결과를 저장할 변수 (최소값으로 초기화)
max_sum = -10001 * K # 나올 수 있는 최소값보다 더 작게 설정

# 상하좌우 이동을 위한 dx, dy
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 백트래킹을 수행하는 재귀 함수
# (px, py): 이전에 마지막으로 선택한 칸의 위치 (중복 방지용)
# count: 현재까지 선택한 칸의 개수
# current_sum: 현재까지 선택한 칸들의 합
def solve(px, py, count, current_sum):
    global max_sum

    # 1. 종료 조건: K개의 칸을 모두 선택했다면
    if count == K:
        # 현재까지의 합이 최대 합보다 크면 갱신
        if current_sum > max_sum:
            max_sum = current_sum
        return # 탐색 종료

    # 2. 재귀 호출: 다음 칸을 선택하러 이동
    # 중복된 조합을 피하기 위해 이전에 선택한 칸(px, py)부터 탐색 시작
    for i in range(px, N):
        # 같은 행(i==px)이면 이전 열(py) 다음부터, 다른 행이면 0번 열부터
        start_j = py if i == px else 0
        for j in range(start_j, M):
            
            # (i, j) 칸이 이미 선택되었다면 건너뜀
            if visited[i][j]:
                continue

            # (i, j) 칸의 상하좌우에 이미 선택된 칸이 있는지 확인
            is_adjacent = False
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                # 격자판 범위 안이라면
                if 0 <= nx < N and 0 <= ny < M:
                    # 인접한 칸이 이미 선택되었다면
                    if visited[nx][ny]:
                        is_adjacent = True
                        break
            
            # 인접한 칸이 없다면, (i, j)를 선택할 수 있음
            if not is_adjacent:
                visited[i][j] = True  # (i, j)를 선택했다고 표시
                solve(i, j, count + 1, current_sum + grid[i][j]) # 다음 칸 선택하러 재귀 호출
                visited[i][j] = False # ★★★ 돌아온 후, (i, j) 선택을 취소 (백트래킹)


# (0, 0) 위치, 0개의 칸 선택, 합 0으로 탐색 시작
solve(0, 0, 0, 0)

# 최종 결과 출력
print(max_sum)