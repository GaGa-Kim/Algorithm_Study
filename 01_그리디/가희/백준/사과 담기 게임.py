# 2828번
# 모든 사과를 담기 위해 바구니가 이동해야 하는 거리의 최솟값 구하는 프로그램
# n칸으로 나눠진 스크린과, 스크린 아래쪽에는 m칸을 차지하는 바구니가 있을 때 (m < n), 
# 바구니는 초기에 왼쪽 m칸을 차지하고 있으며, 좌우로 움직일 수 있다.

import sys
input = sys.stdin.readline

# 1 <= m < n <= 10
n, m = map(int, input().split())

# 떨어지는 사과 개수 j (1 <= j <= 20)
j = int(input())

# 사과가 떨어지는 위치
data = [int(input()) for _ in range(j)]

left = 1                # 바구니 초기 왼쪽 위치
right = left + (m-1)    # 왼쪽 + (바구니 크기 - 1)
result = 0
for i in data:
    # left보다 작은 위치에 떨어질 경우
    if i < left:
        move = left - i
        left -= move
        right -= move
        result += move
    # right보다 큰 위치에 떨어질 경우
    if i > right:
        move = i - right
        left += move
        right += move
        result += move
    # 바구니의 left와 right 사이에 떨어질 경우
    if left <= i and i <= right:
        continue

print(result)
