import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    result = []

    visited = [0] * N
    
    def backtrack():
        if len(result) == M:
            print(*result)
            return
        
        used = set()
        for i, num in enumerate(nums):
            if visited[i] == 1:
                continue
            
            if num in used:
                continue

            if result and num < result[-1]:
                continue
            
            used.add(num)

            # 방문 처리
            visited[i] = 1
            result.append(num)
            
            # 재귀
            backtrack()

            # 재귀 후 상태 복구
            visited[i] = 0
            result.pop()
    
    backtrack()



if __name__ == "__main__":
    solution()