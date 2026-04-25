import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)

    for _ in range(M):
        line = list(map(int, input().split()))
        cnt = line[0]
        singers = line[1:]
        for i in range(cnt - 1):
            adj[singers[i]].append(singers[i + 1])
            in_degree[singers[i + 1]] += 1

    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)
        for nxt in adj[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)

    if len(ans) != N:
        print(0)
    else:
        print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    solution()