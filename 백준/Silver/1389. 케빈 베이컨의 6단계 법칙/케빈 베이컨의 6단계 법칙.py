import sys
from collections import deque

input = sys.stdin.readline


def solution():

    N, M = map(int, input().split())

    # adj matrix ; 최대 100x100
    adj = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    def bfs(s: int):
        dist = [0] * (N+1)
        visited = [0] * (N+1)
        q = deque([s])
        visited[s] = 1

        while q:
            cur = q.popleft()
            pos = dist[cur]
            for nxt in adj[cur]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    dist[nxt] += (pos + 1)
                    q.append(nxt)
        return sum(dist)
    
    min_val = 1000_000_000
    ans = 0
    for i in range(N):
        result = bfs(i+1)
        if result < min_val:
            min_val = result
            ans = i+1
    
    print(ans)


if __name__ == "__main__":
    solution()
