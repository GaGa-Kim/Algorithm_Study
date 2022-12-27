# 최대공약수 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 함수
def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b)) 