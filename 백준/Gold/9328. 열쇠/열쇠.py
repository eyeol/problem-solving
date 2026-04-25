import sys
from collections import deque

input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        board = []
        for _ in range(H):
            board.append(list(input().strip()))
        keys_input = input().strip()

        keys = set()
        if keys_input != '0':
            keys = set(keys_input)

        # 가장자리를 진입점으로 하기 위해 외곽에 빈칸 테두리 추가
        new_board = [['.' for _ in range(W + 2)]]
        for row in board:
            new_board.append(['.'] + row + ['.'])
        new_board.append(['.' for _ in range(W + 2)])
        board = new_board
        H += 2
        W += 2

        visited = [[False] * W for _ in range(H)]
        waiting = {}  # 문 앞에서 대기 중인 좌표들
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            waiting[c] = []

        q = deque()
        visited[0][0] = True
        q.append((0, 0))
        ans = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                    cell = board[nx][ny]
                    if cell == '*':
                        continue
                    visited[nx][ny] = True

                    if cell == '$':
                        ans += 1
                        q.append((nx, ny))
                    elif cell == '.':
                        q.append((nx, ny))
                    elif 'a' <= cell <= 'z':
                        keys.add(cell)
                        q.append((nx, ny))
                        # 이 열쇠로 열 수 있는 대기 중인 문 처리
                        door = cell.upper()
                        for wx, wy in waiting[door]:
                            q.append((wx, wy))
                        waiting[door] = []
                    elif 'A' <= cell <= 'Z':
                        if cell.lower() in keys:
                            q.append((nx, ny))
                        else:
                            waiting[cell].append((nx, ny))

        print(ans)

if __name__ == "__main__":
    solution()