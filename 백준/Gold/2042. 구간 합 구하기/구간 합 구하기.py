import sys

input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    arr = [0] * (N + 1)
    tree = [0] * (4 * N)

    for i in range(1, N + 1):
        arr[i] = int(input())

    def build(node, s, e):
        if s == e:
            tree[node] = arr[s]
            return
        mid = (s + e) // 2
        build(node * 2, s, mid)
        build(node * 2 + 1, mid + 1, e)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

    def update(node, s, e, idx, val):
        if idx < s or idx > e:
            return
        if s == e:
            tree[node] = val
            return
        mid = (s + e) // 2
        update(node * 2, s, mid, idx, val)
        update(node * 2 + 1, mid + 1, e, idx, val)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

    def query(node, s, e, l, r):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return tree[node]
        mid = (s + e) // 2
        return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r)

    build(1, 1, N)

    out = []
    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 1, N, b, c)
        else:
            out.append(str(query(1, 1, N, b, c)))

    print('\n'.join(out))

if __name__ == "__main__":
    solution()