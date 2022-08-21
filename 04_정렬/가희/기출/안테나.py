# 백준 18310번
# 집들의 위치 값이 주어질 때, 
# 안테나로부터 모든 집까지의 거리 총합이 최소가 되도록 위치 선택하는 프로그램

# 안테나는 집이 위치한 곳에만 설치 가능, 논리적으로 동일 위치 가능
# 결과가 여러 개일 경우, 가장 작은 값 출력

# 집의 수 n (1 <= n <= 200,000)
n = int(input())

# 집 위치
array = list(map(int, input().split()))

array.sort()

# 중간값 출력
print(array[(n-1) // 2])
