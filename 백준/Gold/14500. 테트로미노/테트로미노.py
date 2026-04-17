import sys

input = sys.stdin.readline

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

def solution():
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    
    # dfs로 깊이 4만큼 가기 - 백트래킹 DFS
    # T 모양은 따로 처리하기

    visited = [[False] * M for _ in range(N)]

    # DFS로 T 제외 모든 테트로미노 탐색
    def dfs(y, x, depth, total):
        # base
        if depth == 4:
            return total
        
        opt_val = total

        for k in range(4):
            ny, nx = y + DY[k], x + DX[k]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                opt_val = max(opt_val, dfs(ny, nx, depth+1, total + board[ny][nx]))
                visited[ny][nx] = False

        return opt_val
    
    def check_T(y, x):
        adjs = []
        for k in range(4):
            ny, nx = y + DY[k], x + DX[k]
            if 0 <= ny < N and 0 <= nx < M:
                adjs.append(board[ny][nx])
        
        if len(adjs) < 3:
            return 0
        
        adjs.sort(reverse=True)

        return board[y][x] + sum(adjs[:3])

    ans = 0
    for y in range(N):
        for x in range(M):
            # DFS
            visited[y][x] = True
            ans = max(ans, dfs(y, x, 1, board[y][x]))
            visited[y][x] = False

            ans = max(ans, check_T(y, x))
    
    print(ans)


if __name__ == "__main__":
    solution()
