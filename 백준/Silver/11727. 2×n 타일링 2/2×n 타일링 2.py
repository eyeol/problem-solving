import sys

input = sys.stdin.readline

def solution():
    N = int(input())

    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3

    if N <= 2:
        print(dp[N])
        return

    for i in range(3, 1001): # 3 to 1000
        dp[i] = 2 * dp[i-2] + dp[i-1]
    
    print(dp[N] % 10007)

if __name__ == "__main__":
    solution()
