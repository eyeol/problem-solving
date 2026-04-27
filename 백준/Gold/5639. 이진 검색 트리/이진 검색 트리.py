import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solution():
    nums = []
    while True:
        try:
            line = input().strip()
            if line == '':
                break
            nums.append(int(line))
        except:
            break

    result = []

    def post_order(start, end):
        if start > end:
            return

        root = nums[start]

        # 루트보다 큰 값이 처음 나오는 위치 = 오른쪽 서브트리 시작
        mid = start + 1
        while mid <= end and nums[mid] < root:
            mid += 1

        post_order(start + 1, mid - 1)  # 왼쪽
        post_order(mid, end)             # 오른쪽
        result.append(str(root))         # 루트

    post_order(0, len(nums) - 1)
    print('\n'.join(result))

if __name__ == "__main__":
    solution()