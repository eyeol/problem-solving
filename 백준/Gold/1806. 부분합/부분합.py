import sys

input = sys.stdin.readline

def solution():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    start = 0
    total = 0
    ans = N + 1

    for end in range(N):
        total += arr[end]

        while total >= S:
            ans = min(ans, end - start + 1)
            total -= arr[start]
            start += 1

    print(0 if ans == N + 1 else ans)

if __name__ == "__main__":
    solution()