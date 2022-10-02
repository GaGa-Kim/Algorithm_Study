import math 

n = int(input())

if n == 2:
    a, b = map(int, input().split())
    result = math.gcd(a, b)

if n == 3:
    a, b, c = map(int, input().split())
    result = math.gcd(math.gcd(a, b), c)

# 최대 공약수의 약수
for i in range(1, (result // 2) + 1):
    if result % i == 0:
        print(i)
print(result)