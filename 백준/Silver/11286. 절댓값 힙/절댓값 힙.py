import heapq
import sys

input = sys.stdin.readline

def solution():
    N = int(input())

    h = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            if not h:
                print(0)
            else:
                result = heapq.heappop(h)
                print(result[1])
        else: 
            heapq.heappush(h, (abs(num), num))



if __name__ == "__main__":
    solution()
