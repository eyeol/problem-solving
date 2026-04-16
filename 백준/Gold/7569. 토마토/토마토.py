import sys
from collections import deque

input = sys.stdin.readline

DX = [1, 0, 0, -1, 0, 0]
DY = [0, 1, 0, 0, -1, 0]
DZ = [0, 0, 1, 0, 0, -1]

def solution():

    M, N, H = map(int, input().split())

    boxes = []

    # box 개수는 H만큼
    for _ in range(H):
        # M x N 크기 박스
        box = [list(map(int, input().split())) for _ in range(N)]
        boxes.append(box)

    # bfs 출발에 쓰일 토마토들
    sources = []
    all_riped = 1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                all_riped *= boxes[z][y][x]
                if boxes[z][y][x] == 1:
                    sources.append((x, y, z))
    
    # 모든 토마토가 있었다면
    if all_riped != 0:
        print("0")
        return # early return


    q = deque(sources)
    # bfs
    while q:
        cx, cy, cz = q.popleft()
        cur = boxes[cz][cy][cx]
        for k in range(6):
            nx = cx + DX[k]
            ny = cy + DY[k]
            nz = cz + DZ[k]
            # 범위 체크
            if 0<=nx<M and 0<=ny<N and 0 <=nz<H:
                nxt = boxes[nz][ny][nx]
                # nxt tomato가 0이면
                if nxt == 0:
                    boxes[nz][ny][nx] = cur + 1
                    q.append((nx, ny, nz))
    
    max_val = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 0:
                    print(-1)
                    return
                if boxes[z][y][x] > max_val:
                    max_val = boxes[z][y][x]

    print(max_val - 1)

if __name__ == "__main__":
    solution()
