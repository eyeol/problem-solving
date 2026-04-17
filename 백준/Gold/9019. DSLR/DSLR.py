import sys
from collections import deque

input = sys.stdin.readline

def solution():
    T = int(input())

    def ins_D(n):
        return (n * 2) % 10000
    
    def ins_S(n):
        return 9999 if n == 0 else n - 1

    def ins_L(n):
        # abcd → bcda
        return (n % 1000) * 10 + n // 1000
    
    def ins_R(n):
        # abcd → dabc
        return (n % 10) * 1000 + n // 10


    for _ in range(T):
        A, B = map(int, input().split())

        visited = [False] * 10000
        parent = [None] * 10000
        
        q = deque([A])
        visited[A] = True

        while q:
            cur = q.popleft()
            if cur == B:
                # 역추적
                ops = []
                while parent[cur] is not None:
                    prev, op = parent[cur]
                    ops.append(op)
                    cur = prev
                print("".join(reversed(ops)))
                break
            
            for op, nxt in [("D", ins_D(cur)), ("S", ins_S(cur)),
                            ("L", ins_L(cur)), ("R", ins_R(cur))]:
                if not visited[nxt]:
                    visited[nxt] = True
                    parent[nxt] = (cur, op)
                    q.append(nxt)


if __name__ == "__main__":
    solution()