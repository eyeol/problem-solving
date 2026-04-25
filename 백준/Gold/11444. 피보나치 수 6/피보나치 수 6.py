import sys

input = sys.stdin.readline
MOD = 1_000_000_007

def mat_mult(A, B):
    # 2x2 행렬 곱셈
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(M, n):
    # 단위 행렬로 시작
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = mat_mult(result, M)
        M = mat_mult(M, M)
        n //= 2
    return result

def solution():
    N = int(input())
    if N <= 1:
        print(N)
        return
    base = [[1, 1], [1, 0]]
    ans = mat_pow(base, N)
    print(ans[0][1])  # F(N)

if __name__ == "__main__":
    solution()