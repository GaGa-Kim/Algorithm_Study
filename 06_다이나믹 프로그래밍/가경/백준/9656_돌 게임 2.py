import sys

n = int(sys.stdin.readline())

d = [-1] * 1001
d[1] = 1
d[2] = 0
d[3] = 1
for i in range(4, n + 1):
    # 돌을 1개 또는 3개 가져간 이전 턴이 1(상근)일 경우
    if d[i - 1] or d[i - 3]:
        # 다음 턴은 0(창영)
        d[i] = 0
    # 돌을 1개 또는 3개 가져간 이전 턴이 0(창영)일 경우
    else:
        # 다음 턴은 1(상근)
        d[i] = 1
print('SK' if d[n] == 0 else 'CY')
