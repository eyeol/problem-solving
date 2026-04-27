import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(n, adj, start):
    dist = [INF] * (n + 1)
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
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))

    v1, v2 = map(int, input().split())

    d1 = dijkstra(N, adj, 1)
    dv1 = dijkstra(N, adj, v1)
    dv2 = dijkstra(N, adj, v2)

    ans = min(d1[v1] + dv1[v2] + dv2[N],
              d1[v2] + dv2[v1] + dv1[N])

    print(-1 if ans >= INF else ans)

if __name__ == "__main__":
    solution()