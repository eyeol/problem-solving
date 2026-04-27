import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    size = 2 * N

    def pos(x):
        if x > 0:
            return (x - 1) * 2
        else:
            return (-x - 1) * 2 + 1

    adj = [[] for _ in range(size)]
    for _ in range(M):
        a, b = map(int, input().split())
        pa, pb = pos(a), pos(b)
        adj[pa ^ 1].append(pb)
        adj[pb ^ 1].append(pa)

    order = [0] * size
    low = [0] * size
    scc_id = [-1] * size
    stack = []
    on_stack = [False] * size
    cnt = 0
    scc_cnt = 0
    idx_arr = [0] * size  # 각 노드의 adj 탐색 위치

    for i in range(size):
        if order[i]:
            continue
        dfs_stack = [i]
        while dfs_stack:
            u = dfs_stack[-1]
            if order[u] == 0:
                cnt += 1
                order[u] = low[u] = cnt
                stack.append(u)
                on_stack[u] = True

            if idx_arr[u] < len(adj[u]):
                v = adj[u][idx_arr[u]]
                idx_arr[u] += 1
                if order[v] == 0:
                    dfs_stack.append(v)
                elif on_stack[v]:
                    low[u] = min(low[u], order[v])
            else:
                dfs_stack.pop()
                if low[u] == order[u]:
                    scc_cnt += 1
                    while True:
                        t = stack.pop()
                        on_stack[t] = False
                        scc_id[t] = scc_cnt
                        if t == u:
                            break
                if dfs_stack:
                    low[dfs_stack[-1]] = min(low[dfs_stack[-1]], low[u])

    for i in range(N):
        if scc_id[i * 2] == scc_id[i * 2 + 1]:
            print(0)
            return

    print(1)
    result = []
    for i in range(N):
        # 타잔: scc_cnt가 클수록 위상정렬 앞 → 작은 쪽이 true
        if scc_id[i * 2] > scc_id[i * 2 + 1]:
            result.append(0)
        else:
            result.append(1)
    print(*result)

if __name__ == "__main__":
    solution()