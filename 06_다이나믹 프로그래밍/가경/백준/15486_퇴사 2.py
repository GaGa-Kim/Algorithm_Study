import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
# 각 날짜의 최대 수익
d = [0] * (n + 1)
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

money = 0
for i in range(n):
    money = max(money, d[i])
    # 퇴사 이후는 제외
    if i + t[i] > n:
        continue
    # 이전까지의 수익 + 이번 상담의 수익 / 이번 상담의 종료일 시점의 상담 수익
    d[i + t[i]] = max(money + p[i], d[i + t[i]])
print(max(d))
