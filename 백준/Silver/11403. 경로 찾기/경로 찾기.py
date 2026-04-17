import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N = int(input())

    # 방향 그래프의 인접 행렬이 주어짐
    # i에서 j로 가는 길이 양수의 경로가 있는지 확인
    adj = []
    for _ in range(N):
        a = list(map(int, input().split()))
        adj.append(a)
    
    reachable = [[0] * N for _ in range(N)]
    
    def bfs(s: int):
        visited = [0]*N

        q = deque([s])
        while q:
            u = q.popleft()
            for v, connected in enumerate(adj[u]):
                # 연결되어있고, 아직 방문하지 않았다면 방문
                if connected and not visited[v]:
                    reachable[s][v] = 1
                    visited[v] = 1
                    q.append(v)

    for i in range(N):
        bfs(i)
    
    for row in reachable:
        print(*row)



if __name__ == "__main__":
    solution()
