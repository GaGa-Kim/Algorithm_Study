# 파라메트릭 + 이진탐색
# n개의 떡이 있을 때 손님이 적어도 m 길이 만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

# => 이진탐색을 이용해 적절한 높이를 찾을 때까지 절단기의 높이 반복해서 조정

# 1 <= n <= 1,000,000 / 1 <= m <= 2,000,000,000
n, m = map(int, input().split())

# 각 떡의 개별 높이 정보 (높이 <= 10억 또는 0)
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid: 
            total += x-mid
    
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색) ~> 높이 값 감소
    if total > m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색) ~> 높이 값 증가
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 기록
        start = mid + 1

print(result)
