import heapq
import sys

input = sys.stdin.readline

def solution():
    T = int(input())

    def clean_top(heap, visited):
        while heap and not visited[heap[0][1]]:
            heapq.heappop(heap)


    for _ in range(T):
        K = int(input())
        max_heap = []
        min_heap = []

        visited = [False] * K
        idx = 0



        for _ in range(K):
            op = input().strip().split()
            if op[0] == "I":
                num = int(op[1])
                # lazy deletion을 위해 idx로 동기화해놓음
                heapq.heappush(min_heap, (num, idx))
                heapq.heappush(max_heap, (-num, idx))
                visited[idx] = True
                idx += 1
            
            else: # op[0] == "D"
                flag = int(op[1])
                # 최댓값 삭제
                if flag == 1:
                    clean_top(max_heap, visited)
                    if max_heap:
                        _, dead_idx = heapq.heappop(max_heap)
                        visited[dead_idx] = False
                # 최솟값 삭제
                else: # flag = -1
                    clean_top(min_heap, visited)
                    if min_heap:
                        _, dead_idx = heapq.heappop(min_heap)
                        visited[dead_idx] = False

        clean_top(max_heap, visited)
        clean_top(min_heap, visited)

        if not max_heap:
            print("EMPTY")
        else:
            print(max_heap[0][0] * -1, min_heap[0][0])



if __name__ == "__main__":
    solution()
