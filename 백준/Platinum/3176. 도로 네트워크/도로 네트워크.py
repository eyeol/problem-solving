import sys
from collections import deque

input = sys.stdin.readline
LOG = 17
INF = float('inf')

def solution():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    depth = [0] * (N + 1)
    parent = [[0] * (N + 1) for _ in range(LOG)]
    min_w = [[INF] * (N + 1) for _ in range(LOG)]
    max_w = [[0] * (N + 1) for _ in range(LOG)]
    visited = [False] * (N + 1)

    visited[1] = True
    q = deque([1])
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent[0][v] = u
                min_w[0][v] = w
                max_w[0][v] = w
                q.append(v)

    for k in range(1, LOG):
        for v in range(1, N + 1):
            parent[k][v] = parent[k - 1][parent[k - 1][v]]
            min_w[k][v] = min(min_w[k - 1][v], min_w[k - 1][parent[k - 1][v]])
            max_w[k][v] = max(max_w[k - 1][v], max_w[k - 1][parent[k - 1][v]])

    def query(u, v):
        res_min = INF
        res_max = 0

        if depth[u] < depth[v]:
            u, v = v, u

        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                res_min = min(res_min, min_w[k][u])
                res_max = max(res_max, max_w[k][u])
                u = parent[k][u]

        if u == v:
            return res_min, res_max

        for k in range(LOG - 1, -1, -1):
            if parent[k][u] != parent[k][v]:
                res_min = min(res_min, min_w[k][u], min_w[k][v])
                res_max = max(res_max, max_w[k][u], max_w[k][v])
                u = parent[k][u]
                v = parent[k][v]

        res_min = min(res_min, min_w[0][u], min_w[0][v])
        res_max = max(res_max, max_w[0][u], max_w[0][v])
        return res_min, res_max

    K = int(input())
    out = []
    for _ in range(K):
        u, v = map(int, input().split())
        mn, mx = query(u, v)
        out.append(f"{mn} {mx}")
    print('\n'.join(out))

if __name__ == "__main__":
    solution()