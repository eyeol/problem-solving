import sys

input = sys.stdin.readline

def solution():
    A = input().strip()
    B = input().strip()
    n, m = len(A), len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][m])

    # 역추적
    if dp[n][m] == 0:
        return

    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(''.join(reversed(result)))

if __name__ == "__main__":
    solution()