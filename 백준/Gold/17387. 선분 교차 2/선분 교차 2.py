import sys

input = sys.stdin.readline

def ccw(p1, p2, p3):
    val = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if val > 0:
        return 1
    elif val < 0:
        return -1
    return 0

def on_segment(p, q, r):
    # r이 p-q 선분 위에 있는지
    if min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and \
       min(p[1], q[1]) <= r[1] <= max(p[1], q[1]):
        return True
    return False

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    A, B = (x1, y1), (x2, y2)
    C, D = (x3, y3), (x4, y4)

    d1 = ccw(A, B, C)
    d2 = ccw(A, B, D)
    d3 = ccw(C, D, A)
    d4 = ccw(C, D, B)

    if d1 * d2 < 0 and d3 * d4 < 0:
        print(1)
        return

    # 일직선 위인 경우
    if d1 == 0 and on_segment(A, B, C):
        print(1)
        return
    if d2 == 0 and on_segment(A, B, D):
        print(1)
        return
    if d3 == 0 and on_segment(C, D, A):
        print(1)
        return
    if d4 == 0 and on_segment(C, D, B):
        print(1)
        return

    print(0)

if __name__ == "__main__":
    solution()