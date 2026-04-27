import sys
from collections import deque

input = sys.stdin.readline
MAX = 100001

def solution():
    N, K = map(int, input().split())

    if N == K:
        print(0)
        print(1)
        return

    dist = [-1] * MAX
    count = [0] * MAX
    dist[N] = 0
    count[N] = 1
    q = deque([N])

    while q:
        x = q.popleft()

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX:
                if dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    count[nx] = count[x]
                    q.append(nx)
                elif dist[nx] == dist[x] + 1:
                    count[nx] += count[x]

    print(dist[K])
    print(count[K])

if __name__ == "__main__":
    solution()