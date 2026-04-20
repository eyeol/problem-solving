import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    result = []
    visited = [0] * (N+1)

    def backtrack():
        if len(result) == M:
            print(*result)
            return

        for i in range(1, N+1):
            if visited[i]:
                continue

            # 방문
            visited[i] = 1
            result.append(i)
            
            # 재귀
            backtrack()

            # 재귀 후 상태 복구
            result.pop()
            visited[i] = 0
    
    backtrack()


if __name__ == "__main__":
    solution()