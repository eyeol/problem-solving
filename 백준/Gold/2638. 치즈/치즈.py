import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs_air():
        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return visited

    time = 0
    while True:
        air = bfs_air()
        melt = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    cnt = 0
                    for d in range(4):
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < N and 0 <= nj < M and air[ni][nj]:
                            cnt += 1
                    if cnt >= 2:
                        melt.append((i, j))

        if not melt:
            break

        for x, y in melt:
            board[x][y] = 0
        time += 1

    print(time)

if __name__ == "__main__":
    solution()