import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():

    N = int(input())
    fruits = list(map(int, input().split()))
    
    f_count = defaultdict(int)
    kinds = 0
    L = 0
    ans = 0

    # 슬라이딩 윈도우 사용
    for R in range(N):
        # R 이동 및 새 과일 추가
        if f_count[fruits[R]] == 0:
            kinds += 1
        f_count[fruits[R]] += 1

        # 조건 위반 시 L 이동
        while kinds > 2:
            f_count[fruits[L]] -= 1
            if f_count[fruits[L]] == 0:
                kinds -= 1
            L += 1

        ans = max(ans, R - L + 1)
    
    print(ans)


if __name__ == "__main__":
    solution()
