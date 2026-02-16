import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

# DFS 탐색 결과와 BFS 탐색 결과를 출력
# 탐색 결과 출력은 결국 부모 노드를 따라서 복원하면 됨
# 부모 저장하는 배열 사용 <- visited 용도로도 사용

# 방문할 수 있는 정점 여러 개일 때 정점 번호 작은 것 방문 <- adj 배열 정렬해놓으면 됨

def solution():
    N, M, V = map(int, input().split())

    adj = [[] for _ in range(N+1)]

    # adj 배열 만들기
    for _ in range(M):
        u, v = map(int, input().split())
        # undirected graph
        adj[u].append(v)
        adj[v].append(u)

    for row in adj:
        row.sort()
    
    # dfs
    visited = [0 for _ in range(N+1)]
    ans = []

    def dfs(u: int):
        visited[u] = 1
        ans.append(u)

        for v in adj[u]:
            if visited[v] == 0:
                dfs(v)
    
    dfs(V)
    print(*ans)

    # bfs
    visited = [0 for _ in range(N+1)]
    q = deque([V])
    visited[V] = 1
    ans = [V]
    while q:
        u = q.popleft()
        
        for v in adj[u]:
            if visited[v] == 0:
                visited[v] = 1
                q.append(v)
                ans.append(v)
    
    print(*ans)




if __name__ == "__main__":
    solution()