import sys
input = sys.stdin.readline

def solution():
    C, N = map(int, input().split())

    # 색상 접두사 집합
    colors = set()
    for _ in range(C):
        colors.add(input().strip())

    # 닉네임 접미사 집합
    nicks = set()
    for _ in range(N):
        nicks.add(input().strip())

    # 색상 가능한 길이 집합 (빠른 조회용)
    color_lens = set()
    for c in colors:
        color_lens.add(len(c))

    Q = int(input())
    out = []
    for _ in range(Q):
        team = input().strip()
        L = len(team)
        found = False

        for cl in color_lens:
            if cl >= L:
                continue
            if team[:cl] in colors and team[cl:] in nicks:
                found = True
                break

        out.append("Yes" if found else "No")

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    solution()