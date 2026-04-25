import sys

input = sys.stdin.readline

class TrieNode:
    __slots__ = ['children', 'is_end', 'child_count']
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.child_count = 0

def solution():
    while True:
        try:
            N = int(input())
        except:
            break

        root = TrieNode()
        words = []
        for _ in range(N):
            word = input().strip()
            words.append(word)
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                    node.child_count += 1
                node = node.children[ch]
            node.is_end = True

        total = 0
        for word in words:
            cnt = 1  # 첫 글자는 반드시 입력
            node = root.children[word[0]]
            for i in range(1, len(word)):
                ch = word[i]
                # 자식이 2개 이상이거나 현재가 단어 끝이면 입력 필요
                if node.child_count > 1 or node.is_end:
                    cnt += 1
                node = node.children[ch]
            total += cnt

        print(f"{total / N:.2f}")

if __name__ == "__main__":
    solution()