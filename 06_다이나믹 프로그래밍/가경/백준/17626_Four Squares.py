import sys
input = sys.stdin.readline

n = int(input())
# 제곱수 합 DP 테이블
d = [0] * (n + 1)
d[1] = 1
for i in range(2, n + 1):
    min_value = 4 # 제곱수의 최대 개수는 4개
    j = 1
    # n보다 작거나 같은 제곱수를 찾고
    while (j ** 2) <= i:
        # n - (n보다 작거나 같은 제곱수)를 인덱스로 갖는 값에 1을 더해줌
        min_value = min(min_value, d[i - (j ** 2)])
        j += 1
    # d[i - (j ** 2)] + 1
    d[i] = min_value + 1
print(d[n])