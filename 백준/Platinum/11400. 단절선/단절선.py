import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        adj[a].append((b, i))
        adj[b].append((a, i))

    order = [0] * (V + 1)
    low = [0] * (V + 1)
    cnt = [0]
    bridges = []

    def dfs(u, parent_edge):
        cnt[0] += 1
        order[u] = low[u] = cnt[0]

        for v, idx in adj[u]:
            if idx == parent_edge:
                continue
            if order[v] == 0:
                dfs(v, idx)
                low[u] = min(low[u], low[v])
                if low[v] > order[u]:
                    bridges.append((min(u, v), max(u, v)))
            else:
                low[u] = min(low[u], order[v])

    for i in range(1, V + 1):
        if order[i] == 0:
            dfs(i, -1)

    bridges.sort()
    print(len(bridges))
    for a, b in bridges:
        print(a, b)

if __name__ == "__main__":
    solution()