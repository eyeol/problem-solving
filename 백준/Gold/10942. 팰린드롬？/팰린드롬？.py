import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    dp = [[False] * N for _ in range(N)]

    # 길이 1
    for i in range(N):
        dp[i][i] = True

    # 길이 2
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = True

    # 길이 3 이상
    for length in range(3, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            if arr[i] == arr[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    M = int(input())
    out = []
    for _ in range(M):
        s, e = map(int, input().split())
        out.append('1' if dp[s - 1][e - 1] else '0')

    print('\n'.join(out))

if __name__ == "__main__":
    solution()