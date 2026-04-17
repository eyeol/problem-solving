import sys
from collections import deque

input = sys.stdin.readline

def solution():
    T = int(input())

    def digitalize(num: int):
        digits = str(num)
        N = 4 - len(digits)
        digits = "0"*N + digits
        return digits


    def ins_D(digits: str):
        num = int(digits)
        result = digitalize((2*num) % 10000)
        return result
    
    def ins_S(digits: str):
        num = int(digits)
        if num == 0:
            return "9999"
        result = digitalize(num - 1)
        return result

    def ins_L(digits: str):
        result = digits[1] + digits[2] + digits[3] + digits[0]
        return result
    
    def ins_R(digits: str):
        result = digits[3] + digits[0] + digits[1] + digits[2]
        return result


    for _ in range(T):
        A, B = map(int, input().split())
        A = digitalize(A)
        B = digitalize(B)

        visited = [False] * 10000
        parent = [None] * 10000
        
        # (str, # of ops)
        q = deque([A])
        visited[int(A)] = True

        while q:
            cur = q.popleft()
            if cur == B:
                # 역추적
                ops = []
                while parent[int(cur)] is not None:
                    prev, op = parent[int(cur)]
                    ops.append(op)
                    cur = prev
                print("".join(reversed(ops)))
                break
            
            for op, nxt in [("D", ins_D(cur)), ("S", ins_S(cur)),
                            ("L", ins_L(cur)), ("R", ins_R(cur))]:
                if not visited[int(nxt)]:
                    visited[int(nxt)] = True
                    parent[int(nxt)] = (cur, op)
                    q.append(nxt)


if __name__ == "__main__":
    solution()
