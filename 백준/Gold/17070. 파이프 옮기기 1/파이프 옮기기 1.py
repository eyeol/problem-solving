import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    # 0: 가로, 1: 세로, 2: 대각선
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    dp[0][1][0] = 1

    for i in range(N):
        for j in range(2, N):
            if board[i][j] == 1:
                continue
            # 가로로 도착: 이전이 가로 또는 대각선
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            # 세로로 도착: 이전이 세로 또는 대각선
            if i > 0:
                dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            # 대각선으로 도착: 이전이 가로, 세로, 대각선 + 주변 벽 체크
            if i > 0 and board[i - 1][j] == 0 and board[i][j - 1] == 0:
                dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

    print(sum(dp[N - 1][N - 1]))

if __name__ == "__main__":
    solution()