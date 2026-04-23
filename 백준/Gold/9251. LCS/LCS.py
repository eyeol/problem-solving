import sys

input = sys.stdin.readline


def solution():
    A = input().strip()
    B = input().strip()
    
    N, M = len(A), len(B)

    lcs = [[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if A[i-1] == B[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    print(lcs[N][M])


if __name__ == "__main__":
    solution()