# 2960번
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램

# 에라토스테네스의 체) N보다 작거나 같은 모든 소수를 찾는 알고리즘

# 1. 2부터 N까지 모든 정수를 적는다.
# 2. 아직 지우지 않은 수 중 가장 작은 수(P, 소수)를 찾는다.
# 3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 4. 아직 모든 수를 지우지 않았다면 다시 2번으로 간다.
import math

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# N, K (1 <= K < N, max(1,K) < N <= 1000)
n, k = map(int, input().split())

list = []
for i in range(2, n+1):
    if is_prime_num(i):
        if i not in list:
            list.append(i)
        for j in range(i+1, n+1):
            if j % i == 0:
                if j not in list:
                    list.append(j)

print(list[k-1])

#------------------------------------------------------
n, k = map(int, input().split())
# 처음엔 모든 수가 소수라고 초기화
list = [True for _ in range(n+1)]

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if list[j]:
            list[j] = False
            k -= 1
            if k == 0:
                print(j)

