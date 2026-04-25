import sys

input = sys.stdin.readline

def solution():
    while True:
        line = list(map(int, input().split()))
        if line[0] == 0:
            break
        n = line[0]
        heights = line[1:]

        stack = []
        ans = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            w = n if not stack else n - stack[-1] - 1
            ans = max(ans, h * w)

        print(ans)

if __name__ == "__main__":
    solution()