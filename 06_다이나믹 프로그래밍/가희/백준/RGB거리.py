# 1149번
# 1번부터 n번 집이 순서대로 있을 때, RGB 중 하나로 칠해야 한다.
# 각 색으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서
# 모든 집을 칠하는 비용의 최솟값을 구하는 프로그램

# 1. 1번 집 색 != 2번 집 색
# 2. n번 집 색 != n-1번 집 색
# 3. i번 집 색 != i-1, i+1번 집 색 (2 ≤ i ≤ n-1)


# 2 ≤ n ≤ 1,000
n = int(input())

rgb = [list(map(int, input().split())) for _ in range(n)]

# 현재 집에서 각 색을 칠했을 때의 가장 적은 비용 저장해나감
for i in range(1, n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[-1]))
# print(min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2]))