import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        N, M, W = map(int, input().split())
        edges = []

        for _ in range(M):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))   
            edges.append((e, s, t))

        for _ in range(W):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))  

        dist = [0] * (N + 1)  

        negative_cycle = False
        for i in range(N):
            for s, e, t in edges:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
                    if i == N - 1:
                        negative_cycle = True

        print("YES" if negative_cycle else "NO")

if __name__ == "__main__":
    solution()