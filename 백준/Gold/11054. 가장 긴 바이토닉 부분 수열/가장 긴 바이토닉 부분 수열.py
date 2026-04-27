import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    # 왼쪽에서 오른쪽 LIS
    inc = [1] * N
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + 1)

    # 오른쪽에서 왼쪽 LIS
    dec = [1] * N
    for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1):
            if arr[j] < arr[i]:
                dec[i] = max(dec[i], dec[j] + 1)

    ans = 0
    for i in range(N):
        ans = max(ans, inc[i] + dec[i] - 1)

    print(ans)

if __name__ == "__main__":
    solution()