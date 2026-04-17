import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())
    S = input().strip()

    ans = 0
    i = 0

    while i <= M - 3:
        if S[i] == "I" and S[i+1] == 'O' and S[i+2] == "I":
            # 첫번째 i만 카운트
            cnt = 1
            while i+2 < M and S[i+1] == "O" and S[i+2] == "I":
                cnt += 1
                i += 2 # 2칸씩 전진하면서 탐색
            if cnt > N:
                ans += cnt - N
            i += 1
        else: 
            i += 1

    print(ans)

if __name__ == "__main__":
    solution()
