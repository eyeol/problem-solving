import sys
from collections import deque

input = sys.stdin.readline
LOG = 17

def solution():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    depth = [0] * (N + 1)
    dist = [0] * (N + 1)
    parent = [[0] * (N + 1) for _ in range(LOG)]
    visited = [False] * (N + 1)

    # BFS로 depth, dist, parent 구하기
    visited[1] = True
    q = deque([1])
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                dist[v] = dist[u] + w
                parent[0][v] = u
                q.append(v)

    # 희소 배열 채우기
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
        l = lca(u, v)
        out.append(str(dist[u] + dist[v] - 2 * dist[l]))
    print('\n'.join(out))

if __name__ == "__main__":
    solution()