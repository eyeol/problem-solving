import heapq
import sys

input = sys.stdin.readline

def solution():

    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    # 시작점
    s = int(input())

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    s_dist = [float("inf")] * (V+1)
    s_dist[s] = 0

    pq = [(0, s)]

    while pq:
        dist, u = heapq.heappop(pq)
        
        # 최단거리 갱신이 아니면 버리기
        if dist > s_dist[u]:
            continue

        for v, w in adj[u]:
            n_dist = dist + w
            # 기존 거리보다 짧다면
            if n_dist < s_dist[v]:
                s_dist[v] = n_dist
                heapq.heappush(pq, (n_dist, v))
    
    for i in range(1, V+1):
        if s_dist[i] == float("inf"):
            print("INF")
        else:
            print(s_dist[i])


if __name__ == "__main__":
    solution()

