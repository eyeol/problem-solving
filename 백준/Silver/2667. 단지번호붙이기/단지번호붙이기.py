import sys
from collections import deque

input = sys.stdin.readline

DX = (1, -1, 0, 0)
DY = (0, 0, 1, -1)

def solution():
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]

    # 거리는  필요 없고 visited만 기록하면 될듯
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 단지수 ; bfs tree 개수
    # 각 단지에 속하는 집의 수; visited가 갱신될 때마다 1씩 더하면 됨

    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = 1
        house_num = 1

        while q:
            cx, cy = q.popleft()

            for k in range(4):
                nx = cx + DX[k]
                ny = cy + DY[k]
                # 범위 검사
                if 0<=nx<N and 0<=ny<N:
                    # 집이 있고 / 아직 방문 안했다면 que에 넣기
                    if board[nx][ny]!=0 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        house_num += 1

        return house_num

    # 전체에 대해 bfs 돌리기
    tree_num = 0
    house_num = []

    for x in range(N):
        for y in range(N):
            # 집이 있고 / 방문한 적 없으면 거기서 bfs 시작
            if board[x][y] != 0 and not visited[x][y]:
                tree_num += 1
                result = bfs(x, y)
                house_num.append(result)

    print(tree_num)
    house_num.sort()
    for num in house_num:
        print(num)

if __name__ == "__main__":
    solution()