import sys
from collections import Counter

input = sys.stdin.readline

def solution():
    N = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    AB = Counter(a + b for a in A for b in B)

    ans = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in AB:
                ans += AB[target]

    print(ans)

if __name__ == "__main__":
    solution()