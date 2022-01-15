# min()함수 이용

# 행 n, 열 m 공백 구분 입력
# 1 <= n, m <= 100
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 최솟값
    min_value = min(data)
    # 최솟값들 중 최댓값
    result = max(result, min_value)

print(result)