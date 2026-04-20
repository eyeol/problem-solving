import sys

input = sys.stdin.readline

def solution():

    V = int(input())
    adj = [[] for _ in range(V+1)]
    
    ## 인접 리스트 생성
    for _ in range(V):
        info = list(map(int, input().split()))
        i = 1
        while i < len(info)-1:
            adj[info[0]].append((info[i], info[i+1]))
            i += 2

    def dfs(start):
        visited = [0] * (V+1)
        visited[start] = 1

        stack = [(start, 0)]
        far_node, far_dist = start, 0

        while stack:
            u, d = stack.pop()
            if d > far_dist:
                far_node, far_dist = u, d
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    stack.append((v, d + w))
        
        return far_node, far_dist
    
    a, _ = dfs(1)
    _, ans = dfs(a)

    print(ans)


if __name__ == "__main__":
    solution()

