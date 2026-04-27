import sys

input = sys.stdin.readline

def solution():
    s = input().strip()
    bomb = input().strip()
    blen = len(bomb)

    stack = []
    for ch in s:
        stack.append(ch)
        if len(stack) >= blen and ''.join(stack[-blen:]) == bomb:
            del stack[-blen:]

    result = ''.join(stack)
    print(result if result else "FRULA")

if __name__ == "__main__":
    solution()