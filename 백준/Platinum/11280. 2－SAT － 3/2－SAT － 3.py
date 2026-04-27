import sys
sys.setrecursionlimit(400000)

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    size = 2 * N

    # x → x*2, ¬x → x*2+1
    def pos(x):
        if x > 0:
            return (x - 1) * 2
        else:
            return (-x - 1) * 2 + 1

    def neg(a):
        return a ^ 1

    adj = [[] for _ in range(size)]

    for _ in range(M):
        a, b = map(int, input().split())
        pa, pb = pos(a), pos(b)
        # (a ∨ b) → (¬a → b) and (¬b → a)
        adj[neg(pa)].append(pb)
        adj[neg(pb)].append(pa)

    # 타잔 SCC
    order = [0] * size
    low = [0] * size
    on_stack = [False] * size
    stack = []
    cnt = [0]
    scc_id = [-1] * size

    def dfs(u):
        cnt[0] += 1
        order[u] = low[u] = cnt[0]
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if order[v] == 0:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], order[v])

        if low[u] == order[u]:
            while True:
                t = stack.pop()
                on_stack[t] = False
                scc_id[t] = u
                if t == u:
                    break

    for i in range(size):
        if order[i] == 0:
            dfs(i)

    for i in range(N):
        if scc_id[i * 2] == scc_id[i * 2 + 1]:
            print(0)
            return

    print(1)

if __name__ == "__main__":
    solution()