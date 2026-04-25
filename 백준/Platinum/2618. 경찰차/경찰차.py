import sys

sys.setrecursionlimit(3000)
input = sys.stdin.readline

def solution():
    N = int(input())
    W = int(input())
    events = [(0, 0)]  # dummy
    for _ in range(W):
        r, c = map(int, input().split())
        events.append((r, c))

    pos1 = (1, 1)
    pos2 = (N, N)

    def get_dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_pos(car, last_event):
        if last_event == 0:
            return pos1 if car == 1 else pos2
        return events[last_event]

    INF = float('inf')
    memo = {}

    def dp(i, j):
        # 다음 처리할 사건 = max(i, j) + 1
        nxt = max(i, j) + 1
        if nxt > W:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        p1 = get_pos(1, i)
        p2 = get_pos(2, j)

        # 경찰차1이 처리
        cost1 = get_dist(p1, events[nxt]) + dp(nxt, j)
        # 경찰차2가 처리
        cost2 = get_dist(p2, events[nxt]) + dp(i, nxt)

        memo[(i, j)] = min(cost1, cost2)
        return memo[(i, j)]

    print(dp(0, 0))

    # 역추적
    i, j = 0, 0
    for _ in range(W):
        nxt = max(i, j) + 1
        p1 = get_pos(1, i)
        p2 = get_pos(2, j)

        cost1 = get_dist(p1, events[nxt]) + dp(nxt, j)
        cost2 = get_dist(p2, events[nxt]) + dp(i, nxt)

        if cost1 <= cost2:
            print(1)
            i = nxt
        else:
            print(2)
            j = nxt

if __name__ == "__main__":
    solution()