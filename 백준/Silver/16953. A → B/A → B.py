import sys
from collections import deque

input = sys.stdin.readline

def solution():
    A, B = map(int, input().split())

    # (숫자, 도달하기까지 한 연산)
    q = deque([(A, 1)])

    while q:
        cur_num, cur_op = q.popleft()
        if cur_num > B:
            continue
        if cur_num == B:
            print(cur_op)
            return
        nxt_num_1 = cur_num * 2
        nxt_num_2 = int(str(cur_num) + "1")
        q.append((nxt_num_1, cur_op+1))
        q.append((nxt_num_2, cur_op+1))

    print(-1)

if __name__ == "__main__":
    solution()