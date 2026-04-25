import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        in_degree[v] += 1
    
    q = deque()
    for i in range(1, N+1):
        # 첫 주자들
        if in_degree[i] == 0:
            q.append(i)

    ans = []

    while q:
        cur = q.popleft()
        ans.append(cur)
        for nxt in adj[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    
    print(*ans)

if __name__ == "__main__":
    solution()