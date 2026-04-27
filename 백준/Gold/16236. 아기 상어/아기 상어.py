import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N = int(input())
    board = []
    sx, sy = 0, 0
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(N):
            if row[j] == 9:
                sx, sy = i, j

    board[sx][sy] = 0
    size = 2
    eaten = 0
    total_time = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        # BFS로 먹을 수 있는 가장 가까운 물고기 찾기
        visited = [[False] * N for _ in range(N)]
        visited[sx][sy] = True
        q = deque([(sx, sy, 0)])
        candidates = []
        min_dist = float('inf')

        while q:
            x, y, d = q.popleft()
            if d > min_dist:
                break
            if 0 < board[x][y] < size:
                candidates.append((d, x, y))
                min_dist = d
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))

        if not candidates:
            break

        candidates.sort()
        d, fx, fy = candidates[0]
        total_time += d
        board[fx][fy] = 0
        sx, sy = fx, fy
        eaten += 1
        if eaten == size:
            size += 1
            eaten = 0

    print(total_time)

if __name__ == "__main__":
    solution()