import sys

input = sys.stdin.readline


def solution():

    N = int(input())

    A = []
    for _ in range(N):
        A.append(int(input()))

    def insertion_sort(A: list):
        # 삽입할 값의 인덱스 i
        # 이미 한 장 삽입되었다고 보고 1부터 시작
        for i in range(1, len(A)): # 1 ~ N-1
            key = A[i]
            while i > 0 and key < A[i-1]:
                    A[i] = A[i-1]
                    i -= 1
            A[i] = key
    
    insertion_sort(A)
    for num in A:
         print(num)

if __name__ == "__main__":
    solution()