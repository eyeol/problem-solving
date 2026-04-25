import sys

input = sys.stdin.readline
INF = float('inf')

def solution():
    N = int(input())
    mat = []
    for _ in range(N):
        r, c = map(int, input().split())
        mat.append((r, c))

    dp = [[0] * N for _ in range(N)]

    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + mat[i][0] * mat[k][1] * mat[j][1]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][N - 1])

if __name__ == "__main__":
    solution()