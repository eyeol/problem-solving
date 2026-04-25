import sys
from functools import cmp_to_key

input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

def dist2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def solution():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    # 기준점: y 최소, 같으면 x 최소
    points.sort(key=lambda p: (p[1], p[0]))
    pivot = points[0]

    def compare(a, b):
        c = ccw(pivot, a, b)
        if c > 0:
            return -1
        elif c < 0:
            return 1
        else:
            # 일직선이면 가까운 점 먼저
            da = dist2(pivot, a)
            db = dist2(pivot, b)
            if da < db:
                return -1
            elif da > db:
                return 1
            return 0

    rest = sorted(points[1:], key=cmp_to_key(compare))

    stack = [pivot, rest[0]]
    for i in range(1, len(rest)):
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], rest[i]) <= 0:
            stack.pop()
        stack.append(rest[i])

    print(len(stack))

if __name__ == "__main__":
    solution()