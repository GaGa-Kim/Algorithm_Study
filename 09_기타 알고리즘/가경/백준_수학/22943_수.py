import sys, math
from itertools import permutations
input = sys.stdin.readline
MAX = 100001
prime_list = [True] * MAX

# 에라토스테네스의 체를 활용한 소수 판별
def makePrime():
    prime_list[0] = False
    prime_list[1] = False
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if prime_list[i]:
            for j in range(i * i, MAX, i):
                prime_list[j] = False

# 조건1 : 서로 다른 소수의 합
def makeSum(n):
    for i in range(2, n // 2 + 1):
        # 두 값이 서로 다르며 둘 다 소수일 경우
        if i != n - i and prime_list[i] and prime_list[n - i]:
            return True
    return False

# m으로 나누어 떨어지지 않을 때까지 나눈 수
def makeDivision(n, m):
    if n < m:
        return n
    while 1:
        if n % m != 0:
            return n
        n //= m
    return n

# 조건2 : 소수의 곱
def makeMulti(n, m):
    n = makeDivision(n, m)
    for i in range(2, int(math.sqrt(n)) + 1):
        # 둘 다 소수일 경우
        if n % i == 0 and prime_list[i] and prime_list[n // i]:
            return True
    return False

k, m = map(int, input().split())
makePrime()
answer = 0
# k개의 수를 뽑아줌
for num in permutations(['0', '1', '2', '3', '4', '5', '6', '7','8', '9'], k):
    # 뽑힌 수의 맨 앞 수가 0일 경우 continue
    if num[0] == '0':
        continue
    num = int(''.join(num))
    if makeSum(num):
        if makeMulti(num, m):
            answer += 1

print(answer)