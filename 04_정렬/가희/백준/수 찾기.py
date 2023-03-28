# 1920번
# n개의 정수가 주어졌을 때, 이 안에 x라는 정수가 존재하는지 알아내는 프로그램
# 시간 초과 => 이진탐색으로 풀어야 함

# 1 ≤ n ≤ 100,000
n = int(input())
arr = list(map(int, input().split()))

# 1 ≤ m ≤ 100,000
m = int(input())
num = list(map(int, input().split()))


for j in num:
    if j in arr:
        print(1)
    else:
        print(0)