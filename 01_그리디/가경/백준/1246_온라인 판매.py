import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [int(input()) for _ in range(m)]
# 계란 가격 정렬
p = sorted(p, reverse=True)

price = 0
profit = 0
for i in range(m):
    # 고객이 계란의 개수보다 많은 경우, 계란의 개수만큼 판매됨
    if i + 1 > n:
        egg = n
    # 고객보다 계란의 개수가 많거나 같은 경우, 고객의 개수만큼 판매됨
    else:
        egg = i + 1 
    if profit < p[i] * egg:
        profit = p[i] * egg
        price = p[i]

print(price, profit)