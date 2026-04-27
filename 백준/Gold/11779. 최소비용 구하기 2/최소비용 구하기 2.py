import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def solution():
    N = int(input())
    M = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    S, E = map(int, input().split())

    dist = [INF] * (N + 1)
    prev = [0] * (N + 1)
    dist[S] = 0
    hq = [(0, S)]

    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(hq, (dist[v], v))

    print(dist[E])

    path = []
    cur = E
    while cur != 0:
        path.append(cur)
        cur = prev[cur]

    path.reverse()
    print(len(path))
    print(*path)

if __name__ == "__main__":
    solution()