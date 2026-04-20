import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())

    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [0] * (N+1)
    parent = [0] * (N+1)

    q = deque([1])
    visited[1] = 1
    parent[1] = -1

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = 1
                q.append(v)

    for i in range(2, N+1):
        print(parent[i])


if __name__ == "__main__":
    solution()