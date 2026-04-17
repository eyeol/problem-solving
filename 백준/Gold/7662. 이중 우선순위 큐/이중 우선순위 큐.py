import sys
import heapq

input = sys.stdin.readline


def clean_top(heap, visited):
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)


def solution():
    T = int(input())

    for _ in range(T):
        K = int(input())

        min_heap = []
        max_heap = []
        visited = [False] * K

        for idx in range(K):
            op, num = input().split()
            num = int(num)

            if op == "I":
                heapq.heappush(min_heap, (num, idx))
                heapq.heappush(max_heap, (-num, idx))
                visited[idx] = True

            else:  # op == "D"
                if num == 1:
                    clean_top(max_heap, visited)
                    if max_heap:
                        _, dead_idx = heapq.heappop(max_heap)
                        visited[dead_idx] = False
                else:  # num == -1
                    clean_top(min_heap, visited)
                    if min_heap:
                        _, dead_idx = heapq.heappop(min_heap)
                        visited[dead_idx] = False

        clean_top(min_heap, visited)
        clean_top(max_heap, visited)

        if not min_heap or not max_heap:
            print("EMPTY")
        else:
            print(-max_heap[0][0], min_heap[0][0])


if __name__ == "__main__":
    solution()