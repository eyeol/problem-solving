import sys

input = sys.stdin.readline
INF = float('inf')

def solution():
    N, M = map(int, input().split())
    arr = [0] * (N + 1)
    min_tree = [INF] * (4 * N)
    max_tree = [0] * (4 * N)

    for i in range(1, N + 1):
        arr[i] = int(input())

    def build(node, s, e):
        if s == e:
            min_tree[node] = max_tree[node] = arr[s]
            return
        mid = (s + e) // 2
        build(node * 2, s, mid)
        build(node * 2 + 1, mid + 1, e)
        min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
        max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])

    def query_min(node, s, e, l, r):
        if r < s or e < l:
            return INF
        if l <= s and e <= r:
            return min_tree[node]
        mid = (s + e) // 2
        return min(query_min(node * 2, s, mid, l, r),
                   query_min(node * 2 + 1, mid + 1, e, l, r))

    def query_max(node, s, e, l, r):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return max_tree[node]
        mid = (s + e) // 2
        return max(query_max(node * 2, s, mid, l, r),
                   query_max(node * 2 + 1, mid + 1, e, l, r))

    build(1, 1, N)

    out = []
    for _ in range(M):
        a, b = map(int, input().split())
        out.append(f"{query_min(1, 1, N, a, b)} {query_max(1, 1, N, a, b)}")

    print('\n'.join(out))

if __name__ == "__main__":
    solution()