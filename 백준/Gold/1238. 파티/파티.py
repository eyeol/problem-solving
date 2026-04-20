import heapq
import sys

input = sys.stdin.readline

def solution():

    N, M, X = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    radj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        radj[v].append((u, w))

    # X에서 출발해서 노드별 도달하는 최단거리를 구해야 함 = BFS
    # 그런데 간선에 길이 정보가 있음 = 우선순위 큐로 다익스트라

    
    
    def dijkstra(u):
        min_dist = [float("INF")] * (N+1)
        h = [(0, u)]
        min_dist[u] = 0
        
        while h:
            d, u = heapq.heappop(h)
            if d > min_dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < min_dist[v]:
                    min_dist[v] = nd
                    heapq.heappush(h, (nd, v))

        return min_dist
    
    def r_dijkstra(u):
        min_dist = [float("INF")] * (N+1)
        h = [(0, u)]
        min_dist[u] = 0

        while h:
            d, u = heapq.heappop(h)
            if d > min_dist[u]:
                continue
            for v, w in radj[u]:
                nd = d + w
                if nd < min_dist[v]:
                    min_dist[v] = nd
                    heapq.heappush(h, (nd, v))

        return min_dist
    
    max_val = 0

    dist_go = dijkstra(X)
    dist_come = r_dijkstra(X)

    for i in range(1, N+1):
        if dist_go[i] != float("INF") and dist_come[i] != float("INF"):
            max_val = max(max_val, dist_go[i] + dist_come[i])
    
    print(max_val)


if __name__ == "__main__":
    solution()