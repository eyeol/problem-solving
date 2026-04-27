import sys
from itertools import combinations

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = []
    houses = []
    chickens = []

    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(N):
            if row[j] == 1:
                houses.append((i, j))
            elif row[j] == 2:
                chickens.append((i, j))

    ans = float('inf')
    for chosen in combinations(chickens, M):
        total = 0
        for hx, hy in houses:
            total += min(abs(hx - cx) + abs(hy - cy) for cx, cy in chosen)
        ans = min(ans, total)

    print(ans)

if __name__ == "__main__":
    solution()