import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)

def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        s = [0] + list(map(int, input().split()))  # 1-indexed

        state = [0] * (N + 1)  # 0: 미방문, 1: 탐색중, 2: 완료
        in_cycle = 0

        for i in range(1, N + 1):
            if state[i] != 0:
                continue

            path = []
            cur = i
            while state[cur] == 0:
                state[cur] = 1
                path.append(cur)
                cur = s[cur]

            if state[cur] == 1:
                # cur부터 사이클
                idx = 0
                while path[idx] != cur:
                    idx += 1
                in_cycle += len(path) - idx

            for node in path:
                state[node] = 2

        print(N - in_cycle)

if __name__ == "__main__":
    solution()