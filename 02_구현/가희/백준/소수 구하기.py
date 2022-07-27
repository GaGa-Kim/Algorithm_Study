# 1929번
# M 이상 N 이하 소수를 모두 출력하는 프로그램

import math

# 1 ≤ M ≤ N ≤ 1,000,000
# 소수가 하나 이상 있는 입력만 주어짐
m, n = map(int, input().split())

list = [True for _ in range(n+1)]
list[1] = 0 # 1은 소수 아님

for i in range(2, int(math.sqrt(n))+1):
    if list[i]:
        j = 2
        while i*j <= n:
            list[i*j] = False
            j += 1

for i in range(m, n+1):
    if list[i]:
        print(i)