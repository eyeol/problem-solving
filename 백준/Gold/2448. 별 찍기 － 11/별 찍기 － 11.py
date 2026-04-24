import sys
from collections import deque

input = sys.stdin.readline

def solution():
    def draw(arr, r, c):
        arr[r][c] = "*"
        arr[r+1][c-1] = arr[r+1][c+1] = "*"
        for i in range(-2, 3):
            arr[r+2][c+i] = "*"

    def triangle(arr, size, r, c):
        if size == 3:
            draw(arr, r, c)
            return
        half = size // 2
        triangle(arr, half, r, c)
        triangle(arr, half, r+half, c-half)
        triangle(arr, half, r+half, c+half)
    
    N = int(input())
    arr = [[' '] * (2*N-1) for _ in range(N)]
    triangle(arr, N, 0, N-1)
    print('\n'.join(''.join(row) for row in arr))


if __name__ == "__main__":
    solution()