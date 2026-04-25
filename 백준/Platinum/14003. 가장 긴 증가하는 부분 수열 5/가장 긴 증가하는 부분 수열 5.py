import sys
from bisect import bisect_left

input = sys.stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    tails = []
    pos = []  # pos[i] = arr[i]가 tails의 몇 번째에 들어갔는지

    for x in arr:
        p = bisect_left(tails, x)
        if p == len(tails):
            tails.append(x)
        else:
            tails[p] = x
        pos.append(p)

    # 역추적
    lis_len = len(tails)
    print(lis_len)

    result = []
    target = lis_len - 1
    for i in range(N - 1, -1, -1):
        if pos[i] == target:
            result.append(arr[i])
            target -= 1
            if target < 0:
                break

    print(*reversed(result))

if __name__ == "__main__":
    solution()