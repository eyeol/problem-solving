import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip())))

    # visited[x][y][broke] : 벽을 broke번 부수고 (x,y)에 도착했는지
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True

    # (x, y, 벽부순횟수, 거리)
    q = deque([(0, 0, 0, 1)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, broke, dist = q.popleft()

        if x == N - 1 and y == M - 1:
            print(dist)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 칸이면 그냥 이동
                if board[nx][ny] == 0 and not visited[nx][ny][broke]:
                    visited[nx][ny][broke] = True
                    q.append((nx, ny, broke, dist + 1))
                # 벽인데 아직 안 부셨으면 부수고 이동
                elif board[nx][ny] == 1 and broke == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, 1, dist + 1))

    print(-1)

if __name__ == "__main__":
    solution()