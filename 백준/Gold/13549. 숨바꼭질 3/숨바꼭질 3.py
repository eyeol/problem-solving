import sys
from collections import deque

input = sys.stdin.readline
MAX = 100_001

def solution():
    N, K = map(int, input().split())

    dist = [-1] * MAX
    dist[N] = 0
    q = deque([N])

    while q:
        x = q.popleft()

        if x == K:
            print(dist[x])
            return

        # 순간이동 (비용 0) → 덱 앞에
        nx = x * 2
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[x]
            q.appendleft(nx)

        # 걷기 (비용 1) → 덱 뒤에
        for nx in (x - 1, x + 1):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

    print(-1)

if __name__ == "__main__":
    solution()