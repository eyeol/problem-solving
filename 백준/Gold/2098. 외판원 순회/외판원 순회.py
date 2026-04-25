import sys

input = sys.stdin.readline
INF = float('inf')

def solution():
    N = int(input())
    W = []
    for _ in range(N):
        W.append(list(map(int, input().split())))

    full = (1 << N) - 1
    dp = [[INF] * (1 << N) for _ in range(N)]

    # 시작: 0번 도시에서 출발
    dp[0][1] = 0

    for visited in range(1, 1 << N):
        for cur in range(N):
            if dp[cur][visited] == INF:
                continue
            for nxt in range(N):
                if visited & (1 << nxt) or W[cur][nxt] == 0:
                    continue
                nv = visited | (1 << nxt)
                dp[nxt][nv] = min(dp[nxt][nv], dp[cur][visited] + W[cur][nxt])

    # 모든 도시 방문 후 0번으로 돌아오는 최소 비용
    ans = INF
    for cur in range(1, N):
        if W[cur][0] != 0:
            ans = min(ans, dp[cur][full] + W[cur][0])

    print(ans)

if __name__ == "__main__":
    solution()