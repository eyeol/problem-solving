import sys

input = sys.stdin.readline
MOD = 1_000_003

def mat_mult(A, B, size):
    C = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if A[i][j] == 0:
                continue
            for k in range(size):
                C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % MOD
    return C

def mat_pow(M, p, size):
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    while p > 0:
        if p % 2 == 1:
            result = mat_mult(result, M, size)
        M = mat_mult(M, M, size)
        p //= 2
    return result

def solution():
    N, S, E, T = map(int, input().split())
    size = N * 5

    mat = [[0]*size for _ in range(size)]

    # 각 정점 i를 i*5, i*5+1, ..., i*5+4로 분할
    # i*5+k → i*5+k-1 체인 연결 (가중치 1씩 소모)
    for i in range(N):
        for k in range(1, 5):
            mat[i*5+k][i*5+k-1] = 1

    for i in range(N):
        line = input().strip()
        for j in range(N):
            w = int(line[j])
            if w > 0:
                # i → j, 가중치 w
                # i*5+0 에서 j*5+(w-1) 로 연결
                mat[i*5][j*5+w-1] = (mat[i*5][j*5+w-1] + 1) % MOD

    result = mat_pow(mat, T, size)
    print(result[(S-1)*5][(E-1)*5])

if __name__ == "__main__":
    solution()