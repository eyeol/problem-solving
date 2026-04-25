import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    best = float('inf')
    ans = (0, 0, 0)

    for i in range(N - 2):
        lo, hi = i + 1, N - 1
        while lo < hi:
            s = arr[i] + arr[lo] + arr[hi]
            if abs(s) < best:
                best = abs(s)
                ans = (arr[i], arr[lo], arr[hi])
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                print(*ans)
                return

    print(*ans)

if __name__ == "__main__":
    solution()