import sys

input = sys.stdin.readline
MOD = 1_000_000_000

def solution():
    N = int(input())

    # dp[digit][last][mask]
    # mask: 0~9 중 어떤 숫자가 등장했는지 (비트)
    dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

    # 첫 자리: 1~9
    for d in range(1, 10):
        dp[1][d][1 << d] = 1

    for i in range(1, N):
        for d in range(10):
            for mask in range(1024):
                if dp[i][d][mask] == 0:
                    continue
                for nd in (d - 1, d + 1):
                    if 0 <= nd <= 9:
                        new_mask = mask | (1 << nd)
                        dp[i + 1][nd][new_mask] = (dp[i + 1][nd][new_mask] + dp[i][d][mask]) % MOD

    full = (1 << 10) - 1  # 0~9 모두 등장 = 1111111111
    ans = 0
    for d in range(10):
        ans = (ans + dp[N][d][full]) % MOD

    print(ans)

if __name__ == "__main__":
    solution()