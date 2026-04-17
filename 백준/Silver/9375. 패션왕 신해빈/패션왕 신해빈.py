import sys

input = sys.stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        N = int(input())
        clothes = {}

        for _ in range(N):
            item, part = input().split()
            if part not in clothes.keys():
                clothes[part] = [item]
            else:
                clothes[part].append(item)

        keys = clothes.keys()

        ans = 1

        # 하나만 입는거
        for key in keys:
            ans *= (len(clothes[key])+1)
        
        ans -= 1

        print(ans)



if __name__ == "__main__":
    solution()
