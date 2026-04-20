import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    queens = [0] * N
    count = 0

    cols = [0] * N
    diag1 = [0] * (2*N - 1)
    diag2 = [0] * (2*N - 1)

    def backtrack(row):
        nonlocal count
        if row == N:
            count += 1
            return
        
        for col in range(N):
            d1 = row - col + N - 1
            d2 = row + col
            # promising
            if cols[col] or diag1[d1] or diag2[d2]:
                continue

            cols[col] = diag1[d1] = diag2[d2] = True
            backtrack(row + 1)
            cols[col] = diag1[d1] = diag2[d2] = False

    backtrack(0)
    print(count)


if __name__ == "__main__":
    solution()