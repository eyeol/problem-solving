import sys
import heapq

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    gems = []
    for _ in range(N):
        m, v = map(int, input().split())
        gems.append((m, v))

    bags = []
    for _ in range(K):
        bags.append(int(input()))

    gems.sort()  # 무게 순 정렬
    bags.sort()  # 용량 순 정렬

    result = 0
    heap = []  # 최대 힙 (가격을 음수로)
    j = 0

    for bag in bags:
        # 이 가방에 들어갈 수 있는 보석 전부 힙에 넣기
        while j < N and gems[j][0] <= bag:
            heapq.heappush(heap, -gems[j][1])
            j += 1

        # 힙에서 가장 비싼 보석 꺼내기
        if heap:
            result -= heapq.heappop(heap)

    print(result)

if __name__ == "__main__":
    solution()