import sys
input = sys.stdin.readline

n = int(input())
number = sorted(list(map(int, input().split())))
if (n % 2) == 0:
    print(number[(n // 2) - 1])
else:
    print(number[n // 2])