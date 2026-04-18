import sys

input = sys.stdin.readline

def solution():

    N, M, B = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    def calculate_time(h: int, bag: int, cur_min):
        time = 0
        for i in range(N):
            for j in range(M):
                diff = h - ground[i][j]
                # 블록 채워넣어야 함 - 1초 소모
                if diff >= 0:
                    time += diff
                else: # 블록 제거해서 가방에 넣음 - 2초 소모
                    time += diff*(-2)
                # 박스 정리
                bag -= diff

                # early return
                if time > cur_min:
                    return -1
                
        if bag < 0: # 평탄화하기에 블록이 모자람
            return -1
        else:
            return time
    
    min_time = 1000_000_000
    ans_h = 0

    for h in range(257): # 0~256
        time_cost = calculate_time(h, B, min_time)
        if time_cost != -1 and time_cost <= min_time:
            ans_h = h
            min_time = time_cost
        # 시간이 동일하게 걸렸다면 높은 높이가 출력되도록
    
    print(min_time, ans_h)


if __name__ == "__main__":
    solution()
