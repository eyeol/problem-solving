import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    lo, hi = 0, N - 1
    best = float('inf')
    ans = (0, 0)

    while lo < hi:
        s = arr[lo] + arr[hi]
        if abs(s) < best:
            best = abs(s)
            ans = (arr[lo], arr[hi])
        if s < 0:
            lo += 1
        elif s > 0:
            hi -= 1
        else:
            break

    print(*ans)

if __name__ == "__main__":
    solution()