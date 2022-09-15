import sys
input = sys.stdin.readline

n = int(input())
price = [int(input()) for _ in range(n)]
price = sorted(price, reverse=True)

index = 2 # 처음 3번째 인덱스
sum = 0
for i in range(n):
    if (i == index):
        index += 3
        continue
    sum += price[i]
print(sum)