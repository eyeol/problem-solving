import sys

input = sys.stdin.readline

def solution():
    N = int(input())

    triangle = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = triangle[0][0]

    for i in range(1, N):
        for j in range(i+1):
            # 맨 왼쪽
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 맨 오른쪽
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    print(max(dp[N-1]))


if __name__ == "__main__":
    solution()