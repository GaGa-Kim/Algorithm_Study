# <특정한 합을 가지는 부분 연속 수열 찾기>
# : 양의 정수로만 구성된 리스트가 주어졌을 때, 그 부분 연속 수열 중에서 특정한 합을 갖는 수열의 개수 출력

# 특정 부분합 = M이라고 할 때,
# 1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
# 2. 현재 부분합이 M과 같다면 카운트한다.
# 3. 현재 부분합이 M보다 작으면 end + 1
# 4. 현재 부분합이 M보다 크거나 같으면 start + 1

n = 5                   # 데이터 개수 
m = 5                   # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]  # 전체 수열

count = 0 
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)