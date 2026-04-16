import sys
from collections import deque

input = sys.stdin.readline

DX = [1, -1, 0, 0, 0, 0]
DY = [0, 0, 1, -1, 0, 0]
DZ = [0, 0, 0, 0, 1, -1]

def solution():
    M, N, H = map(int, input().split())
    boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    q = deque()
    zero_cnt = 0

    for z in range(H):
        for y in range(N):
            for x in range(M):
                v = boxes[z][y][x]
                if v == 1:
                    q.append((x, y, z))
                elif v == 0:
                    zero_cnt += 1

    if zero_cnt == 0:
        print(0)
        return

    max_day = 1

    while q:
        cx, cy, cz = q.popleft()
        cur = boxes[cz][cy][cx]

        for k in range(6):
            nx = cx + DX[k]
            ny = cy + DY[k]
            nz = cz + DZ[k]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = cur + 1
                max_day = cur + 1
                zero_cnt -= 1
                q.append((nx, ny, nz))

    if zero_cnt > 0:
        print(-1)
    else:
        print(max_day - 1)

if __name__ == "__main__":
    solution()