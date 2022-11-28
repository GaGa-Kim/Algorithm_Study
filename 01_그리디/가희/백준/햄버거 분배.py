# 19941번
# 식탁의 길이 n, 햄버거를 선택할 수 있는 거리 k, 사람과 햄버거의 위치가
# 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램

# 사람들은 자신의 위치에서 거리가 k이하인 햄버거를 먹을 수 있다.

# 1 <= n <= 20,000 / 1 <= k <= 10
n, k = map(int, input().split())

# 사람(P)과 햄버거(H)의 위치
data = list(input())

# 햄버거를 먹을 수 있는 최대 사람 수
result = 0

for i in range(n):
    if data[i] == 'P':
        # 사람 위치에서 양쪽으로 k 범위 안에서 햄버거 확인
        for j in range(i-k, i+k+1):
            if 0 <= j < n and data[j] == 'H':
                result += 1
                data[j] = 0 # 먹은 표시
                break

print(result)
