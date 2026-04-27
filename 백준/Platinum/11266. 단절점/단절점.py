import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    order = [0] * (V + 1)
    low = [0] * (V + 1)
    cnt = [0]
    cut = set()

    def dfs(u, parent):
        cnt[0] += 1
        order[u] = low[u] = cnt[0]
        child = 0

        for v in adj[u]:
            if v == parent:
                continue
            if order[v] == 0:
                child += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if parent == -1 and child >= 2:
                    cut.add(u)
                if parent != -1 and low[v] >= order[u]:
                    cut.add(u)
            else:
                low[u] = min(low[u], order[v])

        return low[u]

    for i in range(1, V + 1):
        if order[i] == 0:
            dfs(i, -1)

    result = sorted(cut)
    print(len(result))
    if result:
        print(*result)

if __name__ == "__main__":
    solution()