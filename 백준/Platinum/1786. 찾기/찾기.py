import sys

input = sys.stdin.readline

def solution():
    T = input().rstrip('\n')
    P = input().rstrip('\n')
    n, m = len(T), len(P)

    # 실패 함수 구하기
    fail = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = fail[j - 1]
        if P[i] == P[j]:
            j += 1
            fail[i] = j

    # 매칭
    result = []
    j = 0
    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = fail[j - 1]
        if T[i] == P[j]:
            j += 1
            if j == m:
                result.append(i - m + 2)  # 1-indexed
                j = fail[j - 1]

    print(len(result))
    print(*result)

if __name__ == "__main__":
    solution()