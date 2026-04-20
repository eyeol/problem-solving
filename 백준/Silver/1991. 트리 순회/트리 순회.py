import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    tree = {}
    for _ in range(N):
        p, l, r = input().split()
        tree[p] = (l, r)


    def preorder(node):
        if node == ".":
            return ""
        l, r = tree[node]
        return node + preorder(l) + preorder(r)
    
    def inorder(node):
        if node == ".":
            return ""
        l, r = tree[node]
        return inorder(l) + node + inorder(r)
    
    def postorder(node):
        if node == ".":
            return ""
        l, r = tree[node]
        return postorder(l) + postorder(r) + node

    print(preorder("A"))
    print(inorder("A"))
    print(postorder("A"))


if __name__ == "__main__":
    solution()