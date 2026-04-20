import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    result = []

    def backtrack():
        if len(result) == M:
            print(*result)
            return
        
        for i in range(1, N+1):
            # 방문
            result.append(i)
            
            # 재귀
            backtrack()

            # 재귀 후 상태 복구
            result.pop()
    
    backtrack()


if __name__ == "__main__":
    solution()