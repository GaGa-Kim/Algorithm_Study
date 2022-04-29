# 안테나.py
n = int(input()) # 집의 수
data = list(map(int, input().split())) # 집의 위치
data.sort()

# 중간값(median)을 출력
print(data[(n - 1) // 2])