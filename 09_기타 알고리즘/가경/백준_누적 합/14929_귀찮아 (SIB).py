import sys
input = sys.stdin.readline

n = int(input())
xi = list(map(int, input().split()))
num = [0]
for i in range(1, n):
    # [x1, x1 + x2, x1 + x2 + x3]
    num.append(num[i - 1] + xi[i])

result = 0
for i in range(n):
    # x1 * (x2 + x3) + x2 * (x3)
    result += xi[i] * (num[n - 1] - num[i])
print(result)