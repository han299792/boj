import sys

# 빠른 입출력을 위해 사용
input = sys.stdin.readline

def solve(K, P):
    # 1. 누적 합(Prefix Sum) 계산
    # 구간의 파일 크기 합을 O(1)에 구하기 위해 사용
    # S[x]는 P[0]부터 P[x-1]까지의 합
    S = [0] * (K + 1)
    for idx in range(1, K + 1):
        S[idx] = S[idx-1] + P[idx-1]

    # 2. DP 테이블 초기화
    # c[i][j] : i번 파일부터 j번 파일까지 합치는 데 드는 최소 비용
    c = [[0] * K for _ in range(K)]

    # 3. DP 진행 (Bottom-Up)
    # L: 합치려는 구간의 길이 (파일 개수, 2개부터 K개까지)
    for L in range(2, K + 1):
        # i: 구간의 시작 인덱스
        for i in range(K - L + 1):
            j = i + L - 1  # 구간의 끝 인덱스
            
            # 최솟값을 구하기 위해 초기값을 무한대로 설정
            c[i][j] = sys.maxsize
            
            # 현재 구간(i~j)의 파일 크기 총합 (이번 병합 비용)
            # 누적 합 배열을 이용해 계산: S[j+1] - S[i]
            current_merge_cost = S[j+1] - S[i]

            # k: 구간을 나누는 분기점 (i <= k < j)
            # c[i][j] = min(왼쪽구간비용 + 오른쪽구간비용) + 이번 병합 비용
            for k in range(i, j):
                temp_cost = c[i][k] + c[k+1][j] + current_merge_cost
                if temp_cost < c[i][j]:
                    c[i][j] = temp_cost

    # 0번부터 K-1번(전체)까지 합치는 최소 비용 반환
    return c[0][K-1]

# 테스트 케이스 처리
T = int(input().strip())

for _ in range(T):
    K = int(input().strip())
    P = list(map(int, input().split()))
    print(solve(K, P))