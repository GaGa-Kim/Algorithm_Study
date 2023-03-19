import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
position = list(map(int, input().split()))
position.sort()

# 센서들끼리의 거리 차이
distance = []
for i in range(1, n):
    distance.append(position[i] - position[i - 1])

# 오름차순 정렬
distance.sort()
# n - k개의 거리 차이를 무시
print(sum(distance[:n - k]))