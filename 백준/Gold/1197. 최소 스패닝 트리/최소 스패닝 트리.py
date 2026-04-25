import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, rank, a, b):
    a, b = find(parent, a), find(parent, b)
    if a == b:
        return False  # 이미 같은 집합 → 사이클
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1
    return True

def solution():
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()  # 가중치 기준 정렬

    parent = list(range(V + 1))
    rank = [0] * (V + 1)

    total = 0
    count = 0
    for cost, a, b in edges:
        if union(parent, rank, a, b):
            total += cost
            count += 1
            if count == V - 1:  # 트리 완성
                break

    print(total)

if __name__ == "__main__":
    solution()