import sys

input = sys.stdin.readline


def solution():
    expr = input().strip()

    op_priority = {}
    op_priority["+"] = 1
    op_priority["-"] = 1
    op_priority["*"] = 2
    op_priority["/"] = 2

    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []          # 연산자 대기실
    result = []

    for ch in expr:
        if ch.isalpha():
            result.append(ch)
        
        elif ch == "(":
            stack.append(ch)
        
        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop() # (도 같이 pop

        else:
            # 연산자 우선순위
            while stack and stack[-1] != "(" and priority[stack[-1]] >= priority[ch]:
                result.append(stack.pop())
            stack.append(ch)
    
    while stack:
        result.append(stack.pop())

    print("".join(result))


if __name__ == "__main__":
    solution()