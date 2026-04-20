import itertools
import sys
from collections import deque

input = sys.stdin.readline

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

def solution():

    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    def bfs(virus, maps):
        # 방문 기록 초기화
        visited = [[0]* M for _ in range(N)]

        for v in virus:
            # virus 하나는 (x, y) tuple
            if not visited[v[0]][v[1]]:
                q = deque([v])
                visited[v[0]][v[1]]
                # 퍼지는건 바이러스
                while q:
                    cx, cy = q.popleft()
                    for k in range(4):
                        nx, ny = cx + DX[k], cy + DY[k]
                        # 범위 안에 있고 벽이 아니어야
                        if 0<=nx<N and 0<=ny<M and maps[nx][ny] != 1:
                            # 빈칸이든 바이러스든 방문 안했다면 추가
                            if not visited[nx][ny]:
                                visited[nx][ny] = 1
                                maps[nx][ny] = 2
                                q.append((nx, ny))

        # 최종 반환할 결과물은 안전 지역
        safe = 0
        for x in range(N):
            for y in range(M):
                if maps[x][y] == 0:
                    safe += 1
        return safe

    empty_space = []
    virus = []

    for x in range(N):
        for y in range(M):
            if maps[x][y] == 0:
                empty_space.append((x, y))
            elif maps[x][y] == 2:
                virus.append((x, y))
    
    # 빈 칸 중에서 벽 세울 세 칸을 골라야 함
    candidate = list(itertools.combinations(empty_space, 3))


    ans = 0
    for case in candidate:
        # freash map 매번 복사해옴
        f_map = [row[:] for row in maps]
        for wx, wy in case:
            f_map[wx][wy] = 1

        result = bfs(virus, f_map)
        ans = max(ans, result)

    print(ans)

if __name__ == "__main__":
    solution()