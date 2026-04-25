import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    area = 0
    for i in range(N):
        j = (i + 1) % N
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]

    print(round(abs(area) / 2, 1))

if __name__ == "__main__":
    solution()