# 1072번
# 게임 횟수와 이긴 게임 횟수가 주어졌을 때, 
# 게임을 최소 몇 번 더 해야 z가 변하는지 구하는 프로그램
# z가 절대 변하지 않는다면 -1 출력

# <게임 기록>
# - 게임 횟수 : x
# - 이긴 게임 : y (z%)
# - z는 형택이의 승률, 소수점은 버림, 

from math import floor
import sys
input = sys.stdin.readline

# 1 <= x <= 1,000,000,000 / 0 <= y <= x
x, y = map(int, input().split())

z = floor(100 * y / x)

start, end = 0, 1000000000
if z >= 99: # 승률 99보다 높아질 수 없음
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        # mid번 이겼을 때 승률
        if floor(100 * (y + mid) / (x + mid)) > z:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1)