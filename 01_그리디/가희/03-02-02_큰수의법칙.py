# m의 크기가 커질 경우
# => 반복되는 수열 파악하여 해결

# 반복되는 수열의 길이 : (k+1)
# 가장 큰 수 등장 횟수: int(m/(k+1))*k + m % (k+1)
# m % (k+1) ~ 나머지 만큼 가장 큰 수가 추가로 더해질 것

# 배열의 크기 n, 숫자 더해지는 횟수 m, 제한 k ~공백 구분 입력
n, m, k = map(int, input().split())
# n개의 수 공백 구분 입력
data = list(map(int, input().split()))

# n개의 수 오름차순 정렬
data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수
count = m // (k+1) * k
count += m % (k+1)

result = 0
result += first*count  # 가장 큰 수 더하기
result += second*(m-count)  # 두 번째로 큰 수 더하기

print(result)