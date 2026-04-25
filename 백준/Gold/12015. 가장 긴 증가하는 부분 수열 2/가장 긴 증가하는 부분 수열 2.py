import sys
from bisect import bisect_left

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    tails = []

    for x in arr:
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    print(len(tails))

if __name__ == "__main__":
    solution()