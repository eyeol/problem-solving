import sys
import copy

input = sys.stdin.readline

def move(board, direction, N):
    # 방향에 따라 한 줄씩 처리
    if direction == 0:  # 위
        for j in range(N):
            merged = []
            for i in range(N):
                if board[i][j] != 0:
                    merged.append(board[i][j])
            merged = merge(merged)
            for i in range(N):
                board[i][j] = merged[i] if i < len(merged) else 0
    elif direction == 1:  # 아래
        for j in range(N):
            merged = []
            for i in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    merged.append(board[i][j])
            merged = merge(merged)
            for i in range(N):
                board[N - 1 - i][j] = merged[i] if i < len(merged) else 0
    elif direction == 2:  # 왼쪽
        for i in range(N):
            merged = []
            for j in range(N):
                if board[i][j] != 0:
                    merged.append(board[i][j])
            merged = merge(merged)
            for j in range(N):
                board[i][j] = merged[j] if j < len(merged) else 0
    else:  # 오른쪽
        for i in range(N):
            merged = []
            for j in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    merged.append(board[i][j])
            merged = merge(merged)
            for j in range(N):
                board[i][N - 1 - j] = merged[j] if j < len(merged) else 0
    return board

def merge(line):
    result = []
    i = 0
    while i < len(line):
        if i + 1 < len(line) and line[i] == line[i + 1]:
            result.append(line[i] * 2)
            i += 2
        else:
            result.append(line[i])
            i += 1
    return result

def solution():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    ans = 0

    def dfs(b, depth):
        nonlocal ans
        if depth == 5:
            ans = max(ans, max(max(row) for row in b))
            return
        for d in range(4):
            nb = copy.deepcopy(b)
            move(nb, d, N)
            dfs(nb, depth + 1)

    dfs(board, 0)
    print(ans)

if __name__ == "__main__":
    solution()