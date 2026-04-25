import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    result = n
    temp = n
    p = 2

    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1

    if temp > 1:
        result -= result // temp

    print(result)

if __name__ == "__main__":
    solution()