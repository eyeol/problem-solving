import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    
    stairs = [0]
    for _ in range(N):
        stairs.append(int(input()))

    # 계단 1개면 그대로 반환
    if N <= 2:
        print(sum(stairs))
        return

    dp = [[0, 0] for _ in range(N+1)]

    # 시작점 출발
    dp[1][0] = dp[0][0] + stairs[1]
    
    # 두번째
    dp[2][0] = dp[1][0] + stairs[2]
    dp[2][1] = dp[0][0] + stairs[2]
    
    for i in range(3, N+1): # 2부터 N
        # 한칸 뛰어서 i에 오는 경우
        # dp[i-1][0]에서 오면 안됨
        dp[i][0] = max(dp[i][0], dp[i-1][1] + stairs[i])

        # 두칸 뛰어서 i에 오는 경우
        # 어디서 오든 상관 없음
        dp[i][1] = max(dp[i][1], dp[i-2][0] + stairs[i])
        dp[i][1] = max(dp[i][1], dp[i-2][1] + stairs[i])

    print(max(dp[N][0], dp[N][1]))

if __name__ == "__main__":
    solution()
