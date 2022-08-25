import sys
input = sys.stdin.readline

h, y = map(int, input().split())
d = [0] * (y + 1)
d[0] = h

for i in range(1, y + 1):
    # 투자 기한이 5년 이상일 경우
    if i >= 5:
        d[i] = max(d[i - 1] * 1.05, d[i - 3] * 1.2, d[i - 5] * 1.35)
    # 투자 기한이 5년 미만 3년 이상일 경우
    elif i >= 3:
        d[i] = max(d[i - 1] * 1.05, d[i - 3] * 1.2)
    # 투자 기한이 3년 미만일 경우
    else:
        d[i] = d[i - 1] * 1.05
    # 매번 이율은 소수점 이하를 버림
    d[i] = int(d[i])
print(int(d[y]))