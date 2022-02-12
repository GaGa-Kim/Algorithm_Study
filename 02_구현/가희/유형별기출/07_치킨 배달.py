# 백준 15686, 완전 탐색

# 크기가 N*N인 도시 ~ 빈칸(0), 집(1), 치킨집(2)
# 집의 개수 2N개 넘지 x, 최소 1개
# (r,c) ~ (행,열), 각각 1부터 시작
# |r1-r2| + |c1-c2|

# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합

# 수익을 가장 많이 낼 수 있는 치킨집 개수 최대 M개
# 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하기

from itertools import combinations

# 2 <= N <= 50, 1 <= M <= 13
n, m = (map(int, input().split()))
chicken, house = [], []

for r in range(n):  # n개의 줄에 도시의 정보 입력 받음
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

# 모든 치킨집 중 m개 뽑는 조합 계산
candidiates = list(combinations(chicken, m))


def get_sum(candidate):  # 도시의 치킨 거리(=치킨 거리의 합) 계산 함수
    result = 0
    for hx, hy in house:
        # 가장 가까운 치킨집 찾기
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx-cx)+abs(hy-cy))
        result += tmp
    return result


# 도시의 치킨거리 최솟값 구하기
result = 1e9
for candidiate in candidiates:
    result = min(result, get_sum(candidate))

print(result)
