import sys

input = sys.stdin.readline

def solution():
    W, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # pair_sum[s] = (i, j) : arr[i]+arr[j]==s 인 쌍 중 j가 가장 작은 것
    pair_sum = {}

    # j를 작은 순서대로 처리
    for j in range(1, N):
        for i in range(j):
            s = arr[i] + arr[j]
            if s not in pair_sum:
                pair_sum[s] = j  # j가 가장 작은 쌍의 최대 인덱스

    # 큰 인덱스 쌍부터 확인
    for c in range(2, N):
        for d in range(c + 1, N):
            need = W - arr[c] - arr[d]
            if need in pair_sum and pair_sum[need] < c:
                print("YES")
                return

    print("NO")

if __name__ == "__main__":
    solution()