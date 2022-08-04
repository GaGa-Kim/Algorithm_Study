import sys
input = sys.stdin.readline

n = int(input())
number = [int(input().strip()) for _ in range(n)]
number.sort()

answer = 4
for i in range(n):
    count = 0
    for j in range(number[i], number[i] + 5):
        if j not in number:
            count += 1
    answer = min(answer, count)
print(answer)
