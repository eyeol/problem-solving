import sys
from collections import deque

input = sys.stdin.readline

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

def solution():

    N, M = map(int, input().split())
    
    campus = [list(input().strip()) for _ in range(N)]

    sx, sy = 0, 0
    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                sx, sy = i, j

    visited = [[0]*M for _ in range(N)]

    q = deque([(sx, sy)])
    visited[sx][sy] = 1

    ans = 0
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + DX[k], cy + DY[k]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if campus[nx][ny] == "O":
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif campus[nx][ny] == "P":
                    ans += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    
    if ans == 0:
        print("TT")
    else:
        print(ans)


if __name__ == "__main__":
    solution()
