import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    adj = [[] for _ in range(N+1)]

    # adj list
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    def dfs(s: int):
        visited = [0]*(N+1)
        visited[s] = 1

        stack = [(s, 0)]
        far_node, far_dist = s, 0

        while stack:
            u, d = stack.pop()
            if d > far_dist:
                far_node, far_dist = u, d
            
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    stack.append((v, d + w))
            
        return far_node, far_dist
    
    v, _ = dfs(1)
    _, ans = dfs(v)

    print(ans)
    

if __name__ == "__main__":
    solution()