import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)

    idx = [0]
    order = [0] * (V + 1)
    on_stack = [False] * (V + 1)
    stack = []
    result = []

    def dfs(u):
        idx[0] += 1
        order[u] = idx[0]
        low = order[u]
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if order[v] == 0:
                low = min(low, dfs(v))
            elif on_stack[v]:
                low = min(low, order[v])

        if low == order[u]:
            scc = []
            while True:
                t = stack.pop()
                on_stack[t] = False
                scc.append(t)
                if t == u:
                    break
            scc.sort()
            result.append(scc)

        return low

    for i in range(1, V + 1):
        if order[i] == 0:
            dfs(i)

    result.sort(key=lambda x: x[0])
    print(len(result))
    for scc in result:
        print(*scc, -1)

if __name__ == "__main__":
    solution()