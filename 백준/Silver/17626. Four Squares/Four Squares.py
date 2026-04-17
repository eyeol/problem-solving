import sys

input = sys.stdin.readline

def solution():
    N = int(input())

    # 제곱수 하나를 빼고 남은 수도 무언가의 제곱수의 합으로 나타낼 수 있다
    # 부분 문제가 나오기 때문에 dp 사용

    dp = [0] * (N+1)

    for i in range(1, N+1):
        dp[i] = i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1

    print(dp[N])



if __name__ == "__main__":
    solution()
