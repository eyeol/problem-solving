import sys

input = sys.stdin.readline
INF = float('inf')

def solution():
    N = int(input())
    M = int(input())

    # 거리 테이블 초기화
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0  # 자기 자신은 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)  # 같은 경로 여러 개 → 최솟값

    # 플로이드-워셜: k를 경유지로
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 출력
    for i in range(1, N + 1):
        row = []
        for j in range(1, N + 1):
            row.append(0 if dist[i][j] == INF else dist[i][j])
        print(*row)

if __name__ == "__main__":
    solution()