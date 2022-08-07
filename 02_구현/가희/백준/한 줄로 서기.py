# 1138번
# 각 사람들이 기억하는 정보가 주어질 때, 
# 줄을 어떻게 서야 하는지 출력하는 프로그램

# 사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만 기억
# n명의 사람이 있고, 사람들의 키는 1부터 n까지 모두 다름

# 사람의 수 n (1 <= n <= 10)
n = int(input())

# 키가 1인 사람부터 차례대로
# 자기보다 키가 큰 사람이 왼쪽에 몇명 있었는지 (0 ~ n-i)
info = list(map(int, input().split()))

result = [0] * n 
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == info[i] and result[j] == 0:
            result[j] = i+1
            break
        elif result[j] == 0:
            cnt += 1

print(*result)
    