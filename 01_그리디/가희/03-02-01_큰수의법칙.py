# M <= 10,000이라 가능한 풀이

# 배열의 크기 n, 숫자 더해지는 횟수 m, 제한 k ~ 공백 구분 입력
n, m, k = map(int, input().split())
# n개의 수 공백 구분 입력
data = list(map(int, input().split()))

# n개의 수 오름차순 정렬
data.sort()
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

result = 0
while True:
    # 가장 큰 수 k번 더함
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)