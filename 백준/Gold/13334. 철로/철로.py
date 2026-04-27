import sys
import heapq

input = sys.stdin.readline

def solution():
    N = int(input())
    pairs = []
    for _ in range(N):
        h, o = map(int, input().split())
        l, r = min(h, o), max(h, o)
        pairs.append((l, r))
    d = int(input())

    pairs = [(l, r) for l, r in pairs if r - l <= d]
    pairs.sort(key=lambda x: x[1])

    heap = []
    ans = 0

    for l, r in pairs:
        heapq.heappush(heap, l)
        while heap and heap[0] < r - d:
            heapq.heappop(heap)
        ans = max(ans, len(heap))

    print(ans)

if __name__ == "__main__":
    solution()