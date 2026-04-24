import sys

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    bags = []
    for _ in range(N):
        w, v = map(int, input().split())
        bags.append((w, v))

    dp = [[0]*(K+1) for _ in range(N+1)]

    # 고려할 물건 인덱스
    for i in range(1, N+1):
        w, v = bags[i-1]
        # 남은 공간 인덱스
        for j in range(K+1):
            if w > j: # 남은 공간이 부족하면 패스
                dp[i][j] = dp[i-1][j]
            else: # 넣을 공간이 있다면
                # 이 물건을 넣지 않고 j만큼 남았을 때와
                # 이 물건을 넣고 j만큼 남았을 때의 최적값 비교
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        
    print(dp[N][K])


if __name__ == "__main__":
    solution()