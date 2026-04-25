import sys
import heapq
from collections import deque

input = sys.stdin.readline
INF = float('inf')

def dijkstra(N, adj, start):
    dist = [INF] * N
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(hq, (dist[v], v))
    return dist

def solution():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        S, D = map(int, input().split())

        adj = [[] for _ in range(N)]
        radj = [[] for _ in range(N)]
        for _ in range(M):
            u, v, w = map(int, input().split())
            adj[u].append([v, w])
            radj[v].append((u, w))

        dist = dijkstra(N, adj, S)

        if dist[D] == INF:
            print(-1)
            continue

        visited = [False] * N
        q = deque([D])
        visited[D] = True
        while q:
            v = q.popleft()
            for u, w in radj[v]:
                if dist[u] + w == dist[v]:
                    for edge in adj[u]:
                        if edge[0] == v and edge[1] == w:
                            edge[1] = INF
                            break
                    if not visited[u]:
                        visited[u] = True
                        q.append(u)

        dist2 = dijkstra(N, adj, S)
        print(dist2[D] if dist2[D] != INF else -1)

if __name__ == "__main__":
    solution()