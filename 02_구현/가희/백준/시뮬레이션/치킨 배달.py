# 15686번 (유형별기출)
# 도시에 있는 치킨집 중 최대 m개를 고르고, 나머지 치킨집은 폐업시킬 때,
# 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램

# 도시 크기 n x n (1 x 1 칸들로 구성)
# 0: 빈 칸, 1: 집, 2: 치킨집
# (r, c) ~ r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸

# 치킨 거리 ~ 집과 가장 가까운 치킨집 사이의 거리 (|r1 - r2| + |c1- c2|)
# 도시의 치킨 거리 ~ 모든 집의 치킨 거리의 합

from itertools import combinations
# 2 ≤ n ≤ 50, 1 ≤ m ≤ 13
n, m = map(int, input().split())
chicken, house = [], []

# 도시 정보 (0: 빈 칸, 1: 집, 2: 치킨집)
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

# 모든 치킨 집 중 m개 뽑는 조합
candidates = list(combinations(chicken, m))

# 도시의 치킨 거리 구하기
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        result += tmp
    return result

# 도시의 치킨거리 최솟값 
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)