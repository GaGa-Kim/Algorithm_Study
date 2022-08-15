# 15486번
# 상담을 적절히 했을 때, 얻을 수 있는 최대 수익 구하는 프로그램

# 오늘부터 n+1일째 되는 날 퇴사하기 위해 
# 남은 n일 동안 최대한 많은 상담을 할 예정 (1 ≤ N ≤ 1,500,000) **조건 바뀐 부분**
# => 그대로 dp로 풀 수 있음 (완전탐색으로는 불가능)

# 상담은 하루에 하나씩 서로 다른 사람
# Ti ~ 상담을 완료하는 데 걸리는 기간 (1 <= Ti <= 5)
# Pi ~ 상담했을 때 받을 수 있는 금액 (1 <= Pi <= 1,000)

import sys
input = sys.stdin.readline

n = int(input())

t, p = [], []
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    
d = [0] * (n+1)

for i in range(n-1, -1, -1):
    # i일에 상담을 하는 게 퇴사일 넘기면 상담x
    if i + t[i] > n:
        d[i] = d[i+1]
    else: # i일에 상담 안 하는 것과 하는 것 중 최댓값
        d[i] = max(d[i+1], p[i] + d[i+t[i]])

print(d[0])