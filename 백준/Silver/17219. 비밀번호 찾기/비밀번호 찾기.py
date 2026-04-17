import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    site_pwd = {}

    for _ in range(N):
        site, pwd = input().strip().split()
        site_pwd[site] = pwd

    for _ in range(M):
        site = input().strip()
        print(site_pwd[site])



if __name__ == "__main__":
    solution()
