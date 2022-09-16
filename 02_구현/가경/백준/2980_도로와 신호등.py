import sys
input = sys.stdin.readline

n, l = map(int, input().split())
now, time = 0, 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += (d - now)
    now = d
    # 대기
    if time % (r + g) < r:
        time += (r - (time % (r + g)))
# 신호등을 모두 통과한 후
time += (l - now)
print(time)