import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        row = list(input().strip())
        board.append(row)
        for j in range(M):
            if row[j] == 'R':
                rx, ry = i, j
            elif row[j] == 'B':
                bx, by = i, j

    def move(x, y, dx, dy):
        cnt = 0
        while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
            x += dx
            y += dy
            cnt += 1
        return x, y, cnt

    visited = set()
    visited.add((rx, ry, bx, by))
    q = deque([(rx, ry, bx, by, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth >= 10:
            break

        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                print(depth + 1)
                return

            # 겹치면 더 많이 이동한 쪽을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    print(-1)

if __name__ == "__main__":
    solution()