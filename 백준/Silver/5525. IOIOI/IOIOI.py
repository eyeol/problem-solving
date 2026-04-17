import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())
    S = input().strip()

    # N의 범위 때문에 완전 탐색 불가능
    # IO가 반복되면서 O가 N보다 길면 추적 시작

    longer = []

    tracking = False
    forward = None
    i_cnt = 0

    for i in range(M):
        if tracking:
            # 다르면 트래킹 계속
            if forward != S[i]:
                forward = S[i]
                # 트래킹 중 I 나오면 카운트 추가
                if S[i] == "I":
                    i_cnt += 1
            # 같으면 트래킹 종료
            else:
                tracking = False
                # 트래킹 종료 후 P_N 이상이면 기록
                if i_cnt >= N+1:
                    longer.append(i_cnt)

        # 트래킹 시작할지 안할지 여부
        if not tracking:
            if S[i] == "I":
                # 새로운 트래킹 시작
                tracking = True
                forward = "I"
                # 카운트 초기화
                i_cnt = 1

    # 트래킹하다가 끝나면 마지막 기록 추가
    if tracking and i_cnt >= N+1:
        longer.append(i_cnt)
    
    ans = 0
    for length in longer:
        ans += (length - N)

    print(ans)


if __name__ == "__main__":
    solution()
