import sys

input = sys.stdin.readline

def solution():
    R, C = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(input().strip())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [False] * 26
    visited[ord(board[0][0]) - ord('A')] = True
    ans = 1

    def dfs(x, y, depth):
        nonlocal ans
        ans = max(ans, depth)
        if ans == 26:
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                idx = ord(board[nx][ny]) - ord('A')
                if not visited[idx]:
                    visited[idx] = True
                    dfs(nx, ny, depth + 1)
                    visited[idx] = False

    dfs(0, 0, 1)
    print(ans)

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    solution()