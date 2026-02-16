import sys
from collections import deque

input = sys.stdin.readline

DX = (1, -1, 0, 0)
DY = (0, 0, 1, -1)

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(N)]
    
    
    # 시작점 1, 1은 여기서는 0, 0
    x, y = 0, 0

    # board의 N-1, M-1 위치로 이동해야 함
    # 최소 칸수는 결국 BFS
    
    dist = [[0 for _ in range(M)] for _ in range(N)]
    
    # 시작점 x, y
    q = deque([(x, y)])
    dist[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx = cx + DX[k]
            ny = cy + DY[k]
            if 0<=nx<N and 0<=ny<M:                   
                # 방문 안했고, 숫자가 1이면 방문 후 거리 기록
                if not dist[nx][ny] and board[nx][ny]:
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))

    print(dist[N-1][M-1])



if __name__ == "__main__":
    solution()