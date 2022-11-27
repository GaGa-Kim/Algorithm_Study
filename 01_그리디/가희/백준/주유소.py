# 13305번
# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를
# 입력받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소 비용 계산

# n개의 도시가 일직선 도로 위에 있고, 
# 도로를 이용하여 이동할 때 1km마다 1L 기름 사용

# 도시의 개수 (2 <= n <= 100,000)
n = int(input())

# 인접한 두 도시 연결하는 도로 길이(왼쪽->오른쪽)
# 1 <= 거리 <= 1,000,000,000
road = list(map(int, input().split()))

# 주유소의 리터당 가격(왼쪽->오른쪽)
# 1 <= 가격 <= 1,000,000,000
price = list(map(int, input().split()))

result = road[0] * price[0] 
min_price = price[0] # 가장 저렴한 주유소

for i in range(1, n-1):
    if min_price > price[i]:
        min_price = price[i]
    result += road[i] * min_price

print(result)