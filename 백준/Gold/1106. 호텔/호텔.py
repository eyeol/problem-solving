import sys

input = sys.stdin.readline

def solution():
    C, N = map(int, input().split())
    cities = []
    for _ in range(N):
        cost, people = map(int, input().split())
        cities.append((cost, people))

    INF = float('inf')
    # C명 이상 확보할 수도 있으니 넉넉하게
    dp = [INF] * (C + 101)
    dp[0] = 0

    for cost, people in cities:
        for j in range(people, C + 101):
            if dp[j - people] != INF:
                dp[j] = min(dp[j], dp[j - people] + cost)

    print(min(dp[C:]))

if __name__ == "__main__":
    solution()