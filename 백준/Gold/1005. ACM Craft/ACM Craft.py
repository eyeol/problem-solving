import sys
from collections import deque

input = sys.stdin.readline

def solution():
    T = int(input())
    
    for _ in range(T):
        N, K = map(int, input().split())
        cost = [0] + list(map(int, input().split()))

        adj = [[] for _ in range(N+1)]
        in_degree = [0] *(N+1)

        for _ in range(K):
            u, v = map(int, input().split())
            adj[u].append(v)
            in_degree[v] += 1

        W = int(input())

        dp = [0] * (N+1)

        q = deque()
        for i in range(1, N+1):
            if in_degree[i] == 0:
                dp[i] = cost[i]
                q.append(i)
        
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                dp[nxt] = max(dp[nxt], dp[cur] + cost[nxt])
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        
        print(dp[W])


if __name__ == "__main__":
    solution()