import sys
input = sys.stdin.readline

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# 최대 고객 수에 따른 비용 DP 테이블
d = [1000000] * (c + 100)
d[0] = 0

for cost, people in city:
    for i in range(people, c + 100):
        # 현재 i명을 모집할 때의 도시에 대한 비용 / 과거 i명을 모집할 때 계산된 비용
        d[i] = min(d[i - people] + cost, d[i])
# c명일 때 최소 비용보다 c명 보다 더 많은 고객에 대한 최소 비용이 더 작을 수 있음
print(min(d[c:]))