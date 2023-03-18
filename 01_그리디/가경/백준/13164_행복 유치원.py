import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

# 원생들끼리의 키 차이
height_diff = []
for i in range(1, n):
    height_diff.append(kids[i] - kids[i - 1])

# 오름차 순 정렬
height_diff.sort()
# n - k개의 키 차이를 무시
print(sum(height_diff[:n - k]))
