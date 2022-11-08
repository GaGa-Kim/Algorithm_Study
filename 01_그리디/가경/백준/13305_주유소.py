import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
money = prices[0] # 현재 주유소의 리터당 가격
for i in range(n - 1):
    # 현재 주유소의 리터당 가격보다 가격이 작아질 경우
    if prices[i] < money:
        # 작은 가격으로 리터당 가격 변경
        money = prices[i]
    # 지금까지 왔던 거리에 대해 계산
    result += money * roads[i]
print(result)