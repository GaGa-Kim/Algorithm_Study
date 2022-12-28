import sys, math
input = sys.stdin.readline

def isPrimeNumber(n):
    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(n)) + 1):
        # 소수가 아닐 경우 False
        if n % i == 0:
            return False
    # 소수일 경우 True
    return True

n = int(input())
sequence = set(map(int, input().split()))
answer = 1
for i in sequence:
    if isPrimeNumber(i):
        # 소수들끼리의 최소공배수는 단순곱
        answer *= i

if answer == 1:
    print(-1)
else:
    print(answer)
