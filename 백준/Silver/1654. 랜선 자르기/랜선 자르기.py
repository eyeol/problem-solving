import sys
from collections import deque

input = sys.stdin.readline


def solution():

    K, N = map(int, input().split())

    assets = []
    for _ in range(K):
        assets.append(int(input()))
    
    # 이분탐색으로 범위 찾기

    ## 판별 함수
    def determine(x):
        result = 0
        for length in assets:
            result += (length // x)
        if result >= N:
            return True
        else: return False

    ## 탐색

    ### 탐색 범위 초기설정
    lo = 1
    hi = max(assets)

    while lo <= hi:
        mid = (lo + hi) // 2
        if determine(mid):
            # mid로 되면 범위 높이기
            lo = mid + 1
        else: # mid로 안되면 범위 낮추기
            hi = mid - 1
    
    print(hi)


if __name__ == "__main__":
    solution()
