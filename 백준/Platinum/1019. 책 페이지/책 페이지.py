import sys

def solution():
    N = int(input())
    ans = [0] * 10

    start = 1
    pos = 1  # 1의 자리부터

    while start <= N:
        # start ~ N 범위에서 현재 자릿수 처리
        # 끝을 맞추기: start의 현재 자릿수를 0으로
        while start % 10 != 0 and start <= N:
            count_digit(start, ans, pos)
            start += 1

        if start > N:
            break

        # 시작을 맞추기: N의 현재 자릿수를 9로
        while N % 10 != 9 and start <= N:
            count_digit(N, ans, pos)
            N -= 1

        if start > N:
            break

        # start ~ N 사이: 현재 자릿수는 0~9가 균등하게 등장
        cnt = (N // 10 - start // 10 + 1)
        for d in range(10):
            ans[d] += cnt * pos

        start //= 10
        N //= 10
        pos *= 10

    print(*ans)

def count_digit(n, ans, pos):
    while n > 0:
        ans[n % 10] += pos
        n //= 10

if __name__ == "__main__":
    solution()