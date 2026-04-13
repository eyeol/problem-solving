n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

diff_sum = 1000_000_000

for i in range(n): # 0부터 n-1
    # i는 회의할 집 인덱스
    diff = 0
    for j in range(n):
        num_people = A[j]
        diff += num_people * abs(j - i)
    
    if diff < diff_sum:
        diff_sum = diff

print(diff_sum)
