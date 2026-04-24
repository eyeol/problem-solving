import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    # N
    boards = [[0]*(N+1)]
    for _ in range(N):
        nums = [0] + list(map(int, input().split()))
        boards.append(nums)

    dp = [[0]*(N+1) for _ in range(N+1)]

    for x in range(1, N+1):
        for y in range(1, N+1):
            dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + boards[x][y]

    for _ in range(M):
        sx, sy, ex, ey = map(int, input().split())
        print(dp[ex][ey] - dp[sx-1][ey] - dp[ex][sy-1] + dp[sx-1][sy-1])


if __name__ == "__main__":
    solution()