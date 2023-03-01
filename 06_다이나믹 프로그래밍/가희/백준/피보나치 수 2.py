# 2748번
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램
# Fn = Fn-1 + Fn-2 (n >= 2)

n = int(input())

d = [0] * (n+1)

d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])