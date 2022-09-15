import sys
input = sys.stdin.readline

n = int(input())
minute = list(map(int, input().split()))
minute.sort()

sum = 0
for i in range(n):
    for j in range(i + 1):
        sum += minute[j]
print(sum)