import sys

input = sys.stdin.readline
INF = float('inf')

def solution():
    N, m, r = map(int, input().split())
    items = list(map(int, input().split()))

    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for _ in range(r):
        a, b, l = map(int, input().split())
        a -= 1; b -= 1
        dist[a][b] = min(dist[a][b], l)
        dist[b][a] = min(dist[b][a], l)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    ans = 0
    for i in range(N):
        total = 0
        for j in range(N):
            if dist[i][j] <= m:
                total += items[j]
        ans = max(ans, total)

    print(ans)

if __name__ == "__main__":
    solution()