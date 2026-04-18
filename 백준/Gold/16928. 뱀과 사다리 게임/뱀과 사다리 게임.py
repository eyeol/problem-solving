import sys
from collections import deque

input = sys.stdin.readline

def solution():

    N, M = map(int, input().split())
    ladders = list(range(101)) # 0 ~ 100
    snakes = list(range(101))  # 0 ~ 100
    for _ in range(N):
        x, y = map(int, input().split())
        ladders[x] = y
    for _ in range(M):
        u, v = map(int, input().split())
        snakes[u] = v

    visited = [0]*101
    visited[0] = 1
    visited[1] = 1

    ans = 0
    # (현재 위치 / 주사위)
    q = deque([(1, 0)])
    while q:
        cur, num = q.popleft()
        if cur == 100:
            ans = num
            break
        for k in range(1, 7): # 1 ~ 6
            if cur + k <= 100 and not visited[cur+k]:
                ## 방문 안했으면 도착
                nxt = cur + k
                visited[cur+k] = 1
                ## 사다리나 뱀 확인
                ## 사다리나 뱀 타게 되면 이동 및 방문
                if ladders[cur+k] != cur+k:
                    if visited[ladders[cur+k]]:
                        continue
                    nxt = ladders[cur+k]
                    visited[nxt] = 1
                elif snakes[cur+k] != cur+k:
                    if visited[snakes[cur+k]]:
                        continue
                    nxt = snakes[cur+k]
                    visited[nxt] = 1
                q.append((nxt, num+1))

    print(ans)


if __name__ == "__main__":
    solution()
