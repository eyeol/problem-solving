import sys

input = sys.stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        N = int(input())
        cards = [] # padding
        # 2N 카드 받기
        cards.append([0] + list(map(int, input().split())))
        cards.append([0] + list(map(int, input().split())))

        dp = [[0]*(N+1), [0]*(N+1)]
        # dp[i][0] : i번째에서 위쪽을 뗐을 때 최적값
        # dp[i][1] : i번째에서 아래쪽을 뗐을 때 최적값
        dp[0][1] = cards[0][1]
        dp[1][1] = cards[1][1]

        for i in range(2, N+1):
            # 위에서 뽑기
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + cards[0][i]
            # 아래에서 뽑기
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + cards[1][i]
        
        print(max(dp[0][N], dp[1][N]))


if __name__ == "__main__":
    solution()