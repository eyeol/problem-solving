import sys

def solution():
    board = []
    blanks = []
    for i in range(9):
        row = list(map(int, list(input())))
        board.append(row)
        for j in range(9):
            if row[j] == 0:
                blanks.append((i, j))

    row_used = [set() for _ in range(9)]
    col_used = [set() for _ in range(9)]
    box_used = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                v = board[i][j]
                row_used[i].add(v)
                col_used[j].add(v)
                box_used[(i // 3) * 3 + j // 3].add(v)

    def solve(idx):
        if idx == len(blanks):
            return True

        r, c = blanks[idx]
        b = (r // 3) * 3 + c // 3

        for num in range(1, 10):
            if num in row_used[r] or num in col_used[c] or num in box_used[b]:
                continue
            board[r][c] = num
            row_used[r].add(num)
            col_used[c].add(num)
            box_used[b].add(num)

            if solve(idx + 1):
                return True

            board[r][c] = 0
            row_used[r].discard(num)
            col_used[c].discard(num)
            box_used[b].discard(num)

        return False

    solve(0)
    for row in board:
        print(''.join(map(str, row)))

if __name__ == "__main__":
    solution()