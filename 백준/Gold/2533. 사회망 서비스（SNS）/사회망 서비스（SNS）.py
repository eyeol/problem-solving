import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # BFS로 부모/순서 구하기 (반복문 DP용)
    parent = [0] * (N + 1)
    order = []
    visited = [False] * (N + 1)
    visited[1] = True
    q = deque([1])
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    dp = [[0, 0] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][1] = 1  # 자기 자신이 얼리어답터

    # 리프부터 루트 방향으로 (역순)
    for u in reversed(order):
        p = parent[u]
        if p == 0:
            continue
        dp[p][0] += dp[u][1]  # 부모가 아니면 자식은 반드시 얼리어답터
        dp[p][1] += min(dp[u][0], dp[u][1])  # 부모가 얼리어답터면 자식은 둘 다 가능

    print(min(dp[1][0], dp[1][1]))

if __name__ == "__main__":
    solution()