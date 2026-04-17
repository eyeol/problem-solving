import sys
from collections import deque

input = sys.stdin.readline

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

def solution():
    N = int(input())

    picture = [list(input().strip()) for _ in range(N)]


    visited = [[0]*N for _ in range(N)]

    def rg_disting_x(sx, sy):    
        q = deque([(sx, sy)])
        visited[sx][sy] = 1
        cur_color = picture[sx][sy]

        while q:
            cx, cy = q.popleft()
            for k in range(4):
                nx, ny = cx + DX[k], cy + DY[k]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if picture[nx][ny] == cur_color:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

    def rg_disting_o(sx, sy):    
        q = deque([(sx, sy)])
        visited[sx][sy] = 1
        cur_color = picture[sx][sy]

        while q:
            cx, cy = q.popleft()
            for k in range(4):
                nx, ny = cx + DX[k], cy + DY[k]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if cur_color == "B":
                        if picture[nx][ny] == cur_color:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                    else: # cur_color = R or G
                        if picture[nx][ny] != "B":
                            visited[nx][ny] = 1
                            q.append((nx, ny))
    
    x_ans = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                x_ans += 1
                rg_disting_x(x, y)
    
    visited = [[0]*N for _ in range(N)]

    o_ans = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                o_ans += 1
                rg_disting_o(x, y)

    print(x_ans, o_ans)

if __name__ == "__main__":
    solution()
