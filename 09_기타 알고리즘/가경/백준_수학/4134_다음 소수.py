import sys, math
input = sys.stdin.readline

def isPrimeNumber(n):
    # 0과 1을 제외한 자기 자신으로만 나누어 떨어질 때 소수
    if n == 0 or n == 1:
        return False
    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(n)) + 1):
        # 소수가 아닐 경우 False
        if n % i == 0:
            return False
    # 소수일 경우 True
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        # 소수일 때까지 +1을 하면서 구함
        if isPrimeNumber(n):
            print(n)
            break
        else:
            n += 1