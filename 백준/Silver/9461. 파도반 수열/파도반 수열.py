import sys

input = sys.stdin.readline

def solution():

    # 반복되는 형태로 재귀식을 만들 수 있음
    # 5각형이 생긴 이후부터 반복됨

    # 1, 2, 3, 4, 5 가 다음엔
    # 2, 3, 4, 5, 1+5 로 구성되면 됨

    base = [1, 1, 1, 2, 2]

    T = int(input())

    for _ in range(T):
        N = int(input())
        if N <= 5:
            print(base[N-1])
        else:
            K = N - 5
            pado = [1, 1, 1, 2, 2]
            for _ in range(K):
                pado = [pado[1], pado[2], pado[3], pado[4], pado[4] + pado[0]]
            print(pado[-1])

if __name__ == "__main__":
    solution()
