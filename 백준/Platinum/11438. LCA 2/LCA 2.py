import sys
from collections import deque

input = sys.stdin.readline
LOG = 21

def solution():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    depth = [0] * (N + 1)
    parent = [[0] * (N + 1) for _ in range(LOG)]
    visited = [False] * (N + 1)

    visited[1] = True
    q = deque([1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent[0][v] = u
                q.append(v)

    for k in range(1, LOG):
        for v in range(1, N + 1):
            parent[k][v] = parent[k - 1][parent[k - 1][v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                u = parent[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        return parent[0][u]

    M = int(input())
    out = []
    for _ in range(M):
        u, v = map(int, input().split())
        out.append(str(lca(u, v)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solution()