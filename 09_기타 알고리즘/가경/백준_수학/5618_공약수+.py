import math 

def gcd(a, b):
    if a == 0:
        return b
    return math.gcd(b % a, a)

n = int(input())
s = list(map(int, input().split()))
result = gcd(s[0], gcd(s[1], s[-1]))

# 최대 공약수의 약수
for i in range(1, (result // 2) + 1):
    if result % i == 0:
        print(i)
print(result)