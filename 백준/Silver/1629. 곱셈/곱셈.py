import sys

input = sys.stdin.readline


def solution():
    A, B, C = map(int, input().split())
    new_A = A % C

    def mod_power(a, b, c):
        result = 1
        while b > 0:
            # 이진수 상에서 일의 자리가 1이면 곱하기
            if b % 2 == 1:
                result = (result * a) % c

            # 이진수 표현에서 한칸씩 증가
            a = (a * a) % c
            b //= 2
        
        return result
    
    ans = mod_power(A, B, C)
    print(ans)


if __name__ == "__main__":
    solution()