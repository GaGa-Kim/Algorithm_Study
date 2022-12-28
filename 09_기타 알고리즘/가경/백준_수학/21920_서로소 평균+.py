import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
sequence = list(map(int, input().split()))
x = int(input())
total = 0
count = 0
for i in sequence:
    # 두 수의 최대공약수가 1이면 서로소
    if gcd(x, i) == 1:
        total += i
        count += 1
print(total / count)
