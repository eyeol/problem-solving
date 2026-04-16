import sys
from collections import deque

input = sys.stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        p = input().strip()
        N = int(input())
        line = input().strip()
        inner = line[1:-1] # 괄호 제거
        
        if inner:
            nums = deque(map(int, inner.split(",")))
        else:
            nums = deque()

        direction = 1
        error_occur = 0
        for ch in p:
            if ch == "R":
                direction *= -1
            elif ch == "D":
                if not nums:
                    error_occur = 1
                    break
                else:
                    if direction == 1:
                        nums.popleft()
                    else:
                        nums.pop()
        
        if error_occur:
            print("error")
        else:
            if direction == 1:
                print("[" + ",".join(map(str, nums)) + "]")
            else:
                nums.reverse()  # 마지막에 한 번만 뒤집기
                print("[" + ",".join(map(str, nums)) + "]")


if __name__ == "__main__":
    solution()
